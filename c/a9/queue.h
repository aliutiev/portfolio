
/*
--------------------------------------------------
Project: cp264-a9q1
File:    queue.h
Description: ¯\_(ツ)_/¯ 
Author:  Andrew Liutiev 
Version: 2020-03-27
--------------------------------------------------
*/

#ifndef QUEUE_H
#define QUEUE_H

#include "common.h"

typedef struct queue {
  NODE *front;
  NODE *rear;
} QUEUE;	

void enqueue(QUEUE *qp, NODE *np);
NODE *dequeue(QUEUE *qp);
void clean_queue(QUEUE *qp);

#endif