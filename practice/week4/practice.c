#include <stdio.h>

int min(int *a, int *b);

int main(void)
{
    int rgbtRed, rgbtGreen, rgbtBlue;
    int sepiaRed = 255, sepiaGreen = 265, sepiaBlue = 165, max = 255;

    rgbtRed = min(&sepiaRed, &max);
    rgbtGreen = min(&sepiaGreen, &max);
    rgbtBlue = min(&sepiaBlue, &max);

    printf("%i %i %i\n", rgbtRed, rgbtGreen, rgbtBlue);
}

int min(int *a, int *b)
{
    return (*a < *b) ? *a : *b;
}
