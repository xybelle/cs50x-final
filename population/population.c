#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
    do
    {
        n = get_int("Starting population size: ");
    }
    while (n <= 9);

    // TODO: Prompt for end size
    int t;
    do
    {
        t = get_int("Ending population size: ");
    }
    while (t <= n);

    // TODO: Calculate number of years until we reach threshold
    // b = n / 3 , d = n / 4
    // y = n + b - d
 

    for (int y = 0; y  y++)
    {
        // TODO: Print number of years
        printf(It will take %i\n.", y);
    }
}
