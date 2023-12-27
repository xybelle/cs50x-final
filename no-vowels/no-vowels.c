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
    char c[];
    for (int i = 0, n = strlen(argv[1]); i < n ; i++)
    {
        argv[1][i] = tolower(argv[1][i]);
        argv[1][i] = c[i];
    }

    for (int i = 0; i < n; i ++)
    {
        if ((c[i] != 'a') || (c[i] !='e') || (c[i] !='i') || c[i] !='o'))
        {
            // return argv[1][i];
            return c[i];
        }
        else
        {
            switch (c[i])
            {
                case 'a':
                    return "6";
                case 'e':
                    return "3";
                case 'i':
                    return "1";
                case 'o':
                    return "0";
            }
        }
    }
    return argv[1];
}
