#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card = get_long("Card number: ");

    // Check card length
    int n;
    int count = 0;
    scanf("%i", &n);
    while (n != 0)
    {
        n = n / 10;
        count++;
    }
    if (count < 13)
    {
        printf("Invalid\n");
    }

    // Get numbers to calculate checksum

    // Check starting digits
    int first

    // Check if length and starting digits are valid

    // Print card type and validity
}


