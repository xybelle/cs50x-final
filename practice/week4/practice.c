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
