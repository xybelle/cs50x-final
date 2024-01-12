#include <stdio.h>
#include <math.h>

float min(float *a, float *b);

int main(void)
{
    int height = 10, width = 5;
    int image[height][width];
    for (int i = 0; i < height/2; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            // Swap pixels
            swap(&image[i][j], &image[height][width]);
            image[height - 1][width - 1];
        }
    }
    return;
}



// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float counter = 0;

            // Edge and corner
            if (((i == 0 && j == 0) || ((i == height) && j == 0) || (i == 0 && (j == width)) || ((i == height) && (j == width))))
            {
                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(copy[i][j].rgbtRed / (float) counter);
                image[i][j].rgbtGreen = round(copy[i][j].rgbtGreen / (float) counter);
                image[i][j].rgbtBlue = round(copy[i][j].rgbtBlue / (float) counter);

                break;
            }

            // Middle part
            if (((i > 1) && (i == (height - 1))) || ((j > 1) && (j == (width - 1))))
            {

                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(copy[i][j].rgbtRed / (float) counter);
                image[i][j].rgbtGreen = round(copy[i][j].rgbtGreen / (float) counter);
                image[i][j].rgbtBlue = round(copy[i][j].rgbtBlue / (float) counter);

                break;
            }
        }
    }
    return;
}
