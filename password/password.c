// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
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
    if (lower(password) && upper(password) && digit(password) && symbol(password))
    {
        return true;
    }
    return false;
}

bool lower(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (islower(password[j]))
        {
            return true;
        }
    }
    return false;
}

bool upper(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isupper(password[j]))
        {
            return true;
        }
    }
    return false;
}

bool digit(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isdigit(password[j]))
        {
            return true;
        }
    }
    return false;
}

bool symbol(string password)
{
    int i = strlen(password);
    for (int j = 0; j < 1; j++)
    {
        if (isprint(password[j]))
        {
            return true;
        }
    }
    return false;
}
