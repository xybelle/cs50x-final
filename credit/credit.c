#include <cs50.h>
#include <stdio.h>

int last_number(int ln);

int main(void)
{
    // Prompt for input
    int card = get_long("Card number: ");

    // Get numbers to calculate checksum
    int ln = last_number(card);
    printf("%i\n", ln);

    // Check card length

    // Check starting digits

    // Check if length and starting digits are valid

    // Print card type and validity
}

int last_number(int ln)
{
    ln = ln % 10;
    return ln;
}

