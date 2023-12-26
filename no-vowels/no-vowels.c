// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// function to replace vowels with numbers
string replace(string r[]);

int main(int argc, string argv[])
{
    if ((argc <= 1) || (argc > 2))
    {
        printf("Error: please type ./no-vowels (word)\n");
        return 1;
    }
    else
    {
        string r = argv[1];
        printf("%s\n", replace(r[]));
    }
}

string replace(string r[])
{
    int n = strlen(r);
    r[] = tolower(r[])
    for (int i = 0; i < n; i ++)
    {
        switch (r[i])
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
