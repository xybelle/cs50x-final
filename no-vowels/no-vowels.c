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
        printf("%s", replace(argv));
    }
    printf("\n");
}

string replace(string argv[1])
{
    int n = strlen(argv[1]);
    string string;
    for (int i = 0; i < n; i++)
    {
        char c[n] = argv[1][i];
    }

    for (int i = 0; i < n; i++)
    {
        if ((c[i] = 'a') || (c[i] ='e') || (c[i] ='i') || (c[i] ='o'))
        {
            switch (argv[1][i])
            {
                case 'a':
                    c[i] = 6;
                case 'e':
                    c[i] = 3;
                case 'i':
                    c[i] = 1;
                case 'o':
                    c[i] = 0;
            }
        }
        else
        {
            return string = c[i];
        }
    }
    return string;
}
