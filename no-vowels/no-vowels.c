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
    int n = strlen(argv[1]);
    for (int i = 0; i < n ; i++)
    {
        argv[1][i] = tolower(argv[1][i]);
    }
    char c[]:
    c[0] = argv[1][0];

    for (int i = 0; i < n; i ++)
    {
        if ((argv[1][i] != 'a') || (argv[1][i] !='e') || (argv[1][i] !='i') || (argv[1][i] !='o'))
        {
            // return argv[1][i];
            argv[1][i + 1];
        }
        else
        {
            switch (argv[1][i])
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
