#include <stdio.h>

void min(int *a, int *b);

int main(void)
{
    int rgbtRed, rgbtGreen, rgbtBlue;
    int sepiaRed = 255, sepiaGreen = 265, sepiaBlue = 165, max = 255;
    if (sepiaRed <= 255  sepiaGreen <= 255 || sepiaBlue <= 255 )
            {
                rgbtRed = min(sepiaRed, max);
                rgbtGreen = min(sepiaGreen, max);
                rgbtBlue = min(sepiaBlue, max);
            }
            else
            {
                rgbtRed = 255;
                rgbtGreen = 255;
                rgbtBlue = 255;
            }

    printf("%i %i %i\n", rgbtRed, rgbtGreen, rgbtBlue);
}

void min(int *a, int *b)
{
    return (*a < *b) ? *a : *b;
}
