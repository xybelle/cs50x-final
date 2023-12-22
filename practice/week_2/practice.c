#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string word = get_string("Word: ");
    int length = strlen(word);
    int array[length];
    for (int i = 0; i < length; i++)
    {
        if (array[i] < array[i +1])
        {
            printf("Yes\n");
        }
        else
        {
            <br>;
            printf("No\n");
        }
    }
}
