/*
--------------------------------------------------
Project: cp264a5q2
File:    a5q2.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-01-23
--------------------------------------------------
*/ 

#include "bigint_dllist.h"

NODE *new_node(char data) {
    NODE *node_temp  = (NODE *)malloc(sizeof(NODE));

    node_temp -> data = data;
    node_temp -> next = NULL;
    node_temp -> prev = NULL;

    return node_temp;
}

void display_forward(NODE *np) {
    while (np != NULL) {

        printf("%c ", np -> data);

        np = np -> next;

    }
}

void display_backward(NODE *np) {
    while (np != NULL) {
        
        printf("%c ", np -> data);

        np = np -> prev;

    }
}

void insert_start(NODE **startp, NODE **endp, NODE *new_np) {
    if(*startp != NULL ) {

        new_np -> next = *startp;

        (*startp)->prev = new_np;
        
        (*startp) = new_np;
        
    } else {

        (*startp) = new_np;

        (*endp) = new_np;

    }
}

void insert_end(NODE **startp, NODE **endp, NODE *new_np) {
    if((*endp) != NULL) {

        (*endp)->next = new_np;

        new_np->prev = *endp;
        
        (*endp) = new_np;

    } else {

        (*startp) = new_np;
     
        (*endp) = new_np;

    }
}

void delete_start(NODE **startp, NODE **endp) {
    if ((*startp) != NULL && (*endp) != NULL){

        // save location of memory
        NODE *dn = *startp;

        // if last remaining
        if ((*startp)->next != NULL) {

            (*startp) = (*startp)->next;

            (*startp)->prev = NULL;

        } else {

            (*startp) = NULL;

            (*endp) = NULL;
            
        }

        free(dn);

    }    
}

void delete_end(NODE **startp, NODE **endp) {
    if ((*endp) != NULL && (*startp) != NULL ){

        // save location of memory
        NODE *dn = *endp;


        if ((*endp) -> prev != NULL) {

            (*endp) = (*endp)->prev;

            (*endp) -> next = NULL;
            
        } else {

            (*startp) = NULL;

            (*endp) = NULL;
            
        }

        free(dn);
    }
}

void clean(NODE **startp, NODE **endp) {
    NODE *node_temporary;
    NODE *null_pointer = *startp;

    while (null_pointer != NULL) { 
        node_temporary = null_pointer; 
        null_pointer = null_pointer -> next;
        free(node_temporary);
    }

    *startp = NULL;
    *endp = NULL;
}
