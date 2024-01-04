#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

bool only_digits(string argv[1]);

int main(int argc, string argv[])
{
    // Check number of command-line argument
    if ((argc <= 1 ) || (argc > 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == '1')
    {
        return 0;
    }

    int k = string

    printf("%i\n", only_digits(argv));

}

bool only_digits(string argv[1])
{
    int i = strlen(argv);
    if (isdigit(argv[1]))
    {
        return true;
    }
    else
    {
        return false;
    }
}

