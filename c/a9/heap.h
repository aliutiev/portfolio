/*
--------------------------------------------------
Project: cp264-a9q1
File:    heap.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef HEAP_H
#define HEAP_H
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN_CAPACITY 4

typedef int KEYTYPE;  // key type
typedef int DATA;     // data type 

typedef struct heap_node { // data element ds for binary heap
  KEYTYPE key;
  DATA data;
} HNODE;

typedef struct heap {  
  unsigned int capacity; // the MAX length of array
  unsigned int size;     // the current heap size
  HNODE *hnap;  // pointer pointing the heap node array
} HEAP;

/* create and return a heap data structure 
to instantiate and return the pointer of the above heap structure,  size=0, capacity=4, allocate memory space to hold array of 
elements of the capacity and store pointer in data
*/
HEAP *new_heap(int capacity);

/* this inserts the given node data a into the heap; When the heap size is equal to the capacity, the inserting process needs first to expand data array by doubling its amount. This may need to copy the data of old array to new array, secondly insert the new data element into the end of the array and update size.*/
void insert(HEAP *heap, HNODE a);

/* this gets the data element of minimum key and delete the element from the binary heap. When the heap size  is no more than a quarter of the capacity, it needs to shrink the data array by half to free the unused memory space. */
HNODE extract_min(HEAP *heap);

/* this decreases the key value of given element by index to new_key_value */
void decrease_key(HEAP *heap, int index, KEYTYPE new_key_value);

/* this finds and returns the first index of heap node of given data d*/
int find_index(HEAP *heap, DATA d);

/* this displays data elements in heap by index ordering.  */
void display_heap(HEAP *heap);

/* this compare two key values a and b, return -1 if a<b, 0 if a=b, 1 if a>b  */ 
int cmp(KEYTYPE a, KEYTYPE b); 

/* help functions to ensure conditions are met */
void heap_helper(HEAP *heap, int count);
 
#endif 