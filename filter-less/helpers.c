#include "helpers.h"
#include <math.h>

float min(float *a, float *b);
void swap(int *a, int *b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through all pixels
    int avergb;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get average of r, g, b
            avergb = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;

            // Update pixel values
            image[i][j].rgbtRed = round(avergb);
            image[i][j].rgbtGreen = round(avergb);
            image[i][j].rgbtBlue = round(avergb);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaGreen, sepiaBlue;
    int max = 255;
    // Loop through all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get sepia values
            sepiaRed = (.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen)
                 + (.189 * image[i][j].rgbtBlue);
            sepiaGreen = (.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen)
                 + (.168 * image[i][j].rgbtBlue);
            sepiaBlue = (.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen)
                 + (.131 * image[i][j].rgbtBlue);

            // Update pixel values
            image[i][j].rgbtRed = round(min(&sepiaRed, &max));
            image[i][j].rgbtGreen = round(min(&sepiaGreen, &max));
            image[i][j].rgbtBlue = round(min(&sepiaBlue, &max));
        }
    }
    return;
}

// Return which is lower
float min(float *a, float *b)
{
    return (*a < *b) ? *a : *b;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through all pixels
    for (int i = 0; i < height/2; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            // Swap pixels
            swap(&image[i][j], &image[height][width])
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

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
