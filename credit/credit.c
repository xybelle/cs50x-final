#include <cs50.h>
#include <stdio.h>

long calculate_last(long card);

int main(void)
{
    // Prompt for input
    long card;
    printf("Card number: ");

    // Get numbers to calculate checksum
    long lastnum = calculate_last(card);

    // Check starting digits
    long firsttwo;
    scanf("%li", &card);

    firsttwo = card;

    while (firsttwo >= 100)
    {
        firsttwo = firsttwo / 10;
    }
    printf("first digit = %li\n", firsttwo);

    // Check length
    long le, count = 0;

    le = card;
    do
    {
        le /= 10;
        count++;
    }
    while (le != 0);

    printf("Number of digits: %li\n", count);

    // Print card type and validity
    if (40 <= firsttwo && firsttwo <= 49)
    {
        if (count == 13)
        {
            printf("VISA\n");
        }
        else if (count == 16)
        {
            printf("VISA\n");
        }
    }
    else if (firsttwo == 34 || firsttwo == 37)
    {
        if (count == 15)
        {
            printf("AMEX\n");
        }
    }
    else if (51 <= firsttwo && firsttwo <= 55)
    {
        if (count == 16)
        {
            printf("MasterCard\n");
        }
    }
    else
    {
        printf("Invalid\n");
    }
}
