#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index

    // Print the grade level
    printf("%i\n", letters);

}

int count_letters(string text)
{
    // Return the number of letters in text
    // isalpha()
    int cl = 0;
    for (int i = 0, j = strlen(text); i < j; i++)
    {
        if (isalpha(text[i]))
        {
            cl++;
        }
    }
    return cl;
}

int count_words(string text)
{
    // Return the number of words in text
    int cw = 0;
    for (int i = 0, j = strlen(text); i < j; i++)
    {
        if (isalpha(text[i]))
        {
            
        }
    }
    return cw;
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    return false;
}
