#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // Make sure program was run with just one commandline argument
    if ((argc < 1 ) || (argc > 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == 1)
    {
        return 0;
    }

}

