/*
--------------------------------------------------
Project: cp264a5q1 
File:    a5q1.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/

#ifndef RECORD_LLIST
#define RECORD_LLIST
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/**
 * RECORD structure
 * name  - char array for person's name
 * score - float score of record
 */
typedef struct {

  char name[40];

  float score;

} RECORD;

/**
 * linked list node structure
 * data  - RECORD data
 * next  - pointer pointing to next node of linked list
 */
typedef struct node {

    RECORD data;

    struct node *next;

} NODE;

/**
 * Display linked list.
 * @param start Pointer to the first node of linked list.
 */
void display(NODE *start);

/**
 * Search linked list for name key.
 * @param start Pointer to the first node of linked list.
 * @param name Key to search
 * @return Pointer to found node if found; otherwise NULL
 */
NODE *search(NODE *start, char *name);

/**
 * Insert new record to linked list at the sorted position.
 * @param startp Pointer pointing to the start pointer of linked list, used to update the start node address in case of change.
 * @param name The name data of new record.
 * @param score The score data of new record
 */
void insert(NODE **startp, char *name, float score);

/**
 * your comment
 */
int delete(NODE **startp,  char *name);

/**
 * your comment
 */
void clean(NODE **startp);


// The following functions are adapted and/or modified from previous assignment
void import_data(NODE **startp, char *filename);
void report_data(NODE *start,  char *filename);
char letter_grade(float score);
void swap(float *first, float *second );
void quick_sort(float *a, int left, int right);
float median(NODE *start);

#endif