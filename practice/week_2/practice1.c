#include <cs50.h>
#include <stdio.h>

const int N = 3;

float average(int array[]);

int main(void)
{
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Scores: ");
    }

    printf("The average score is: %f\n", average(scores));
}

float average(int array[])
{
    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum = sum + array[i];
    }
    return sum / (float) N;
}


string replace(string argv[1])
{
    int n = strlen(argv[1]), i = 0;
    char c[n];
    string word = c[n]
    for (i < n ; i++)
    {
        argv[1][i] = tolower(argv[1][i]);
        argv[1][i] = c[i];
    }

    for (i < n; i ++)
    {
        if ((c[i] != 'a') || (c[i] !='e') || (c[i] !='i') || (c[i] !='o'))
        {
            // return argv[1][i];
            return c[i];
        }
        else
        {
            switch (c[i])
            {
                case 'a':
                    return "6";
                case 'e':
                    return "3";
                case 'i':
                    return "1";
                case 'o':
                    return "0";
            }
        }
    }
    return argv[1];
}
