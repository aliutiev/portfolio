/*
 -------------------------------------
 File:    a1q1.c
 Project: cp264a2_liut5320
 file description
 -------------------------------------
 Author:  Andrew Liutiev
 ID:      180635320
 Email:   liut5320@mylaurier.ca
 Version  2020-01-15
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int *low_address;
int *high_address;

int iterative_fibonacci(int n)
{
    int priorPreviousNumber, previousNumber = 0, currentNumber = 1;

    // update the lowest memory address reached.
    if (&n < low_address) low_address = &n;

    // my implementation
    for (int i = 1; i < n; i++){
        priorPreviousNumber = previousNumber;
        previousNumber = currentNumber;
        currentNumber = priorPreviousNumber + previousNumber;
    }
    return currentNumber; 
}

int recursive_fibonacci(int n) {

    // update the lowest memory address reached. 
    if (&n < low_address) low_address = &n;  
    
    // your implementation
    if (n == 0){
        return 0;
    } else if (n == 1){
        return 1;
    } else {
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2);
    }
}

int main(){
    int i = 0, n = 40;
    clock_t t1, t2; 

    int m1 = 500000, m2 = 10;
    double time_span1, time_span2;
    
    printf("Iterative algorithm measurement:\n");
    
    //measuring memory span for iterative_fibonacci function
    high_address = &i;
    low_address = high_address;
    
    printf("iterative_fibonacci(%d): %d\n", n, iterative_fibonacci(n));
    printf("high address: %lu\n", high_address);
    printf("low address: %lu\n", low_address);
    int memory_span1 = (unsigned long) high_address - (unsigned long) low_address;
    printf("memory span: %d\n", memory_span1);

    //measuring runtime for iterative_fibonacci function
    t1 = clock();
    for (i = 0; i < m1; i++) {
        iterative_fibonacci(n);
    }
    t2=clock();
    time_span1 = (double) t2-t1;

    printf("time_span(iterative_fibonacci(%d) for %d times): %0.1f (ms)\n", n, m1, time_span1);
    printf("\nRecursive algorithm measurement:\n");
    
    // add your memory span and time span measuring for the recursive_fibonacci function

    high_address = &i;
    low_address = high_address;

    printf("recursive_fibonacci(%d): %d\n", n, recursive_fibonacci(n));
    printf("high address: %lu\n", high_address);
    printf("low address: %lu\n", low_address);
    int memory_span2 = (unsigned long) high_address - (unsigned long) low_address;
    printf("memory span: %d\n", memory_span2);

    t1 = clock();
    for (i = 0; i < m2; i++) {
        recursive_fibonacci(n);
    }
    t2=clock();

    time_span2 = (double) t2-t1;
    printf("time_span(recursive_fibonacci(%d) for %d times): %0.1f (ms)\n", n, m2, time_span2);

    // comparison
    printf("\nComparison of recursive and iterative algorithms:\n");
    printf("memory_span(recursive_fibonacci(%d))/memory_span(iterative_fibonacci(%d)): %0.1f\n", n, n, ((double) memory_span2)/memory_span1);
    printf("time_span(recursive_fibonacci(%d))/time_span(iterative_fibonacci(%d)): %0.1f\n", n, n, (time_span2/time_span1)*(m1/m2));
    
    return 0;
}
