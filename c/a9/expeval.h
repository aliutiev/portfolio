/*
--------------------------------------------------
Project: cp264-a9q1
File:    expeval.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef EXPEVAL_H
#define EXPEVAL_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "common.h"
#include "queue.h"
#include "stack.h"
#include "hash.h"

/* 
 * convert infix expression string to postfix expression represented by queue, 
 * and get symbol value from hash table
*/
QUEUE infix_to_postfix(char *infixstr, HASHTABLE *ht);

/* 
 * evaluate postfix expression represented by queue
*/
int evaluate_postfix(QUEUE queue);

/*
 * get the priority of operator opr
*/ 
int get_priority(char opr);

/*
 * evaluate symbolic infix expression, 
 * calling infix_to_postfix(char *infixstr, HASHTABLE *ht); then 
 * calling evaluate_postfix(QUEUE queue);
*/ 
int evaluate_infix(char *infixstr, HASHTABLE *ht);

/*
 * parsing statement symbol=expression, to get left-side symbol string, and 
 * evaluate the right side expression using evaluate_infix(char *infixstr, HASHTABLE *ht);
 * insert the symbol and its value into hashtable
*/ 
int resolve_assignment(char* statement, HASHTABLE *ht);

#endif