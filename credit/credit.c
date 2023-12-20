#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cc = 0;
    do
    {
        cc = get_long("Card number: ");
    }
    while (cc > 5699999999999999);

    if (cc >= 4000000000000000 && cc <= 4999999999999999)
    {
        printf("Visa\n");
    }
    else if (cc >= 3400000000000000 && cc <= 3799999999999999)
    {
        printf("AMEX\n");
    }
    else if (cc >= 5100000000000000 && cc <= 5599999999999999)
    {
        printf("Mastercard\n");
    }
    else;
    {
        printf("Invalid\n");
    }
}
