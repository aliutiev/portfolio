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
#include "bisection.h"
 
int main(int argc, char* args[])
{	
	float p[] = {1, 2, 3, 4};
	int n = 4;
	float a = -2, b = 2;
	
	float pa = horner(p, n, a);
	float pb = horner(p, n, b);
	printf("f(%f): %f\n", a, pa);
	printf("f(%f): %f\n", b, pb);
		
	if (pa * pb < 0) {
	   float r = bisection(p, n, a, b);	
	   printf("root: %f\n", r);
	   printf("f(%f): %f\n", r, horner(p, n, r));
	} else 
    
	return 0;
}
