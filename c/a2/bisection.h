/*
 -------------------------------------
 File:    a1q3.c
 Project: cp264a2_liut5320
 file description
 -------------------------------------
 Author:  Andrew Liutiev
 ID:      180635320
 Email:   liut5320@mylaurier.ca
 Version  2020-01-15
 -------------------------------------
 */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define TOL 1e-7

float horner(float *p, int n, float x);
float bisection(float *p, int n, float a, float b);

// horny formula
float horner(float *p, int n, float x)
{
  // my implementation
   float total = 0;

   for (int i = 0 ; i < n; i++){
    total = total * x + (*p + i);
   }
   return total;
}

// bisection formula
float bisection(float *p, int n, float a, float b)
{
  // my implementation
  float c = a;

  while ((b - a) >= TOL) {
    c = (a + b) / 2;
    
    if (horner(p, n, c) == 1e-6) {
      break; 
    } else if (horner(p, n, c) * horner(p, n, a) < 0.0) {
      b = c; 
    } else {
      a = c;
    }
  }
  return c;

}