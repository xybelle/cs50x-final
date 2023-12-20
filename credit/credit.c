#include <cs50.h>
#include <stdio.h>

long get_card(void);
long last_number(int n);

int main(void)
{
    // Prompt for input
    long card = get_card();

    // Get numbers to calculate checksum
    int ln = last_number(card);
    scanf("%i", &ln);
    printf("%i\n", ln);

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

long last_number(int n)
{
    return n % 10;
}
