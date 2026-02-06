#include "stm32f4xx.h"
#include "stdio.h"

volatile uint16_t val = 0;
char buffer[50];

//-------------------- USART2 Initialization --------------------
void usart_init(void) {
    // 1. Enable clocks for GPIOA and USART2
    RCC->AHB1ENR |= (1 << 0);      // GPIOA clock enable
    RCC->APB1ENR |= (1 << 17);     // USART2 clock enable

    // 2. Set PA2 -> USART2_TX (AF7), PA3 -> USART2_RX (AF7)
    GPIOA->MODER &= ~((3 << 4) | (3 << 6));   // Clear mode bits
    GPIOA->MODER |=  ((2 << 4) | (2 << 6));   // Alternate function mode

    GPIOA->AFR[0] &= ~((0xF << 8) | (0xF << 12)); // Clear AF bits
    GPIOA->AFR[0] |=  ((7 << 8) | (7 << 12));     // AF7 for USART2

    // 3. Configure USART2: 9600 baud, 8 data bits, 1 stop bit
    USART2->BRR = 0x0683;   // 9600 @ 16 MHz
    USART2->CR1 |= (1 << 2) | (1 << 3);  // Enable RX, TX
    USART2->CR1 |= (1 << 13);            // Enable USART
}

//-------------------- Send String Function --------------------
void send_string(char *str) {
    while (*str) {
        while (!(USART2->SR & (1 << 7)));  // Wait until TXE = 1
        USART2->DR = *str++;
    }
}

//-------------------- ADC1 Initialization --------------------
void adc_init(void) {
    // 1. Enable GPIOA and ADC1 clocks
    RCC->AHB1ENR |= (1 << 0);   // GPIOA clock
    RCC->APB2ENR |= (1 << 8);   // ADC1 clock

    // 2. Set PA0 (ADC1_IN0) to analog mode
    GPIOA->MODER |= (3 << 0);   // Analog mode (11)

    // 3. Configure ADC
    ADC1->SQR3 = 0;             // Channel 0 first in sequence
    ADC1->CR1 |= (1 << 5);      // Enable EOC interrupt
    ADC1->CR2 |= (1 << 1);      // Continuous conversion mode
    ADC1->CR2 |= (1 << 0);      // ADC ON
    ADC1->CR2 |= (1 << 30);     // Start conversion

    // 4. Enable ADC interrupt in NVIC
    NVIC_EnableIRQ(ADC_IRQn);
}

//-------------------- ADC Interrupt Handler --------------------
void ADC_IRQHandler(void) {
    if (ADC1->SR & (1 << 1)) {       // Check EOC flag
        val = ADC1->DR;              // Read data (clears EOC flag)
        ADC1->SR &= ~(1 << 1);       // Explicitly clear EOC flag
    }
}

//-------------------- Delay Function using SysTick --------------------
void delay(uint32_t ms) {
    SysTick->LOAD = 16000 - 1;  // 1 ms tick for 16 MHz
    SysTick->VAL = 0;
    SysTick->CTRL = 0x5;        // Enable SysTick, no interrupt

    for (uint32_t i = 0; i < ms; i++) {
        while ((SysTick->CTRL & (1 << 16)) == 0);
    }
    SysTick->CTRL = 0;          // Stop SysTick
}

//-------------------- Main Function --------------------
int main(void) {
    adc_init();
    usart_init();

    // Enable GPIOC (button) and GPIOD (LED)
    RCC->AHB1ENR |= (1 << 2);  // GPIOC clock
    RCC->AHB1ENR |= (1 << 3);  // GPIOD clock

    // Configure PC13 (button) as input with pull-up
    GPIOC->MODER &= ~(3 << 26);  // Input mode
    GPIOC->PUPDR &= ~(3 << 26);
    GPIOC->PUPDR |=  (1 << 26);  // Pull-up

    // Configure PD12 (LED) as output
    GPIOD->MODER &= ~(3 << 24);
    GPIOD->MODER |=  (1 << 24);

    while (1) {
        // 1️⃣ Send ADC value if above threshold
        if (val > 2000) {
            sprintf(buffer, "ADC value high: %u\r\n", val);
            send_string(buffer);
        }

        // 2️⃣ If button pressed, send ADC value
        if (!(GPIOC->IDR & (1 << 13))) {
            while (!(GPIOC->IDR & (1 << 13)));  // Wait for release
            sprintf(buffer, "Button pressed - ADC: %u\r\n", val);
            send_string(buffer);
        }

        // 3️⃣ Blink LED
        GPIOD->ODR ^= (1 << 12);
        delay(1000);
    }
}
