/*
--------------------------------------------------
Project: cp264a8q1
File:    avl.h
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-03-13
--------------------------------------------------
*/

#ifndef AVL_H
#define AVL_H

typedef struct rec {
  char name[40];
  float score;
} RECORD;

typedef struct node {
    RECORD data;
    int height;
    struct node *left;
    struct node *right;

} TNODE;

/* check if the tree is AVL tree, return 1 if true, 0 otherwise */
int is_avl(TNODE *root);

/* do left rotation  */
TNODE *rotate_left(TNODE *root);  

/* do right rotation  */
TNODE *rotate_right(TNODE *root);

/* insert record (name, score) into the AVL using name as key */
void insert(TNODE **rootp, char *name, float score);

/* delete node of data.name from the AVL */ 
void delete(TNODE **rootp, char *name);  // 

// following functions are from a7
TNODE *extract_smallest_node(TNODE **rootp); 
void display_inorder(TNODE *root);
void display_tree(TNODE *root, int prelen);
TNODE *search(TNODE *root, char *name);
void clean_tree(TNODE **rootp); 

#endif