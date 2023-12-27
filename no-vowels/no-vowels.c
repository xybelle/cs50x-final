// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// function to replace vowels with numbers
string replace(string argv[1]);

int main(int argc, string argv[])
{
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./no-vowels (word)\n");
        return 1;
    }
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        if ((argv[1][i] != "a") )
        printf("%c", argv[1][i]);
    }
    printf("\n");
}

