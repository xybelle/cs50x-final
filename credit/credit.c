#include <cs50.h>
#include <stdio.h>

bool checksum(long card);
int findlenght(long card);
bool cardlength(long card);

int main(void)
{
    // Prompt for input
    long card;
    do
    {
        card = get_long("Number: ");
    }
    while (card <= 0)

    if (cardlength(card))
    {
        checksum(card);
    }
    else
    {
        printf("Invalid\n");
    }
}

bool cardlength(long card);
{
    int length = findlenght(card);
    return ((length == 13 || length == 15 || length == 16) && checksum(card))
}

int findlength(long card)
{
    int count = 0;
    while (card != 0)
    {
        card = card / 10;
        count++;
    }
    return count
}

bool checksum(long card)
{
    int sum = 0;
    long temp = card;

    while (temp > 0)
    {
        int last = temp % 10;
        sum = sum + last;
        temp = temp / 100;
    }

    while (temp > 0)
    {
        int seclast = (temp % 10);
        int multemp = seclast * 2;
        sum = sum + (multemp % 10) + (multemp / 10);
        temp = temp / 100;
    }
    return (sum % 10) == 0;
}
