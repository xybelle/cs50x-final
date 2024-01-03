// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);
bool lower(string password);
bool upper(string password);
bool digit(string password);
bool symbol(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password) == 1)
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below

bool valid(string password)
{
    if ((lower(password) == 1) && (upper(password) == 1) && (digit(password) == 1) && (symbol(password) == 1))
    {
        return 1;
    }
    return 0;
}

bool lower(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (islower(password[j]) == 1)
        {
            return 1;
            upper(password);
        }
    }
    return 0;
}

bool upper(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isupper(password[j]) == 1)
        {
            return 1;
            digit(password);
        }
    }
    return 0;
}

bool digit(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isdigit(password[j]) == 1)
        {
            return 1;
            symbol(password);
        }
    }
    return 0;
}

bool symbol(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isprint(password[j]) == 1)
        {
            return 1;
            valid(password);
        }
    }
    return 0;
}


