#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>

#define SHM_SIZE 1024  // Define shared memory size

int main() {
    key_t key = ftok("ipc", 65);  // Generate unique key
    int shmid = shmget(key, SHM_SIZE, 0666 | IPC_CREAT); // Create shared memory

    if (shmid == -1) {
        perror("shmget failed");
        exit(1);
    }

    char *data = (char *)shmat(shmid, NULL, 0); // Attach shared memory
    if (data == (char *)(-1)) {
        perror("shmat failed");
        exit(1);
    }

    printf("Enter message to write in shared memory: ");
    fgets(data, SHM_SIZE, stdin); // Store user input in shared memory

    printf("Data written: %s\n", data);

    shmdt(data); // Detach shared memory
    return 0;
}
