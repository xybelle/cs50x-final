#include <cs50.h>
#include <stdio.h>

long get_card(void);

int main(void)
{
    // Prompt for input
    long card = get_card();

    // Calculate checksum

    // Check card length

    // Check starting digits

    // Check if length and starting digits are valid

    // Print card type and validity
    
}

long get_card(void)
{
    long c = get_long("Card number: ");
    return c;
}

int get_number(int n)
{
    n = n % 10;
    return n * 2;
}
