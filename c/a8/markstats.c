/*
--------------------------------------------------
Project: cp264a8q1
File:    markstats.c 
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-03-13
--------------------------------------------------
*/
#include "markstats.h"

void merge_tree(TNODE **rootp1, TNODE **rootp2) {

  if (rootp2 == NULL) return;

  // insert
  insert(rootp1, &(*rootp2)-> data.name, (*rootp2)-> data.score);

  // left root
  if ((*rootp2)-> left != NULL) merge_tree(rootp1, &(*rootp2) -> left);
  // right root
  if ((*rootp2)-> right != NULL) merge_tree(rootp1, &(*rootp2) -> right);

}

void merge_data(MARKS *ds1, MARKS *ds2) {

	merge_tree(&ds1->bst, &ds2->bst);

  // first set of variables
	int first_count = ds1->count;
	float first_avg = ds1->mean;
	float first_stdv = ds1->stddev;

  // second set of variables
	int second_count = ds1->count;
	float second_avg = ds2->mean;
	float second_stdv = ds2->stddev;


  // first calc
	ds1->count = first_count + second_count;

  // second calc
	ds1->mean = (first_avg * first_count + second_avg * second_count) / ds1->count;
  
  // third calc
	ds1->stddev = sqrt(
			(1.0 / ds1->count)
					* (((first_stdv * first_stdv * first_count) + (first_avg * first_avg * first_count)
          + (second_stdv * second_stdv * second_count)
          + (second_avg * second_avg * second_count))) - (ds1->mean * ds1->mean));

}

void add_data(MARKS *dsp, char *name, float score) {
	if (search(dsp->bst, name) == NULL) {
		insert(&dsp->bst, name, score);
		int count = dsp->count;
		float mean = dsp->mean;
		float stddev = dsp->stddev;
		dsp->count = count + 1;
		dsp->mean = (mean * count + score) / (count + 1);
		dsp->stddev = sqrt(
				score * score / (count + 1.0)
						+ (stddev * stddev + mean * mean)
								* (count / (count + 1.0))
						- dsp->mean * dsp->mean);
	} else {
		printf("record exit");
	}
}

void remove_data(MARKS *dsp, char *name) {
	TNODE *np = NULL;
	if ((np = search(dsp->bst, name)) != NULL) {
		float score = np->data.score;
		delete(&dsp->bst, name);

		int count = dsp->count;
		float mean = dsp->mean;
		float stddev = dsp->stddev;
		dsp->count = count - 1;
		dsp->mean = (mean * count - score) / (count - 1.0);
		dsp->stddev = sqrt(
				(stddev * stddev + mean * mean) * (count / (count - 1.0))
						- score * score / (count - 1.0)
						- dsp->mean * dsp->mean);
	} else {
		printf("record not exit");
	}
}

void display_marks(MARKS *dsp) {
	printf("grade report\n");
	display_inorder(dsp->bst);
	printf("\nstatistics summary\n");
	printf("%-15s%d\n", "count", dsp->count);
	printf("%-15s%3.1f\n", "mean", dsp->mean);
	printf("%-15s%3.1f\n", "stddev", dsp->stddev);
}

void clean_marks(MARKS *dsp) {
	clean_tree(&dsp->bst);
	dsp->count = 0;
	dsp->mean = 0;
	dsp->stddev = 0;
}

void import_data(MARKS *ds, char *filename) {
	char line[40], name[20];
	FILE *fp = fopen(filename, "r");
	char *result = NULL;
	float score = 0;
	char delimiters[] = ",\n";

	if (fp == NULL) {
		perror("Error while opening the file.\n");
		exit(EXIT_FAILURE);
	}

	while (fgets(line, sizeof(line), fp) != NULL) {
		result = strtok(line, delimiters);
		if (result) {
			strcpy(name, result);
			result = strtok(NULL, delimiters);
			score = atof(result);
			add_data(ds, name, score);
		}
	}
	fclose(fp);
}

void print_to_file_inorder(TNODE *root, FILE *fp) {
	if (root) {
		if (root->left)
			print_to_file_inorder(root->left, fp);
		fprintf(fp, "%-15s%3.1f%4c\n", root->data.name, root->data.score,
				letter_grade(root->data.score));
		if (root->right)
			print_to_file_inorder(root->right, fp);
	}
}

void report_data(MARKS *dsp, char *filename) {
	FILE *fp = fopen(filename, "w");
	fprintf(fp, "grade report\n");
	print_to_file_inorder(dsp->bst, fp);
	fprintf(fp, "\nstatistics summary\n");
	fprintf(fp, "%-15s%d\n", "count", dsp->count);
	fprintf(fp, "%-15s%3.1f\n", "mean", dsp->mean);
	fprintf(fp, "%-15s%3.1f\n", "stddev", dsp->stddev);
	fclose(fp);
}

char letter_grade(float s) {
	char r = 'F';
	if (s >= 85)
		r = 'A';
	else if (s >= 70)
		r = 'B';
	else if (s >= 60)
		r = 'C';
	else if (s >= 50)
		r = 'D';
	else
		r = 'F';
	return r;
}
