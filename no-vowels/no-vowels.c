// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// function to replace vowels with numbers
string replace(string r[], string argv[1]);

int main(int argc, string argv[])
{
    if ((argc > 2) && (argc < 1))
    {
        printf("Error: please type ./no-vowels (word)\n");
        return 1;
    }
    else
    {
        string r;
        printf(replace(r));
    }
    printf("\n");
}

string replace(string r[], string argv[1]);
{
    int n = strlen(argv[1]);
    r = tolower(r);
    for (int i = 0; i < n; i ++)
    {
        if (r[i] == 'a')
        {
            r[i] = '6';
        }
        else if (r[i] == 'e')
        {
            r[i] = '3';
        }
        else if (r[i] == 'i')
        {
            r[i] = '1';
        }
        else if (r[1] == 'o')
        {
            r[i] = '0'
        }
        else
        {
            return r[i];
        }
    }
}
