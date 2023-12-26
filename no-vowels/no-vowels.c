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
        printf("Error: please type ./no-vowels (word)\n");
        return 1;
    }

    printf("%s\n", replace(argv));
}

string replace(string argv[1])
{
    int n = strlen(r);
    for (int i = 0; i < n ; i++)
    {
        argv[1][i] = tolower(argv[1][i]);
    }

    for (int i = 0; i < n; i ++)
    {
        switch (argv[1][i])
        {
            case 'a':
                return '6';
            case 'e':
                return '3';
            case 'i':
                return '1';
            case 'o':
                return '0';
            default:
                return r[i];
        }
    }
}
