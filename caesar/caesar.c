#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc <= 1 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
    }
    else if (isdigit(argv[1]))
    {
        plaintext();
    }
    else
    {
        printf("Usage: ./caesar key\n");
    }
}


