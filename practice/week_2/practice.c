#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(void)
{
    string word = get_string("Word: ");

    for (int a = 0; a < str[a]; a++)
    {
        str[a] = tolower(str[a]);
    }
    int length = strlen(result);
    int array[length];

    for (int i = 0; i < length; i++)
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
