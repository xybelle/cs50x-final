#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string word = get_string("Word: ");
    string result = tolower(word);
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
