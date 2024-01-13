#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK = 512;

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
    FILE *card = fopen(argv[1], "r");
    FILE *jpeg = fopen( , "w");

    // Check if .raw - if not inform user and return 1
    if (card == NULL)
    {
        printf("Cannot open %c\n", argv[1]);
        return 1;
    }

    uint8_t buffer[BLOCK];

    // Read from memory card while there are still data left
    while (fread(buffer, 1, BLOCK, card) == BLOCK)
    {
        fwrite(buffer, 1, BLOCK, jpeg);
    }


    // Files generated should be named 000.jp for the first and counting up
    // Program if uses malloc must not leak memory

}
