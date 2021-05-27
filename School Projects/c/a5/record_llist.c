/*
--------------------------------------------------
Project: cp264a5q1 
File:    a5q1.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#include "record_llist.h"

void display(NODE *start) {

    while (start != NULL){

        printf("%-12s %-12.2f   \n", start -> data.name, start -> data.score );
        start = start -> next;

    }
}

NODE* search(NODE *startp, char *name) {

    NODE *temp_pointer = startp;

    while(temp_pointer != NULL) {

        if(strcmp(temp_pointer -> data.name, name ) == 0) {

            return temp_pointer;

        } 

        temp_pointer = temp_pointer->next;

    }

    return NULL;
}

void insert(NODE **startp, char *name, float score) {

    NODE *temp_pointer = (NODE *) malloc (sizeof(NODE));

    strcpy(temp_pointer -> data.name, name);
    temp_pointer -> data.score = score;
    temp_pointer -> next = NULL;

    NODE *temp_previous = NULL;
    NODE *temp_pointer_dup = *startp;

    while(temp_pointer_dup != NULL) {
        if (strcmp(temp_pointer_dup-> data.name, name) >= 0) {
            break;
        }
        temp_previous = temp_pointer_dup;
        temp_pointer_dup = temp_pointer_dup-> next;
    }

    if (temp_previous == NULL) {
        *startp = temp_pointer ;
        temp_pointer -> next = temp_pointer_dup;
    } else {
        temp_previous-> next = temp_pointer ;
        temp_pointer -> next = temp_pointer_dup;
    }
}

int delete(NODE **startp, char *name) {
    NODE *temp_pointer = *startp;
    NODE *temp_previous = NULL;

    // the node head
    if (temp_pointer  != NULL && strcmp(temp_pointer ->data.name, name) == 0) {

        *startp = temp_pointer ->next;
        free(temp_pointer );

        return 0;
    }

    // the search for the node
    while (temp_pointer  != NULL && strcmp(temp_pointer -> data.name, name) != 0) {
        temp_previous = temp_pointer ;
        temp_pointer  = temp_pointer -> next;
    }

    // nothing found exit
    if (temp_pointer  == NULL) {
        return 0;
    }

    // linke change
    temp_previous->next = temp_pointer -> next;
    free(temp_pointer );

    return 1;
}

void clean(NODE **startp) {

    NODE *temp_pointer;
    NODE *null_pointer = *startp;

    while (null_pointer != NULL) { 

        temp_pointer = null_pointer; 
        null_pointer = null_pointer -> next;
        free(temp_pointer);
        
    }

    *startp = NULL;
}

// the following functions are adapted and modified from previous assignments. You make use of them. 

void report_data(NODE *start, char *filename) {
  NODE *np = start;
  int count = 0;
  float mean = 0;
  float stddev = 0;
  int histogram[6] = {0};
  FILE *fp = fopen(filename, "w");

  fprintf(fp, "grade report\n");  
  while (np != NULL) {
    count++;
    mean += np->data.score;
    stddev += np->data.score * np->data.score ;
      //histogram data
    if (np->data.score >=100)  histogram[0]++;
    else if (np->data.score < 50)  histogram[5]++;
    else histogram[(unsigned int) (99.99-np->data.score)/10]++;
    
    fprintf(fp, "%-15s%3.1f%4c\n", np->data.name, np->data.score, letter_grade(np->data.score));
    np = np->next;
  }
  mean /= count;
  stddev = sqrt(stddev/count - mean*mean);
  
  fprintf(fp, "\nstatistics summary\n");
  fprintf(fp, "%-15s%d\n", "count", count);
  fprintf(fp, "%-15s%3.1f\n", "mean", mean);
  fprintf(fp, "%-15s%3.1f\n", "stddev", stddev);
  fprintf(fp, "%-15s%3.1f\n", "median", median(start));
  
  fprintf(fp, "histogram\n");
  int i;
  fprintf(fp, "%-15s%d\n", "[90,100]", histogram[0]);
  for (i=1; i<5; i++) {
     fprintf(fp, "[%d,%d)        %d\n", 90-i*10, 100-i*10, histogram[i]);
  }
  fprintf(fp, "%-15s%d\n", "[0,50)", histogram[5]);
  
  fclose(fp);
}

void import_data(NODE **startp, char *filename) {
  char line[40], name[20];
  FILE *fp = fopen(filename, "r");
  char *result = NULL;
  char delimiters[] = ",";
  float score = 0;

  if (fp == NULL) {
    perror("Error while opening the file.\n");
    exit(EXIT_FAILURE);
  }

  while (fgets(line, sizeof(line), fp) != NULL) {
    result = strtok(line, delimiters);
    strcpy(name, result);
    result = strtok(NULL, delimiters);
    score = atof(result);
    insert(startp, name, score);
  }
  fclose(fp);
}

char letter_grade(float s){
  char r = 'F';
  if (s >= 85) r = 'A';
  else if (s >= 70) r = 'B';
  else if (s >= 60) r = 'C';
  else if (s >= 50) r = 'D';
  else r = 'F';
  return r;
}

void swap(float *first, float *second )
{
  float temp = *first;
  *first = *second;
  *second = temp;
}
  
void quick_sort(float *a, int left, int right)
{ 
  float key;
  int i,j;
  if( left < right ) {  
    key = *(a+left);
    i = left+1;
    j = right;
    while(i <= j) {
      while( i <= right && *(a+i) <= key) i++;
      while( j >= left && *(a+j) > key ) j--;
      if( i < j) swap(a+i, a+j);
    }    
    swap(a+left, a+j);
    quick_sort(a, left, j-1);
    quick_sort(a, j+1, right); 
  }
}

float median(NODE *start)
{
  if (start == NULL) return 0;
  int len = 0, i=0;
  NODE *np = start;
  while (np) { len++; np = np->next; }
  
  float a[len];
  for (i=0, np=start; i<len; i++, np=np->next) {
    a[i] = np->data.score;
  } 
  
  quick_sort(a, 0, len-1);
  
  return (len % 2 == 1)?  a[len/2] : (a[len/2-1] + a[len/2])/2 ; 
 } 