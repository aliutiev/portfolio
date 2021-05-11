/*
--------------------------------------------------
Project: cp264-a9q1
File:    common.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef COMMON_H
#define COMMON_H

/* node structure for postfix expression by queue and evaluation by stack */ 
typedef struct node {
	int data; // data can be int operant or a operator 
	int type; // 0: int operant; 1:operator; 3: parenthesis 
	struct node *next;
} NODE;
NODE *new_node(int data, int type);
void display(NODE *start);
void clean(NODE **startp);
#endif
