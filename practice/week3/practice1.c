#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    int votes;
} candidate;

candidate candidates[4];

int main(void)
{
    const int n = 4;
    for (int i = 0; i < n; i++)
    {
        candidates[i].name = get_string("Candidate name: ");
    }
}
