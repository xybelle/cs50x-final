#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int x[]);

int main(void)
{
    int x[3], i;
    for (i = 0; i < 3; i ++)
    {
        x[i] = get_int("Give me a positive number: ");
    }

    int y = valid_triangle(x[]);

    printf("%i\n", y);
}

bool valid_triangle(int x)
{
    if (x[0] <= 0 || x[1] <= 0 || x[2] <= 0)
    {
        return false;
    }

    if ((x[0] + x[1] <= x[2]) || (x[0] + x[2] <= x[1]) || (x[2] + x[1] <= x[0]))
    {
        return false;
    }
    return true;
}

