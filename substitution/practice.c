#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string key = get_string("Key: ");
    char u[26];

    for (int i = 0; i < 26; i++)
    {
        u[i] = key[0][i];
    }

}
