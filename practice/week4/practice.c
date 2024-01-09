#include <stdio.h>

int main(void)
{
    int n = 50;
    int *o = &n;
    printf("%d\n", *o);
    printf("%p\n", &o);
}
