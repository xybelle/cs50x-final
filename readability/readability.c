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
    double L = ((float) letters / (float) words) * 100;
    double S = ((float) sentences / (float) words) * 100;
    double index = 0.0588 * (float) L - 0.296 * (float) S - 15.8;

    // Print the grade level
    if ((double) round(index) >= 16)
    {
        printf("Grade 16+\n");
    }
    else if ((double) round(index) < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %f\n", (double) round(index));
    }

    printf("%i %i %i %f\n", letters, words, sentences, (double) round(index));

}

int count_letters(string text)
{
    // Return the number of letters in text
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
        if (isblank(text[i]))
        {
            cw++;
        }
    }
    return (cw + 1);
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int cs = 0;
    for (int i = 0, j = strlen(text); i < j; i++)
    {
        if (ispunct(text[i]))
        {
            cs++;
        }
    }
    return cs;
}
