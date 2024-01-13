#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if 2 argv
        // else print usage "Usage: ./recover image", then return 1

    if (!argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open memory card
    FILE *file = fopen(argv[2], "r");

    // Check if .raw - if not inform user and return 1
    if (file == NULL)
    {
        printf("Cannot open %c\n", argv[2]);
        return 1;
    }

    

    // Files generated should be named 000.jp for the first and counting up
    // Program if uses malloc must not leak memory

}
