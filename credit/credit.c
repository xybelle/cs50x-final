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

    if (firsttwo >= 4)
    {
        printf("VISA\n");
    }

    // Check if length and starting digits are valid

    // Print card type and validity
}


