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
    while (n < 9);

    // TODO: Prompt for end size
    int t;
    do
    {
        t = get_int("Ending population size: ");
    }
    while (t <= n);

    // TODO: Calculate number of years until we reach threshold
    // b = n / 3 , d = n / 4
    // j = n + b - d
    // y++
    int b = n / 3;
    int d = n / 4;
    int j = n + b - d;
    int y = 0;
    while (j < t)
    {
        j = j + b -d;
        y++;
    }

    // TODO: Print number of years
    printf("It will take %i years.\n", y);
}
