/*
 -------------------------------------
 File:    a1q2.c
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

float horner(float p[], int n, float x)
{
    // my implementation
    float total = 0;

    for(int i = 0; i < n; i++){
        total = total * x + p[i];  
    }

    return total;
}
 
int main(int argc, char* args[])
{   
    //get polynomial efficients from command line arguments
    if (argc <= 1) {
        printf("Need more than one arguments, e.g.: 1 2 3 4\n");
        return 0;
    }

    // setting len of args
    int n = argc-1;  
    float result = 0;

    // declaring float array data structure for coffeficient 
    float cf[n];

    // read command line arguments convert them to floating numbers atof(args[i+1]);
    for (int i = 0; i < n; i++){
        cf[i] = atof(args[i+1]);
    }

    // repetitive polynomial evaluation for user input of x value
    float x = 0.0;
    do {
        do {
            printf("Please enter x value (Ctrl+C or 999 to quit):\n");
            //get x value from keyboard
            if (scanf("%f", &x) != 1) {
                printf("Invalid input\n");
            } else {            
                break;
            }
            // flush the input buffer 
            while(getchar() !='\n'); 

        } while (1);

        // write your code
        // escape when input 999
        // print the polynomial expression
        // use x^n to denote x raised to the n-th power
        // use %.1f format for floating number
        // get polynomial's value by calling horner(p, n, x)

        if (x == 999){
            break;
        } else {
            result = horner(cf, n, x);

            for (int i = 0; i < n; i++){
                if(i > 0) printf("+ ");
                printf("%0.1f*%0.1f^%d ", cf[i], x, pow(x, (n - (i + 1))));
            }

            printf("= %0.1f\n", result);
        }
    
    } while (1);

    return 0;
}