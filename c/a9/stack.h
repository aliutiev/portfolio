/*
--------------------------------------------------
Project: cp264-a9q1
File:    stack.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef STACK_H
#define STACK_H

#include "common.h"

typedef struct stack {
  NODE *top;
} STACK;
void push(STACK *sp, NODE *np);
NODE *pop(STACK *sp);
void clean_stack(STACK *sp);

#endif