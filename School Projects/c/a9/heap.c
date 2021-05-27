/*
--------------------------------------------------
Project: cp264-a9q1
File:    heap.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include "heap.h"

HEAP *new_heap(int capacity)
{
  // getting new heap
	HEAP *the_new_heap  = (HEAP*) malloc(sizeof(HEAP));

  // setting new capacity and size
	the_new_heap -> capacity = capacity;
	the_new_heap -> size = 0;

  // setting the new pointer
	the_new_heap -> hnap = (HNODE*) malloc(sizeof(HNODE) * capacity);

  // return
	return the_new_heap ;
}

void insert(HEAP *heap, HNODE new_node)
{
	if (heap == NULL)
		return;

	if (heap -> size == heap -> capacity) {
    // doubling the capacity
		heap -> capacity *= 2; 

    // getting new node
		HNODE *the_new_temp_heap_node = realloc(heap -> hnap, sizeof(HNODE) * heap -> capacity);
    
    // if valid node
		if (the_new_temp_heap_node) {
			heap -> hnap = the_new_temp_heap_node;
		} else {
			the_new_temp_heap_node = malloc(sizeof(HNODE) * heap -> capacity);

      // if the node is still valid
			if (the_new_temp_heap_node) {
				memcpy(the_new_temp_heap_node, heap -> hnap, sizeof(HNODE) * heap -> size);
				free(heap -> hnap);
				heap -> hnap = the_new_temp_heap_node;
			} else {
				printf("array resize failed\n");
			}

		}
    // compare check for size & capacity
	} else if (heap -> size <= (heap -> capacity / 4)) {

    // capacity in half
		heap -> capacity /= 2; 

    // getting new node
		HNODE *the_new_temp_heap_node = realloc(heap -> hnap, sizeof(HNODE) * heap -> capacity);

    // if valid node
		if (the_new_temp_heap_node) {
			heap -> hnap = the_new_temp_heap_node;
		} else {
      // new temp
			the_new_temp_heap_node = malloc(sizeof(HNODE) * heap -> capacity);

      // if the node is still valid
			if (the_new_temp_heap_node) {

        // creating a copy
				memcpy(the_new_temp_heap_node, heap -> hnap, sizeof(HNODE) * heap -> size);
				free(heap -> hnap);

        // new next
				heap -> hnap = the_new_temp_heap_node;
			} else {
				printf("array resize failed\n");
			}
		}
	}

  // setting variables
	int count = (heap -> size)++;
  int count_of_pointer = (count - 1) / 2;

	while (count && new_node.data > heap -> hnap[count_of_pointer].data) {
		heap -> hnap[count] = heap -> hnap[(count - 1) / 2];
		count = (count - 1) / 2;
	}

  // setting new next node
	heap -> hnap[count] = new_node;
}

HNODE extract_min(HEAP *heap)
{

  // getting the new node
	HNODE *the_new_temp_node = (HNODE*) malloc(sizeof(HNODE));

  // setting the keys and data
	the_new_temp_node -> key = heap -> hnap -> key;
	the_new_temp_node -> data = heap -> hnap -> data;

	// move the last node to the front 
	heap -> size--;
	heap -> hnap[0] = heap -> hnap[(heap -> size)];

	// takes whatever root has the minimum_value value and interchanges it, done for the whole heap
	heap_helper(heap, 0);

	// capacity gets resized if the amount of elements is less than a quarter of the entire capacity
	if (heap -> size <= (heap -> capacity / 4)) {

    // halves the capacity
		heap -> capacity /= 2; 

		HNODE *new_temp_node = realloc(heap -> hnap, sizeof(HNODE) * heap -> capacity);
    
    // if the node is valid
		if (new_temp_node) {
			heap -> hnap = new_temp_node;

      // else if the node isn't
		} else {
      // getting the new node
			new_temp_node = malloc(sizeof(HNODE) * heap -> capacity);

      // if new node is valid
			if (new_temp_node) {
        // copies to memory
				memcpy(new_temp_node, heap -> hnap, sizeof(HNODE) * heap -> size);
				free(heap -> hnap);
				heap -> hnap = new_temp_node;

        // failure
			} else {
				printf("array resize failed\n");
			}
		}
	}

  // returns
	return *the_new_temp_node;
}

void heap_helper(HEAP *heap, int count) {
  // tracks index for left, minimum value and right child
	int left_index_tracker = 2 * count + 1, minimum_value, right_index_tracker = 2 * count + 2; 
	
  // first: compare the parent&left child key to find min val of the two
  // second: makes sure the node isn't a leaf and see if the parent is greater than the key of the left child
	if (left_index_tracker < heap -> size && cmp(heap -> hnap[left_index_tracker].key, heap -> hnap[count].key) == -1) {

		minimum_value = left_index_tracker;

	} else {

		minimum_value = count;

  }

  // comparing mininmum key value with the right child key
	if (right_index_tracker < heap -> size && cmp(heap -> hnap[right_index_tracker].key, heap -> hnap[minimum_value].key) == -1) {
		minimum_value = right_index_tracker;
	}

  // if parents not already the lowest posisble value then its swapped with whichever was the lowest 
	if (minimum_value != count) {
    // new node setting
		HNODE new_temp_node = heap -> hnap[count];
    // setting the count
		heap -> hnap[count] = heap -> hnap[minimum_value];
    //setting the new point
		heap -> hnap[minimum_value] = new_temp_node;

    // recursed through until the count is equal to the min val
		heap_helper(heap, minimum_value);
	}
}

void decrease_key(HEAP *heap, int node_index, KEYTYPE key_value)
{
	int the_index_of_the_parent = (node_index - 1) / 2;

	heap -> hnap[node_index].key = key_value;

	while (the_index_of_the_parent >= 0) {

    // comparing key value to the parent key
		if (cmp(key_value, heap -> hnap[the_index_of_the_parent].key) == -1) {

      // setting new node      
			HNODE the_new_temp_node = heap -> hnap[the_index_of_the_parent];
      // setting the new index
			heap -> hnap[the_index_of_the_parent] = heap -> hnap[node_index];
      // pointing to the new node
			heap -> hnap[node_index] = the_new_temp_node;
      // new node
			node_index = the_index_of_the_parent;

		}
    // index is not equal to 0
		if (the_index_of_the_parent != 0){
			the_index_of_the_parent = (node_index - 1) / 2;
    } else {
      the_index_of_the_parent = -1;
    }
			
	}
}

int find_index(HEAP *heap, DATA value) {
  // index @0
	int index_count = 0;

  // while loop for heap
	while (index_count < heap->size && cmp(heap->hnap[index_count].data, value) != 0) {
    //increments
		index_count++;
	}

  // returns
	return index_count;
}

void display_heap(HEAP *hp) {
  printf("\nsize:%d\ncapacity:%d\n", hp->size, hp->capacity);
    printf("(index, key, data):\n");
    int i;
    for (i=0; i < hp->size; i++) {
    printf("(%d %d %d) ", i, hp->hnap[i].key, hp->hnap[i].data);
    if (i % 10 == 9) printf("\n");    
  }
    printf("\n");
}

int cmp(KEYTYPE a, KEYTYPE b) {
  if (a < b) 
     return -1;
  else if (a==b) 
     return 0;
  else 
     return 1;
}