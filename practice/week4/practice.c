#include <stdio.h>

int main(void)
{
    int rgbtRed, rgbtGreen, rgbtBlue;
    int sepiaRed = 255, sepiaGreen = 265, sepiaBlue = 165;
    if (sepiaRed <= 255  sepiaGreen <= 255 || sepiaBlue <= 255 )
            {
                rgbtRed = min(sepiaRed, 255);
                rgbtGreen = sepiaGreen;
                rgbtBlue = sepiaBlue;
            }
            else
            {
                rgbtRed = 255;
                rgbtGreen = 255;
                rgbtBlue = 255;
            }

    printf("%i %i %i\n", rgbtRed, rgbtGreen, rgbtBlue);
}
