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
    long first, second;
    scanf("%ld", &card);

    first = card;

    while (first >= 10)
    {
        first = first / 10;
    }
    printf("first digit = %li", first);



    // Check if length and starting digits are valid

    // Print card type and validity
}


