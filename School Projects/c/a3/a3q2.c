/*
--------------------------------------------------
Project: cp264a3q2 
File:    a3q2.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#include "matrix.h"
#include "matrix.c"

int main() {
  int n = 3;
  int m1[n][n];
  int m2[n][n];
  int m3[n][n];
  
  int *p1 = &m1[0][0];
  magic_square(p1, n);
  printf("\nm1:");
  display_matrix(p1, n);
  printf("is_magic_square:%d\n", is_magic_square(p1, n));  
  
  int *p2 = &m2[0][0];  
  printf("\nm1':");
  transpose_matrix(p1, p2, n);
  display_matrix(p2, n);
  printf("is_magic_square:%d\n", is_magic_square(p2, n));  
  
  int *p3 = &m3[0][0];
  multiply_matrix(p1, p2, p3, n);  
  printf("\nm1*m1':");
  display_matrix(p3, n);
  printf("is_magic_square:%d\n", is_magic_square(p3, n));  
  
  return 0;
}
