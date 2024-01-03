#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    // Prompt user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);

    // Compute the Coleman-Liau index

    // Print the grade level
    printf("\n");

}

int count_letters(string text)
{
    // Return the number of letters in text
    // isalpha()
}

int count_words(string text)
{
    // Return the number of words in text
}
