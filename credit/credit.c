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
    long count = 0;
    scanf("%ld", &card);
    do
    {
        card /= 10;
        count++;
    }
    while (card != 0);

    printf("Number of digits: %li\n", count);


    // Print card type and validity
    if (firsttwo >= 4)
    {
        printf("VISA\n");
    }
}


