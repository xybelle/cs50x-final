#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Check the number of command-line argument
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check if key contains 26 characters
    int count = strlen(argv[1]);
    if (count != 26)
    {
        printf("Key must contain 26 characters.\n");
    }

    // Check if key contains anything but alphabet
    do
    {
        if (isalnum(argv[1]))
        {

        }
    }

    // Check if each key is unique

    // Prompt user for plaintext

    // Print ciphertext
}



