#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // Make sure program was run with just one commandline argument
    if ((argc <= 1 ) || (argc > 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in arg[1] is a digit
    if (isdigit(argv[1]))
    {
        plaintext(argv[1]);
    }
    // Convert argv[1] from a 'string' to an 'int'
    else if
    {
        conversion(argv[1]);
    }
}

// Prompt User for plaintext
int plaintext(string argv[1], string plain)
{

}


