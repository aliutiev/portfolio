/*
--------------------------------------------------
Project: cp264-a9q1
File:    hash.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef HASH_H
#define HASH_H

extern int htsize;

typedef struct hashnode {
  char name[10];  // used as key variable
  int value;
  struct hashnode *next; 
} HTNODE;

typedef struct hashtable {
  HTNODE **hnp;    // pointer pointing to the array of hashnode pointers 
  int size;          // hash table size, maximum number of different indices
  int count;         // number of data elements in the hash table
} HASHTABLE;

/* hash function that hash name string to an integer of modular htsize */
int hash(char *name); 

/* create dynamically a hash node and set name and value and return the point */
HTNODE *new_hashnode(char *name, int vale); 

/* create dynamically a chained hash table of the size */
HASHTABLE *new_hashtable(int size); 

/* search the hash table and return the pointer of found hashnode */
HTNODE *search(HASHTABLE *ht, char *name);

/* insert hashnode np to hash table
 * when the named hashnode exists, update the hashnode's value by np->value, return 0;
 * otherwise insert into the hash table, return 1 
*/
int insert(HASHTABLE *ht, HTNODE *np);

/* 
 * delete hashnode by name. If the named hash node exists, delete it and return 1; 
 * otherwise return 0
*/
int delete(HASHTABLE *ht, char *name);

void clean_hash(HASHTABLE **htp);

void display_hashtable(HASHTABLE *ht, int option);

#endif