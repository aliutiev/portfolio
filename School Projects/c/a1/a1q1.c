/*
 -------------------------------------
 File:    a1q1.c
 Project: cp264a1_liut5320
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

int main(int argc, char *argv[]) {
	setbuf(stdout, NULL); // turns standard output buffering off

	char c, c1 = 0;

	do {
		printf("Please enter a character: \n");
		scanf(" %c", &c);

		if (c >= 48 && c <= 58) {
			printf("%c %d %c\n", c, c, c);

		} else if (c >= 65 && c <= 90) {
			c1 = c + 32;
			printf("%c %d %c\n", c, c, c1);

		} else if (c >= 97 && c <= 122) {
			c1 = c - 32;
			printf("%c %d %c\n", c, c, c1);
		} else {
			printf("Invalid Input \n");
		}

	} while (c != 42);

	printf("Goodbye \n");

	return (0);

}
