#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argv[1]);
char rotate (char c, int k);

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

    // Check if argv[1] is a digit
    if (only_digits(argv))
    {
        // Convert argv[1] to int
        int k(string argv[1]);
        int i = strlen(argv);
        string plaintext = get_string("Plaintext:  ");
        for (int j = 0; j < i; j++)
        {
            char plaintext[j] = rotate (plaintext[j], k);
        }

        printf("Ciphertext: %c%c%c ", plaintext[0], plaintext[1], plaintext[2]);

    }
    else

    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool only_digits(string argv[1])
{
    int i = strlen(argv[1]);
    for (int j = 0; j < i; j++)
    {
        if (isdigit(argv[1][j]))
        {
            return true;
        }
    }
    return false;
}

char rotate (char c, int k)
{
    if (isupper(c))
    {
        c = (int) c - k;
    }
    else if (islower(word[j]))
    {
        c = (int) c - k;
    }

    return c;
}
