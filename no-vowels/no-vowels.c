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
        if (argv[1][i] = a)
        {
            replce
        }
        printf("%c", argv[1][i]);
    }
    printf("\n");
}

string replace(string argv[1])
{
    int n = strlen(argv);
    for (int i = 0; i < n; i ++)
    {
        if ((argv[1][i] = 'a') || (argv[1][i] ='e') || (argv[1][i] ='i') || (argv[1][i] ='o'))
        {
            switch (argv[1][i])
            {
                case 'a':
                    argv[1][i] = "6";
                case 'e':
                    argv[1][i] = "3";
                case 'i':
                    argv[1][i] = "1";
                case 'o':
                    argv[1][i] = "0";
            }
        }
        else
        {
            return argv[1][i];
        }
    }
    // return argv[1];
}

