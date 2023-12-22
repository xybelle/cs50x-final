#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(void)
{
    string word = get_string("Word: ");

    for (int a = 0; a < strlen[word]; a++)
    {
        tolower(str[a]);
    }
    int array[length];

    for (int i = 0; i < strlen(word); i++)
    {
        if (array[i] > array[i + 1])
        {
            array[i] = array[i + 1];
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
            break;
        }

    }
}
