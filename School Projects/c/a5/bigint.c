/*
--------------------------------------------------
Project: cp264a5q3
File:    a5q3.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#include "bigint_dllist.h"
#include "bigint.h"

BIGINT bigint(char *p) {
  BIGINT bn = {0};
  if (p == NULL) 
    return bn;
  else if (!(*p >= '0' && *p <= '9')) {// not begin with digits 
    return bn;
  }
  else if (*p == '0' && *(p+1) == '\0') {// just "0"
    insert_end(&bn.start, &bn.end, new_node(*p -'0'));
    return bn;
  }  
  else { 
    while (*p) {
      if (*p >= '0' && *p <= '9' ){
        insert_end(&bn.start, &bn.end, new_node(*p -'0'));
      } else {
        clean_bigint(&bn);   
        break;
      }
      p++;
    }
    return bn;
  }
}

void display_bigint(BIGINT bignumber) {
  NODE *ptr = bignumber.start;
  while ( ptr != NULL) {
    printf("%d", ptr->data);
    ptr = ptr->next;
  }
}

void clean_bigint(BIGINT *bignumberp) {
  clean(&bignumberp->start, &bignumberp->end);
}

BIGINT add(BIGINT op1, BIGINT op2) {
    BIGINT sum = {0};
	int the_carry_over = 0;
	int the_digit_current = 0;
	NODE *first_pointer = op1.end;
	NODE *second_pointer  = op2.end;

	while (first_pointer != NULL && second_pointer != NULL){
		the_digit_current = first_pointer -> data + second_pointer -> data + the_carry_over;
		the_carry_over = 0;

		if (the_digit_current > 9){
			the_carry_over = 1;
			the_digit_current -= 10;
		}

		insert_start(&sum.start, &sum.end, new_node(the_digit_current));
		first_pointer = first_pointer -> prev;
		second_pointer  = second_pointer -> prev;

	}

	while (first_pointer != NULL){

		the_digit_current = first_pointer -> data + the_carry_over;
		the_carry_over = 0;

		insert_start(&sum.start, &sum.end, new_node(the_digit_current));

		if (the_digit_current > 9){
			the_carry_over = 1;
			the_digit_current -= 10;
		}

		first_pointer = first_pointer-> prev;
	}

	while (second_pointer  != NULL){

		the_digit_current = second_pointer -> data + the_carry_over;
		the_carry_over = 0;

		insert_start(&sum.start, &sum.end, new_node(the_digit_current));
		
		if (the_digit_current > 9){
			the_carry_over = 1;
			the_digit_current -= 10;
		}
		second_pointer  = second_pointer -> prev;
	}

	if (the_carry_over == 1){
		insert_start(&sum.start, &sum.end, new_node(1));
	}
	return sum;
}

BIGINT Fibonacci(int n) {
	BIGINT first = {0};
	BIGINT second = {0, new_node(1)};
	BIGINT third;
	BIGINT the_flag = {0};

	if (n <= 0){

		the_flag = first;

	} else {

		for (int i = 1; i < n; i++) {

			third = add(first, second);
			first = second;
			second = third;

		}
		the_flag = third;
  }
}