#include <stdio.h>

int main(void)
{
    int sepiaRed = 255, sepiaGreen = 265, sepiaBlue = 165;
    if (sepiaRed <= 255 || sepiaGreen <= 255 || sepiaBlue <= 255 )
            {
                image[i][j].rgbtRed = sepiaRed;
                image[i][j].rgbtGreen = sepiaGreen;
                image[i][j].rgbtBlue = sepiaBlue;
            }
            else
            {
                image[i][j].rgbtRed = 255;
                image[i][j].rgbtGreen = 255;
                image[i][j].rgbtBlue = 255;
            }
}
