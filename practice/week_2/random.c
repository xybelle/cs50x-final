#include <cs50.h>
#include <stdio.h>

// I don't know what I want to do here

//float mult_two_numbers(float a, float b);
int add_two_ints(int a, int b);

int main()
{
    // ask user for input
    printf("Give me an integer: ");
    int x = GetInt();
    printf("Give me another integer: ");
    int y = GetInt();

    // add the two numbers together via a function call
    int z = add_two_ints(x, y);

    // output the result
    printf("The sum of %i and %i is %i\n", x, y, z);

}

//float mult_two_numbers(float a, float b)
//{
//    return a * b;
//}

int add_two_ints(int a, int b)
{
    return a + b;
}
