#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // TODO
    if (number == 2 || number == 3)
        return true;
    if (number <=1 || number % 2 == 0 || number % 3 == 0)
        return false;
    for (int n = 5; n * n <= n; n += 6)
    {
        if (number % n == 0 || n % (n + 2) == 0)
        return false;
    }
    return true;
}
