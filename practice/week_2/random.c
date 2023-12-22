#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int z);
int sumoftwosides(int x);

int main(void)
{
    int x[3], i;
    for (i = 0; i < 3; i ++)
    {
        x[i] = get_int("Give me a positive number: ");
    }

    int y = valid_triangle(x[i]);
    if (y == 0)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }
}

bool valid_triangle(int z)
{
    int sumoftwosides(int x);
    return 0;
}

int sumoftwosides(int x)
{
    if (x[0] < (x[1] + x[2]))
    {
        return 0;
    }
}

