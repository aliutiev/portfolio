/*
 -------------------------------------
 File:    a1q3.c
 Project: cp264a1_liut5320
 file description
 -------------------------------------
 Author:  Andrew Liutiev
 ID:      180635320
 Email:   liut5320@mylaurier.ca
 Version  2020-01-17
 -------------------------------------
 */

#include <stdio.h>
#include <math.h>  // need this library for maths functions fabs() and sqrt()

int main(int argc, char *argv[]) {
	float a, b, c, disc, x1, x2;
	int inn;
	char temp;

// do-while for repeated input
	do {
		// do-while loop to get correct input of three floating number coefficient
		do {
			printf("Please enter the coefficients a,b,c:\n");
			inn = scanf("%f,%f,%f", &a, &b, &c);

			if (inn != 3) {
				printf("Invalid input\n");
			} else
				break;
			do {  // flush the input buffer
				scanf("%c", &temp);
				if (temp == '\n')
					break;
			} while (1);

		} while (1);

		if (fabs(a) < 1e-6 && fabs(b) < 1e-6 && fabs(c) < 1e-6) {
			printf("Goodbye\n");
			break;
		} else if (fabs(a) < 1e-6) {
			printf("not a quadratic equation\n");

		} else {

			 double disc = b*b - 4*a*c;

          if (disc < 0) {


              printf("%f+%fi\n", -b/(float)(2*a), sqrt(-disc)/(2*a));


              printf("%f-%fi\n", -b/(float)(2*a), sqrt(-disc)/(2*a));
          }
          else { //real roots

              x1 = (-b + sqrt(disc))/(2*a);


              x2 = (-b - sqrt(disc))/(2*a);



              if (x1 == x2) {

                  printf("The equation has two equal real roots:  \n%f\n", x1);

              } else {

                  printf("The equation has two distinct real roots: \n %f\n %f\n", x1, x2);


              }
          }
		}

	} while (1);


	return 0;
}
