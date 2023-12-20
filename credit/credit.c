#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cc;
    do
    {
        cc = get_long("Card number: ");
    }
    while (cc < 9999999999999999)
}
