/*
--------------------------------------------------
Project: cp264-a9q1
File:    common.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include <stdio.h>
#include <malloc.h>
#include "common.h"

NODE *new_node(int data, int type) {
  NODE *np = (NODE *) malloc(sizeof(NODE));
  np->data = data;
  np->type = type;
  np->next = NULL;
  return np;
}

void display(NODE *start) {
  while (start) {
    if (start->type == 0) 
      printf("%d ", start->data);
    else 
      printf("%c ", start->data);      
    
    start = start->next;
  }
}

void clean(NODE **topp) {
  NODE *curr = *topp;
  while (curr) {
    NODE *tmp = curr;
    curr = curr->next;
    free(tmp);
  }
  *topp = NULL;
}
