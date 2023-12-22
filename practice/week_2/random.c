#include <cs50.h>
#include <stdio.h>

// I don't know what I want to do here
int GetIntA(int a);
int GetIntB(int b);
//float mult_two_numbers(float a, float b);
int add_two_ints(int a, int b);

int main()
{
    int x = GetIntA();
    int y = GetIntB();

    // add the two numbers together via a function call
    int z = add_two_ints(x, y);

    // output the result
    printf("The sum of %i and %i is %i\n", x, y, z);

}

int GetIntA(int a)
{
    int a = get_int("Give me an integer: ");
    return a;
}
int GetIntB(int b)
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
