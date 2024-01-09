#include <stdio.h>

int main(void)
{
    int n = 50;
    int *o = &n;
    printf("%p\n", o);
    printf("%p\n", &o);
}
