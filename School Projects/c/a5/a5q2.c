/*
--------------------------------------------------
Project: cp264a5q2
File:    a5q2.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/ 

#include "bigint_dllist.h"

int main(int argc, char* args[]) {
  NODE *start = NULL, *end = NULL;
  int i=0;
  for (i = 0; i<10; i++) {
    insert_start(&start, &end, new_node('0'+i));
  }
  display_forward(start);
  printf("\n");
  display_backward(end);
  delete_start(&start, &end);
  delete_end(&start, &end);
  printf("\n");
  display_forward(start);
  clean(&start, &end); 
  
  for (i = 0; i<10; i++) {
    insert_end(&start, &end, new_node('a'+i));
  }
  printf("\n");
  display_forward(start);
  clean(&start, &end); 
  return 0;
}