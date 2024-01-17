#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if single command-line is entered
    if (argc != 2)
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

    const int BLOCK_SIZE = 512;
    uint8_t buffer[BLOCK_SIZE];
    int counter = 0;
    char *filename = malloc(8 * sizeof(char));
    if (filename == NULL)
    {
        return 4;
    }

    FILE *img = fopen(filename, "w");
    if (img == NULL)
    {
        fclose(card);
        fclose(img);
        printf("Cannot create");
        return 5;
    }
    bool firstjpg = false;
    bool newjpg = true;

    // Read from memory card while there are still data left
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!firstjpg)
            {
                firstjpg = true;
                newjpg = false;

                sprintf(filename, "%03i.jpg", counter);
                counter++;

                img = fopen(filename, "w");
                if (img == NULL)
                {
                    fclose(card);
                    fclose(img);
                    return 6;
                }

                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
            else if (firstjpg && newjpg)
            {
                fclose(img);
                firstjpg = false;
                newjpg = true;
            }
        }
        else
        {
            if (counter >= 1)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
    }

    fclose(card);
    fclose(img);
    free(filename);
    return 0;
}
