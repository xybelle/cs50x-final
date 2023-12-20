#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card = get_long("Card number: ");

    // Check card length
    int count = 0;
    scanf("%ld", &card);
    while (card != 0)
    {
        card = card / 10;
        count++;
    }
    if (count < 13)
    {
        printf("Invalid\n");
    }

    // Get numbers to calculate checksum

    // Check starting digits

    // Check if length and starting digits are valid

    // Print card type and validity
}


