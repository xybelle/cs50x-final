#include <cs50.h>
#include <stdio.h>

bool checksum(long card);
int findlenght(long card);
bool cardlength(long card);

int main(void)
{
    // Prompt for input
    long card;
    do
    {
        card = get_long("Number: ");
    }
    while (card <= 0)

    if (cardlength(card))
    {
        checksum(card);
    }
    else
    {
        printf("Invalid\n");
    }
}

bool cardlength(long card);
{
    int len = findlength(card);
    return ((len == 13 || len == 15 || len == 16) && checksum(card))
}

int findlength(long card)
{
    long le, count = 0;
    le = card;
}

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
        if (40 <= firsttwo && firsttwo <= 49)
        {
            if (count == 13)
            {
                printf("VISA\n");
            }
            else if (count == 16)
            {
                printf("VISA\n");
            }
        }
        else if (firsttwo == 34 || firsttwo == 37)
        {
            if (count == 15)
            {
                printf("AMEX\n");
            }
        }
        else if (51 <= firsttwo && firsttwo <= 55)
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
    else
    {
        printf("Invalid\n");
    }
}

bool checksum(long card)
{
    int sum = 0;
    long temp = card;

    while (temp > 0)
    {
        int last = temp % 10;
        sum = sum + last;
        temp = temp / 100;
    }

    while (temp > 0)
    {
        int seclast = (temp % 10);
        int multemp = seclast * 2;
        sum = sum + (multemp % 10) + (multemp / 10);
        temp = temp / 100;
    }
    return (sum % 10) == 0;
}

