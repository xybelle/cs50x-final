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
        if ((argv[1][i] = 'a') || (argv[1][i] ='e') || (argv[1][i] ='i') || (argv[1][i] ='o'))
        {
            argv[1][i] = replace(argv[1]);
            printf("%c", argv[1][i]);
        }
        else
        {
            printf("%c", argv[1][i]);
        }
    }
    printf("\n");
}

string replace(string argv[1])
{
    int n = strlen(argv[1]);
    string c;
    for (int i = 0; i < n; i++)
    {
        c[i] = argv[1][i];
    }

    switch (c[i])
    {
        case 'a':
            argv[1][i] = 6;
            break;
        case 'e':
            argv[1][i] = 3;
            break;
        case 'i':
            argv[1][i] = 1;
            break;
        case 'o':
            argv[1][i] = 0;
            break;
    }
    return c;
}
