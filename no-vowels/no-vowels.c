// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// function to replace vowels with numbers
string replace(string nv);

int main(int argc, string argv[])
{
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./no-vowels (word)\n");
        return 1;
    }

    string nv = argv[1];
    printf("%s\n", replace(nv));
}

string replace(string nv)
{
    int i = 0;
    int h = strlen(nv);
    for (int j = 0; j < h; j++)
    {
        if(nv[i] == 'a')
        {
            nv[i] = '6';
        }

    }
    return nv;
}
