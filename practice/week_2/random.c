#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int z[]);

int main(void)
{
    int x[3], i;
    for (i = 0; i < 3; i ++)
    {
        x[i] = get_int("Give me a positive number: ");
    }

    int y = valid_triangle(x);

    if (y == 1)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }
}

bool valid_triangle(int z[])
{
    if (z[0] <= 0 || z[1] <= 0 || z[2] <= 0)
    {
        return false;
    }

    if ((z[0] + z[1] <= z[2]) || (z[0] + z[2] <= z[1]) || (z[2] + z[1] <= z[0]))
    {
        return false;
    }
    return true;
}

