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




// Swap pixels
    for (int i = 0; i < height; i++)
    {
        w = width;
        for (int j = 0; j < width; j++)
        {
            image[i][j] = tmp[i][w];
            w--;
        }
    }

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    int h = height, w = width;
  //  RGBTRIPLE tmp[h][w];
    RGBTRIPLE *tmp[h][w];
    tmp[h][w] = malloc(h * w * sizeof(RGBTRIPLE));
    if ( tmp[h][w] == NULL)
    {
        return;
    }
    // Loop through all pixels
    for (int i = 0; i <= height; i++)
    {
        for (int j = 0; j <= width; j++)
        {
            // Copy to temporary
            *tmp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i <= height; i++)
    {
        for (int j = 0, n = width/2; j < n; j++)
        {
            image[i][j] = image[h][w];
            image[h][w] = *tmp[i][j];
            h--;
            w--;
        }
    }
    free(tmp[h][w]);
    return;
}

for (int i = 0; i < height; i++)
    {
        for (int j = 0, n = width/2; j < n, j++)
        {
            image[i][j] = image[h][w];
            w--;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0, n = width/2; j < n; j++)
        {
            image[h][w] = tmp[i][j];
        }
    }

for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // mid mid
            int counter = 0;
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
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;
            }
            // corners (4x)
            else if ((i == 0 && j == 0) || ((i == height) && j == 0) || (i == 0 && (j == width)) ||
                ((i == height) && (j == width)))
            {
                for (int x = 0; x < 2; x++)
                {
                    for (int y = 0; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;
            }
            // sides (6x)
            else if (((i == 0) && (j >= 1)) || ((i == height) && (j >= 1)))
            {
                // upper-lower side (6)
                for (int x = -1; x < 1; x++)
                {
                    for (int y = -1; y < 2; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;
            }
            else if (((i >= 1) && (j == 0)) || ((i >= 1) && (j == width)))
            {
                // right-left sides (6)
                for (int x = -1; x < 2; x++)
                {
                    for (int y = -1; y < 1; y++)
                    {
                        copy[i][j].rgbtRed += copy[i + x][j + y].rgbtRed;
                        copy[i][j].rgbtGreen += copy[i + x][j + y].rgbtGreen;
                        copy[i][j].rgbtBlue += copy[i + x][j + y].rgbtBlue;
                        counter++;
                    }
                }
                image[i][j].rgbtRed = copy[i][j].rgbtRed / counter;
                image[i][j].rgbtGreen = copy[i][j].rgbtGreen / counter;
                image[i][j].rgbtBlue = copy[i][j].rgbtBlue / counter;
            }
        }
    }
