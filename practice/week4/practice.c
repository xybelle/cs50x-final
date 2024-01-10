#include <stdio.h>

int min(int *a, int *b);

int main(void)
{
    int rgbtRed, rgbtGreen, rgbtBlue;
    float sepiaRed = 254.6, sepiaGreen = 265.9, sepiaBlue = 165, max = 255;

    rgbtRed = round(min(&sepiaRed, &max));
    rgbtGreen = round(min(&sepiaGreen, &max));
    rgbtBlue = round(min(&sepiaBlue, &max));

    printf("%i %i %i\n", rgbtRed, rgbtGreen, rgbtBlue);
}

float min(int *a, int *b)
{
    return (*a < *b) ? *a : *b;
}
