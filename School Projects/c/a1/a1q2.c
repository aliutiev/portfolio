/*
 -------------------------------------
 File:    a1q2.c
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
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
	setbuf(stdout, NULL); // turns standard output buffering off

	int count = atoi(argv[1]);


	int counter = 0, total = 1;

	if (count <= 0) {
		printf("Integer must be greater than 0 \n");
	} else {
		for (int i = 1; i <= count; i++) {
			total = total * i;
			if (total > 999999999) {
				printf("\noverflow at %d!", (i));
				break;
			} else {

				// adds new line
				if (counter == 3) {
					printf(" \n");
					counter = 0;
				}
				//prints out formula
				printf("%10d", total);
				counter++;

				// reset once counter is at max
				if (i == (count)) {
					printf(" \n");
					total = 1;
					counter = 0;
				}

			}
		}

	}
	return (0);


}
