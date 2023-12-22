#include <cs50.h>
#include <stdio.h>

// I don't know what I want to do here
int get_int_a(void);
int get_int_b(void);
//float mult_two_numbers(float a, float b);
int add_two_ints(int a, int b);

int main()
{
    int x = get_int_a();
    int y = get_int_b();

    // add the two numbers together via a function call
    int z = add_two_ints(x, y);

    // output the result
    printf("The sum of %i and %i is %i.\n", x, y, z);

}

int get_int_a(void)
{
    int a = get_int("Give me an integer: ");
    return a;
}
int get_int_b(void)
{
    int b = get_int("Give me another integer: ");
    return b;
}

//float mult_two_numbers(float a, float b)
//{
//    return a * b;
//}

int add_two_ints(int a, int b)
{
    return a + b;
}
