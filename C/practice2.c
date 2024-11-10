#include <stdio.h>
#include <stdlib.h>
#include <string.h> // For strcpy

int main() {
    int numNames = 3; // Number of names
    char **names = malloc(numNames * sizeof(char*)); // Allocate memory for the array of string pointers

    // Check if memory allocation was successful
    if (names == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Allocate memory for each name and initialize them
    names[0] = malloc(20 * sizeof(char)); // Allocate memory for the first name
    strcpy(names[0], "Alice"); // Initialize the first name

    names[1] = malloc(20 * sizeof(char)); // Allocate memory for the second name
    strcpy(names[1], "Bob"); // Initialize the second name

    names[2] = malloc(20 * sizeof(char)); // Allocate memory for the third name
    strcpy(names[2], "Charlie"); // Initialize the third name

    // Print the names
    for (int i = 0; i < numNames; i++) {
        printf("%s\n", *(names+i)); // Print each name
    }
    printf("%c",**names);
    // Free the allocated memory for each name
    for (int i = 0; i < numNames; i++) {
        free(names[i]);
    }
    // Free the array of pointers

    free(names);

    return 0;
}
