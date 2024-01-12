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
            float counter = 0.0, red = 0.0, green = 0.0, blue = 0.0;
            // Corners
            if (((i == 0 && j == 0) || ((i == height - 1) && j == 0) || (i == 0 && (j == width - 1))
                || ((i == height - 1) && (j == width - 1))))
            {
                for (int x = 0; x < 2; x++)
                {
                    for (int y = 0; y < 2; y++)
                    {
                        red += copy[i + x][j + y].rgbtRed;
                        green += copy[i + x][j + y].rgbtGreen;
                        blue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(red / (float) counter);
                image[i][j].rgbtGreen = round(green / (float) counter);
                image[i][j].rgbtBlue = round(blue / (float) counter);
            }

            // Left and right edges
            if ( (j == 0 && ((i >= 1) && (i < height - 2))) || (j == width - 1 && ((i >= 1) && (i < height - 2))))
            {
                for (int x = -1; x < 2; x++)
                {
                    for (int y = 0; y <= 1; y++)
                    {
                        red += copy[i + x][j + y].rgbtRed;
                        green += copy[i + x][j + y].rgbtGreen;
                        blue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(red / (float) counter);
                image[i][j].rgbtGreen = round(green / (float) counter);
                image[i][j].rgbtBlue = round(blue / (float) counter);
            }

            // Upper and lower edges
            if ((i == 0 && ((j >= 1) && (j < width - 2))) || (i == height - 1 && ((j >= 1) && (j < width - 2))))
            {
                for (int x = 0; x <= 1; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        red += copy[i + x][j + y].rgbtRed;
                        green += copy[i + x][j + y].rgbtGreen;
                        blue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(red / (float) counter);
                image[i][j].rgbtGreen = round(green / (float) counter);
                image[i][j].rgbtBlue = round(blue / (float) counter);
            }

            // Middle part
            if ((i >= 1 && i <= (height - 2)) || (j >= 1 && j <= (width - 2)))
            {

                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        red += copy[i + x][j + y].rgbtRed;
                        green += copy[i + x][j + y].rgbtGreen;
                        blue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = round(red / (float) counter);
                image[i][j].rgbtGreen = round(green / (float) counter);
                image[i][j].rgbtBlue = round(blue / (float) counter);
            }
        }
    }
    return;
}
