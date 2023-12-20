#include <cs50.h>
#include <stdio.h>

int get_card(void);
int last_number(int n);

int main(void)
{
    // Prompt for input
    int c = get_long("Card number: ");
    

    // Get numbers to calculate checksum
    int ln = last_number(card);

    printf("%i\n", ln);

    // Check card length

    // Check starting digits

    // Check if length and starting digits are valid

    // Print card type and validity

}

int get_card(void)
{

    return c;
}

int last_number(int n)
{
    c = n / 10;
    return n % 10;
}
