#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK_SIZE = 512;

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
    FILE *card = fopen(argv[1], "rb");
    if (card == NULL)
    {
        printf("Cannot open %s\n", argv[1]);
        return 2;
    }

    FILE *img = fopen(filename, "wb");
    if (img == NULL)
    {
        printf("Cannot create");
        return 3;
    }

    uint8_t buffer[BLOCK_SIZE];

    // Read from memory card while there are still data left
    while (fread(buffer, sizeof(buffer), BLOCK_SIZE, card) == BLOCK)
    {
        if ()
        fwrite(buffer, sizeof(buffer), BLOCK_SIZE, jpeg);

        int count = 0;
        sprintf(filename, "%03i.jpg", count);
        count++;
    }


    // Files generated should be named 000.jp for the first and counting up
    // Program if uses malloc must not leak memory

    fclose(card);
}
