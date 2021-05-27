#include "mystring.h"

int letter_count(char *s)
{
   
    char *pointer = s;
    int count = 0;

    // check empty
    if (s == NULL) return -1;

    while (*pointer)
    {
        if (*pointer != ' ')
        {
            count++;
        }
        pointer++;
    }
    return count;
}

void lower_case(char *s)
{
    char *pointer = s;

    // check empty
    if (s == NULL) return;
    while (*pointer)
    {
        if ((*pointer >= 'A') && (*pointer <= 'Z'))
            *pointer += 32;
        pointer++;
    }
}

int word_count(char *s)
{
    char *pointer = s;
    int count = 0;

    if (s == NULL || *s == '\0') return 0;
    
    while (*pointer)
    {
        if (*pointer != ' ' && (pointer == s || *(pointer - 1) == ' '))
        {
            count++;
        }
        pointer++;
    }
    return count;
}

void trim(char *s)
{
    char *pointer = s, *pointer2 = s;

    while (*pointer)
    {
        if (*pointer != ' ' || (pointer > s && *(pointer - 1) != ' '))
        {
            *pointer2 = *pointer;
            pointer2++;
        }
        pointer++;
    }
    if (*(pointer - 1) == ' ')
    {
        *(pointer2 - 1) = '\0';
    }
    else
        *pointer2 = '\0';

    printf("\n%s", s);
}