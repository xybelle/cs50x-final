#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card;
    printf("Card number: ");

    // Get numbers to calculate checksum

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
    if (firsttwo >= 40 && count >= 13)
    {
        printf("VISA\n");
    }
    else
    {
        printf("Invalid\n");
    }

    if (firsttwo <= 37 && count == 15)
    {
        printf("AMEX\n");
    }

    if (firsttwo == 51, 52, 53, 54, 55 && count == 16)
}


