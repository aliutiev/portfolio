/*
--------------------------------------------------
Project: cp264a3q1 
File:    a3q1.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#include <time.h> 
#include "sort.h"

int main(int argc, char *args[])
{
  int a[] = {3, 1, 4, 5, 2, 7, 6, 9, 8}; // input array for correctness testing
  int n = sizeof(a)/sizeof(int);         // array length
  int b[n], i;                           // array to sort
  
  printf("Algorithm correctness testing:\n");  
  printf("Input array:");  
  display_array(a, n);
  printf("Is sorted:%d\n", is_sorted(a, n));  
  
  printf("Selection sort:");
  copy_array(a, b, n);
  selection_sort(b, 0, n-1);
  display_array(b, n);
  printf("Is sorted:%d\n", is_sorted(b, n));  

  printf("Quick sort:");
  copy_array(a, b, n);
  quick_sort(b, 0, n-1); 
  display_array(b, n);
  printf("Is sorted:%d\n", is_sorted(b, n));  
  

  printf("Algorithm runtime testing:\n");  
  //run time measurement
  clock_t t1, t2;    
  int len = 2000;
  int a1[len];
  int b1[len];
  //generate randomly an array of len elements more modular len
  srand(time(NULL)); 
  for (i=0;i<len;i++) {
    a1[i] = rand()% len;
  }

  //run time measuring for selection_sort
  int m1 = 10;
  t1=clock();
  for (i=0; i< m1; i++) {
    copy_array(a1, b1, len);
    selection_sort(b1, 0, len-1); 
    if (!is_sorted(b1, len)) printf("not sorted:%d\n");  
  }
  t2=clock();
  double time_span1 = (double) t2-t1;
  printf("time_span(selection_sort(%d numbers) for %d times): %0.1f (ms)\n", len, m1, time_span1);
  
  //run time measuring for quick_sort
  int m2 = 1000;
  t1=clock();
  for (i=0; i< m2; i++) {
    copy_array(a1, b1, len);
    quick_sort(b1, 0, len-1); 
    if (!is_sorted(b1, len)) printf("not sorted:%d\n");  
  }
  t2=clock();
  double time_span2 = (double) t2-t1;
  printf("time_span(quick_sort(%d numbers) for %d times): %0.1f (ms)\n", len, m2, time_span2);
  
  printf("time_span(selection_sort(%d numbers))/time_span(quick_sort(%d numbers)): %0.1f\n", len, len,
  (time_span1/time_span2)*(m2/m1));

  return 0;
}
