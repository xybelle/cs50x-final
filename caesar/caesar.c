#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

    // Check if argv[1] is a digit
    if (only_digits(argv))
    {
        printf("True\n");
        return 0;
    }
    else

    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert argv[1] to int
    int key(string argv[1]);
    char plaintext[] = get_string("Plaintext:  ");
    int i = strlen(plaintext);
    printf("Ciphertext:  ");
    for (int j = 0; j < i; j++)
    {
        rotate(plaintext[j]);
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

char rotate (char c, int key)
