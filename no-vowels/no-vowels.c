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
}

string replace(string r[], string argv[1]);
{
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i ++)
    {
        if (r[i] == ')
    }
}
