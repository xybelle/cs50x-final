#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card;
    printf("Card number: ");

    // Check card length

    // Get numbers to calculate checksum

    // Check starting digits
    long firsttwo;
    scanf("%ld", &card);

    firsttwo = card;

    while (firsttwo >= 100)
    {
        firsttwo = firsttwo / 10;
    }
    printf("first digit = %li\n", firsttwo);

    // Check if length and starting digits are valid
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
    if (firsttwo >= 40 && le >= 13)
    {
        printf("VISA\n");
    }
    else
    {
        printf("Invalid\n");
    }
}


