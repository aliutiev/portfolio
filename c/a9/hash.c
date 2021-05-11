/*
--------------------------------------------------
Project: cp264-a9q1
File:    hash.c
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h> 
#include "hash.h"

int hash(char* word) {
  unsigned int hash = 0, i;
  for (i = 0; word[i] != '\0'; i++) {
    hash = 31 * hash + word[i];
  }
  return hash % htsize;
}

HTNODE *new_hashnode(char *name, int value) {
  // creating temp node & copy
	HTNODE *the_temp_nullpointer = (HTNODE*) malloc(sizeof(HTNODE));
	strcpy(the_temp_nullpointer -> name, name);

  // setting the new hashnode
	the_temp_nullpointer -> value = value;
	the_temp_nullpointer -> next = NULL;

  // return
	return the_temp_nullpointer;
}

HASHTABLE* new_hashtable(int size) {

	int counter;

  // 
	HASHTABLE* new_heap_table = (HASHTABLE*) malloc(sizeof(HASHTABLE));
	new_heap_table -> hnp = (HTNODE**) malloc(sizeof(HTNODE**) * size);

  
  // for loop
	for (counter = 0; counter < size; counter++)
		*(new_heap_table -> hnp + counter) = NULL; // initialize to NULL

  // setting the new hashtable
	new_heap_table -> size = size;
	new_heap_table -> count = 0;

  // return
	return new_heap_table;

}

HTNODE* search(HASHTABLE *ht, char *name) { 

	int the_index = hash(name);
	HTNODE *the_temp_null_pointer = ht -> hnp[the_index];

	while (the_temp_null_pointer != NULL) {

		if (strcmp(the_temp_null_pointer -> name, name) == 0) {
			return the_temp_null_pointer;
		}

		the_temp_null_pointer = the_temp_null_pointer -> next;

	}
	return NULL;
}

int insert(HASHTABLE *ht, HTNODE *np) {
	HTNODE *the_temp_null_pointer = search(ht, np -> name);

	if (the_temp_null_pointer) {
		the_temp_null_pointer -> value = np -> value;
		return 0;
	}

	char *temp_name = np -> name;
	int count = hash(np -> name);

  // pointer to pointer for previous pointer
	HTNODE *the_temp_pointer = *(ht -> hnp + count), *pointer_to_pointer = NULL;  

  // empty linked list
	if (the_temp_pointer == NULL) {   

    // set new leading node   
		*(ht -> hnp + count) = np; 

	} else {
    // key value search
		while (the_temp_pointer && (temp_name > the_temp_pointer -> name)) {  
			pointer_to_pointer = the_temp_pointer;
			the_temp_pointer = the_temp_pointer -> next;
		}

    // if the pointer to pointer is null
		if (pointer_to_pointer == NULL){
      *(ht -> hnp + count) = np;
    } else{
      pointer_to_pointer -> next = np;
    }

		np -> next = the_temp_pointer;

	}

  // add one
	ht -> count++;

	return 1;
}

int delete(HASHTABLE *ht, char *name) {

  //setting the value
	int index = hash(name);
  // getting new nodes
	HTNODE *temp_pointer = *(ht -> hnp + index), *pointer_to_pointer = NULL;


	if (temp_pointer != NULL) {

    // while loop
		while (temp_pointer && name > temp_pointer -> name) {
			pointer_to_pointer = temp_pointer;
			temp_pointer = temp_pointer -> next;
		}

    // if valid & the names match
		if (temp_pointer && (strcmp(temp_pointer -> name, name) == 0)) {
      // if pointer to pointer is valid
			if (pointer_to_pointer) {
				pointer_to_pointer -> next = temp_pointer -> next;
      } else {
				*(ht -> hnp + index) = NULL;
      }

			free(temp_pointer);
			ht -> count--;

      // return
			return 1;

		}
	}

  // return
	return 0;

}

void clean_hash(HASHTABLE **htp) {
  if (*htp == NULL) return;
  HASHTABLE *ht = *htp;
  HTNODE *sp = ht->hnp[0], *p, *temp;
  int i;
  for (i = 0; i < ht->size; i++) {
    p = ht->hnp[i];
    while (p) {
      temp = p;  
      p = p->next;
      free(temp);
    }
  ht->hnp[i] = NULL;
  }
  free(ht->hnp);
  ht->hnp = NULL;
  *htp = NULL;
}

void display_hashtable(HASHTABLE *ht, int option) {
  int i = 0;
  HTNODE *p;
  if (option == 0) {

    printf("size:  %d\n", ht->size);
    printf("count: %d\n", ht->count);
    printf("hash data:\nindex: list of the data elements");

    for (i = 0; i < ht->size; i++) {
      p = *(ht->hnp + i);
      if (p)
        printf("\n%2d: ", i);
      
      while (p) {

        printf("(%s, %d) ", p->name, p->value);
        p = p->next;

      }
    }

    printf("\n");

  }
  else {

    for (i = 0; i < ht->size; i++) {

      p = *(ht->hnp + i);

      while (p) {

        printf("%s=%d\n", p->name, p->value);
        p = p->next;

      }
    }
  }
}