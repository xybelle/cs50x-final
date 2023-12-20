#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for input
    long card;
    printf("Card number: ");

    // Get numbers to calculate checksum

    scanf("%li", &card);
    long le, count = 0;

    le = card;
    do
    {
        le /= 10;
        count++;
    }
    while (le != 0);

    if (le == 16)
    {
        int a, b, c, d, 
    }
}
