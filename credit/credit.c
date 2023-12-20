#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cc;
    do
    {
        cc = get_long("Card number: ");
    }
    while (cc > 5699999999999999);

    switch(cc)
    {
        case (cc == 4000000000000000 || cc == 4999999999999999):
            printf("Visa\n");
            break;

        case (cc > 5600000000000000):
            printf("Invalid\n");
            break;
    }
}
