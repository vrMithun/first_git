#include <Arduino.h>
#include <stdlib.h>
#include <SD.h>

#define in1 5
#define in2 6
#define in3 10
#define in4 11
#define LED 13

struct RobotConfig {
  int speed;
  int turnRadius;
  int brakeTime;
  int lastCommand;
  int ledPin;
  int* motorPins;
};

RobotConfig* initRobotConfig() {
  RobotConfig* config = (RobotConfig*)malloc(sizeof(RobotConfig));
  config->speed = 204;
  config->turnRadius = 0;
  config->brakeTime = 45;
  config->lastCommand = 0;
  config->ledPin = LED;

  config->motorPins = (int*)malloc(4 * sizeof(int));
  config->motorPins[0] = in1;
  config->motorPins[1] = in2;
  config->motorPins[2] = in3;
  config->motorPins[3] = in4;

  return config;
}

void saveCommandHistory(int* commandHistory, int size) {
  if (!SD.begin(4)) {
    return;
  }
  File file = SD.open("commandHistory.txt", FILE_WRITE);
  if (file) {
    for (int i = 0; i < size; i++) {
      file.println(commandHistory[i]);
    }
    file.close();
  }
}

RobotConfig* config;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  config = initRobotConfig();

  for (int i = 0; i < 4; i++) {
    pinMode(config->motorPins[i], OUTPUT);
  }
  
  SD.begin(4);
  File file = SD.open("commandHistory.txt", FILE_WRITE);
  file.close();
}

void loop() {
  static int commandHistory[100];
  static int historyIndex = 0;

  if (Serial.available() > 0) {
    int command = Serial.read();
    config->lastCommand = command;

    if (historyIndex < 100) {
      commandHistory[historyIndex++] = command;
    }

    switch (command) {
      case 'F': forward(config); break;
      case 'B': back(config); break;
      case 'L': left(config); break;
      case 'R': right(config); break;
      case 'S': Stop(config); break;
      case 'q': config->speed = 255; break;
    }

    if (command == 'S') {
      brakeOn(config);
    }
  }

  if (historyIndex >= 100) {
    saveCommandHistory(commandHistory, historyIndex);
    historyIndex = 0;
  }
}

void forward(RobotConfig* config) {
  analogWrite(config->motorPins[0], config->speed);
  analogWrite(config->motorPins[2], config->speed);
  analogWrite(config->motorPins[1], 0);
  analogWrite(config->motorPins[3], 0);
}

void back(RobotConfig* config) {
  analogWrite(config->motorPins[1], config->speed);
  analogWrite(config->motorPins[3], config->speed);
  analogWrite(config->motorPins[0], 0);
  analogWrite(config->motorPins[2], 0);
}

void left(RobotConfig* config) {
  analogWrite(config->motorPins[2], config->speed);
  analogWrite(config->motorPins[1], config->speed);
  analogWrite(config->motorPins[0], 0);
  analogWrite(config->motorPins[3], 0);
}

void right(RobotConfig* config) {
  analogWrite(config->motorPins[3], config->speed);
  analogWrite(config->motorPins[0], config->speed);
  analogWrite(config->motorPins[1], 0);
  analogWrite(config->motorPins[2], 0);
}

void Stop(RobotConfig* config) {
  for (int i = 0; i < 4; i++) {
    analogWrite(config->motorPins[i], 0);
  }
}

void brakeOn(RobotConfig* config) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(config->motorPins[i], HIGH);
  }
  delay(config->brakeTime);
  Stop(config);
}
