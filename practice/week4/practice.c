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
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = *a;
}




void swap(RGBTRIPLE *a, RGBTRIPLE *b, int h, int w);

           swap(&image[i][j], &image[h][w], h, w);
// Swap pixels
void swap(RGBTRIPLE *a[h][w], RGBTRIPLE *b[h][w], int h, int w)
{
    RGBTRIPLE tmp[h][w];
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            tmp[i][j] = *a[h][w];
        }
    }

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            *a[i][j] = *b[h][w];
        }
    }

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            *b[i][j] = tmp[h][w];
        }
    }
}

