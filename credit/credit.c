#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card = get_long("Card number: ");

    // Check card length

    // Get numbers to calculate checksum

    // Check starting digits
    int first;
    scanf("%ld", &card);

    first = card;

    while (first >= 10)
    {
        first = first / 10;
    }
    printf("first digit = %d", first);

    // Check if length and starting digits are valid

    // Print card type and validity
}


