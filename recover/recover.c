#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Check if single command-line is entered
    if (!argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Cannot open %s\n", argv[1]);
        return 2;
    }

    uint8_t buffer[BLOCK_SIZE];
    int count = 0;

    // Read from memory card while there are still data left
    while (fread(buffer, sizeof(buffer), BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
                FILE *img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Cannot create");
                    return 3;
                }

                sprintf(img, "%03i.jpg", count);
                fwrite(buffer, sizeof(buffer), BLOCK_SIZE, img);
                count++;
                fclose(img);
        }
    }

    fclose(card);
}
