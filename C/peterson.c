#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_ITERATIONS 5

int flag[2] = {1, 1}; // Flags for both processes
int turn = 0;         // Shared variable to indicate turn

void *process0(void *arg) {
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        flag[0] = 1; // Process 0 wants to enter
        turn = 1;    // Give turn to Process 1

        // Wait until Process 1 finishes
        while (flag[1] && turn == 1);

        // Critical Section
        printf("Process 0 is in the critical section\n");
        usleep(500000); // Simulate work (0.5 seconds)

        // Exit section
        flag[0] = 0; // Release control
    }
    return NULL;
}

void *process1(void *arg) {
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        flag[1] = 1; // Process 1 wants to enter
        turn = 0;    // Give turn to Process 0

        // Wait until Process 0 finishes
        while (flag[0] && turn == 0);

        // Critical Section
        printf("Process 1 is in the critical section\n");
        usleep(500000); // Simulate work (0.5 seconds)

        // Exit section
        flag[1] = 0; // Release control
    }
    return NULL;
}

int main() {
    pthread_t t0, t1;

    pthread_create(&t0, NULL, process0, NULL);
    pthread_create(&t1, NULL, process1, NULL);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    return 0;
}
