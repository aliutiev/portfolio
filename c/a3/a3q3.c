/*
--------------------------------------------------
Project: cp264a3q3 
File:    a3q3.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#include "mystring.h"
#include "mystring.c"

int main(int argc, char* args[]) {
  setbuf(stdout, NULL);
  char str[100] = "     This Is    a Test   ";
  printf("\nInput string: \"%s\"", str);
  printf("\nLetter count:%d", letter_count(str));
  printf("\nWord count:%d", word_count(str));
  trim(str);
  printf("\nAfter trimming:\"%s\"", str);
  lower_case(str);  
  printf("\nAfter lower case:\"%s\"", str);
  return 0;
}
