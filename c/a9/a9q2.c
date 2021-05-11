/*
--------------------------------------------------
Project: cp264-a9q1
File:    a9q2.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include "expeval.h"   
#include "hash.h"

int htsize = 10;

int main(int argc, char* args[]) {
  char infilename[40] = "expression.txt";0;
  if (argc >1) strcpy(infilename, args[1]);
  
  if (argc >2) htsize = atoi(args[2]);

  HASHTABLE *ht = new_hashtable(htsize);

  char line[100];
  char delimiters[] = ";\n";
  char *st;
  
  FILE *fp = fopen(infilename, "r");
  if (fp == NULL) {
    perror("Error while opening the file.\n");
    return 0;
  }
  
  printf("Symbolic expressions:\n"); 
  while (fgets(line, sizeof(line), fp) != NULL) {
    st = strtok(line, delimiters);
	printf("%s\n", st);
    while (st != NULL) {
      resolve_assignment(st, ht);
      st = strtok(NULL, delimiters);
    }
  }
  fclose(fp);
  
 
  printf("\nSymbolic expression evaluation:\n");  
  display_hashtable(ht, 1);
  
  clean_hash(&ht);
  
  return 0;
}

/*
gcc common.c queue.c stack.c hash.c expeval.c a9q2.c -o a9q2
a9q2 expression.txt

Symbolic expressions:
a=5
b=3
c=(a+b)*(a-b)
b=a+b+c

Symbolic expression evaluation:
a=5
b=24
c=16
*/
 
 
 