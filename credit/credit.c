#include <cs50.h>
#include <stdio.h>



int main(void)
{
    // Prompt for input
    long card;
    printf("Card number: ");

    // Get numbers to calculate checksum

    // Check starting digits
    long firsttwo;
    scanf("%li", &card);

    firsttwo = card;

    while (firsttwo >= 100)
    {
        firsttwo = firsttwo / 10;
    }
    printf("first digit = %li\n", firsttwo);

    // Check length
    long le, count = 0;

    le = card;
    do
    {
        le /= 10;
        count++;
    }
    while (le != 0);

    printf("Number of digits: %li\n", count);

    // Print card type and validity
    if (13 < firsttwo && firsttwo < 40)
    {
        if (count == 15);
        {
            printf("VISA\n");
        }
    }
    else if (34 < firsttwo && firsttwo < 37)
    {
        printf("AMEX\n");
    }
    else if (firsttwo == 34 && count == 15)
    {
        printf("AMEX\n");
    }
    else if (51 < firsttwo && firsttwo < 55)
    {
        if (count == 16)
        {
            printf("MasterCard\n");
        }
    }

    else
    {
        printf("Invalid\n");
    }
}


