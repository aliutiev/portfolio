/*
--------------------------------------------------
Project: cp264a8q1
File:    a8q1.c  
Description: ¯\_(ツ)_/¯
Author:  Andrew Liutiev
Version: 2020-03-13
--------------------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include "avl.h"

int main(int argc, char* args[])
{
  int n = 8;
  if (argc >1)  {
    n = atoi(args[1]);
  }

  printf("Build AVL by inserting key-value (i, i) for if from 0 to %d\n", n);
  TNODE *root = NULL, *np;
  int i;
  char name[20];
  for (i = 0; i < n; i++) {
    //itoa(i, name, 10);  //itoa(int value, char *string, int radix), use number string as name
	name[0]= i+'0';
	name[1] = '\0';
	
    insert(&root, name, i+0.0);  // use number i as score data
  }

  printf("Display tree: name, socre, height\n");
  display_tree(root, 0);
  
  printf("\nis_val:%d\n", is_avl(root));
  
  printf("Inorder traversal\n");
  display_inorder(root);
  
  printf("Delete nodes of even number keys\n");
  for (i = 0; i < n; i++) {
    if (i % 2 == 0) {
      //itoa(i, name, 10);
	  name[0]= i+'0';
	  name[1] = '\0';
      delete(&root, name);
    }
  }
  display_tree(root, 0);
  
  printf("\nis_val:%d\n", is_avl(root));
  
  display_inorder(root);
  clean_tree(&root);
  return 0;
}

/*
gcc avl.c a8q1.c -o a8q1
a8q1
|___3 3.0 4
    |___5 5.0 3
        |___6 6.0 2
            |___7 7.0 1
        |___4 4.0 1
    |___1 1.0 2
        |___2 2.0 1
        |___0 0.0 1
is_val:1
0              0.0
1              1.0
2              2.0
3              3.0
4              4.0
5              5.0
6              6.0
7              7.0
|___5 5.0 3
    |___7 7.0 1
    |___3 3.0 2
        |___1 1.0 1
is_val:1
1              1.0
3              3.0
5              5.0
7              7.0
*/
