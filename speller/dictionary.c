// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26 * 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Obtain hash value
    int x = hash(word);

    // Access linked list
    node *tmp = table[x];

    // Traverse linked list
    while (tmp->next != NULL)
    {
        if (strcasecmp(word, tmp->word) != 0)
        {
            tmp = tmp->next;
        }
        else
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (strlen(word) < 3)
    {
        return 0;
    }

    int a = toupper(word[0] - 'A');
    int b = toupper(word[1] - 'A');
    int c = toupper(word[2] - 'A');
    int x = (a * 26 * 26) + (b * 26) + c;

    // Ensure the result is within the range of the hash table size
    return x % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dicttionary
    FILE *src = fopen(dictionary, "r");
    if (src == NULL)
    {
        return false;
    }

    // Read each word in the file
    char words[LENGTH];
    while (fscanf(src, "%s", words) == 1)
    {
        // Create space for new hash table node
        node *new_node = (malloc(sizeof(node)));
        if (new_node == NULL)
        {
            return false;
        }
        new_node->next = NULL;

        // Copy the word into the new node
        strcpy(new_node->word, words);

        // Hash the word to obtain its hash value
        int x = hash(words);

        // Insert the new node into the hash table (using the index specified by its hash value)
        new_node->next = table[x];
        table[x] = new_node;
    }

    // Close dictionary
    fclose(src);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int counter = 0;

    for (int i = 0; i < N; i++)
    {
        node *tmp = table[i];

        while (tmp != NULL)
        {
            counter++;
            tmp = tmp->next;
        }
    }
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *tmp1 = table[i];
        node *tmp2;

        while (tmp1 != NULL)
        {
            tmp2 = tmp1;
            tmp1 = tmp1->next;
            free(tmp2);
        }

        table[i] = NULL;
    }
    return true;
}
