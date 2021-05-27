/*
--------------------------------------------------
Project: cp264-a9q1
File:    stack.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

void push(STACK *sp, NODE *np) {
  if (sp == NULL || np == NULL) return; 	
  if (sp->top == NULL) {
    sp->top = np;
    sp->top->next = NULL;
  }
  else {
    np->next = sp->top;
    sp->top = np;
  }
}

NODE *pop(STACK *sp) {
  if (sp == NULL || sp->top == NULL) return NULL;
  
  NODE *tmp = sp->top;
  sp->top = tmp->next;
  tmp->next = NULL;
  return tmp;
}

void clean_stack(STACK *sp) {
  clean(&(sp->top));
  sp->top = NULL;
}

