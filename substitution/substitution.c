#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool all_alpha(string key);
bool all_unique(string key);
bool key_count(string key);
char ciphertext(char key[], string plaintext);

int main(int argc, string argv[])
{
    // Check the number of command-line argument
    string key = argv[1];
    if ((argc <= 1) || (argc > 2))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (key_count(key))
    {
        if (all_unique(key))
        {
            // Prompt user for plaintext
            string plaintext = get_string("Plaintext:  ");
            printf("Ciphertext: ");
            int len = strlen(plaintext);
            for (int i = 0; i < len; i++)
            {
                printf("%c", ciphertext(key, plaintext));
            }
            printf("\n");
        }
        else
        {
            printf("Key has duplicates\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}

// Check if key contains 26 characters
bool key_count(string key)
{
    int count = strlen(key);
    if (count != 26)
    {
        printf("Key must contain 26 characters.\n");
    }
    return count && all_alpha(key);
}

// Check if key contains anything but alphabet
bool all_alpha(string key)
{
    int digit = 0;
    for (int i = 0; i < 26; i++)
    {
        if (isdigit(key[i]))
        {
            digit++;
        }
    }
    if (digit >= 1)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    return true;
}

// Check if each key is unique
bool all_unique(string key)
{
    for (int i = 0; i < 26; i++)
    {
        for (int j = i + 1; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                return false;
            }
        }
    }
    return true;
}

// Ciphertext
char ciphertext(char key[], string plaintext)
{
    int plain_length = strlen(plaintext), ci = 0;
    char cipher[plain_length];
    for (int i = 0; i < plain_length; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                ci = plaintext[i] - 65;
                cipher[i] = key[ci];
                return cipher[i];
            }
            else if (islower(plaintext[i]))
            {
                ci = plaintext[i] - 97;
                cipher[i] = key[ci];
                return cipher[i];
            }
        }
        return cipher[i];
    }
    return plaintext;
}
