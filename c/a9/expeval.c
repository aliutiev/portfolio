/*
--------------------------------------------------
Project: cp264-a9q1
File:    expeval.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expeval.h"


/*
 * axillary function 
*/
int get_priority(char op) {
  if (op == '/' || op == '*' || op == '%') 
    return 1;
  else if (op == '+' || op == '-')
    return 0;
  else 
    return -1;    
}


/*
 * axillary function 
*/
int type(char c) {
  if (c >= '0' &&  c <= '9' )
     return 0;
  else if (c == '/' || c == '*' || c == '%' || c == '+' || c == '-')
    return 1;
  else if (c == '(')
    return 2;
  else if ( c == ')')
    return 3;  
  else 
    return 4;
}


QUEUE infix_to_postfix(char *infixstr, HASHTABLE *ht) {
  QUEUE queue = {0};
  STACK stack = {0};  
  char *p = infixstr;
  int sign = 1;
  int num = 0;
  char symbol[20] = {};

  while (*p) {
    if ( *p == '-' && (p == infixstr || *(p-1) == '(')  ) {
      sign = -1;
    }  
    else if (*p >= '0' && *p <= '9'){
      num = *p-'0';
      while ((*(p+1) >= '0' && *(p+1) <= '9')) {
         num = num*10 + *(p+1)-'0';
         p++;
      }
      enqueue(&queue, new_node(sign*num, 0));
      sign = 1;  
    }
    else if (*p == '(') {
      push(&stack, new_node('(', 2));
    }
    else if (*p == ')') {
      while (stack.top){
        if (stack.top->type == 2) {
          free(pop(&stack));
          break;
        }
        enqueue(&queue, pop(&stack));  
      }
    } else if (type(*p) == 1) {
      while (stack.top && stack.top->type==1 && get_priority( stack.top->data) >= get_priority(*p))
        enqueue(&queue, pop(&stack));  
      push(&stack, new_node(*p, 1));
    }
    else if ( (*p >= 'a' && *p <= 'z') || (*p >=  'A' && *p <= 'Z') ) {
      
      // add your code to handle the case when symbolic name is encounted. 
      // 1. get the symbolic name string 
      char the_new_name[2];
			the_new_name[0] = *p;
			the_new_name[1] = '\0';

      // 2. search hash table to find the value of the symbolic name
			HTNODE *np = search(ht, the_new_name);

      // 3. enqueue the value
			enqueue(&queue, new_node(np->value, 0));
      
    }
    p++;
  }
  
  while (stack.top) {    
    enqueue(&queue, pop(&stack));  
  }
  
  return queue;
}


int evaluate_postfix(QUEUE queue) {
  STACK stack = {0};

  int type = 0;
  NODE *p = queue.front;
  
  while (p) {
    type = p->type;
    
    if (type == 0) {    // operant
      push(&stack, new_node(p->data, 0));
    }    
    else if (type==1){  // operator
      int operator = p->data;
      NODE *oprand2 = pop(&stack);

      if (operator == '+')
        stack.top->data = stack.top->data + oprand2->data;
      else if (operator == '-')
        stack.top->data = stack.top->data - oprand2->data;
      else if (operator == '*')
        stack.top->data = stack.top->data * oprand2->data;
      else if (operator == '/')
        stack.top->data = stack.top->data / oprand2->data;
          
      free(oprand2);
    }
    p = p->next;
  }

  int result = stack.top->data;
  clean_stack(&stack);  
  return result;
}


/*
 * evaluate symbolic infix expression, 
 * calling infix_to_postfix(char *infixstr, HASHTABLE *ht); then 
 * calling evaluate_postfix(QUEUE *qp);
*/ 

int evaluate_infix(char *infixstr, HASHTABLE *ht) {

  // setting the new queue
  QUEUE the_new_queue = infix_to_postfix(infixstr, ht);

  // return
	return evaluate_postfix(the_new_queue);
}


int resolve_assignment(char* statement, HASHTABLE *ht) {
  char name[10] = { 0 };
  char *dest = strstr(statement, "=");
  if (dest) 
    *dest = '\0';
  else 
    dest = statement;
  strcpy(name, statement);
  if ( (name[0] >= 'a' && name[0] <= 'z') || (name[0] >= 'A' && name[0] <= 'Z')) {
      
    int value = evaluate_infix(dest + 1, ht);

    if (value == 99999)  // escape value
      return 2;
    else {
      insert(ht, new_hashnode(name, value));
    }
    return 1;
  }
  return 0;
}
