#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card = get_long("Card number: ");

    // Check card length
    int n;
    int count = 0;
    scanf("%d", &n);
    while (n != 0)
    {
        n = n / 10;
        count++;
    }
    if (count < 13)
    {
        printf("Invalid\n");
    }

    long a, b, c, d, e, f, g, h, i, j, k, l, m, o, p;

    // Get individual numbers
    p = card % 10;
    o = (card / 10) % 10;

    printf("%li \t %li\n", p , o);

    // Get numbers to calculate checksum

    // Check starting digits

    // Check if length and starting digits are valid

    // Print card type and validity
}


