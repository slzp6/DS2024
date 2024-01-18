/* code: c10_c_bst10m.c   (v1.24.00) */
#include <stdio.h>
#include <stdlib.h>


#define DATA_SIZE   10000000
struct Node {
  int data;
  struct Node *left;
  struct Node *right;
};
typedef struct Node NODE_TYPE;

/* ------------------------------------------ */
void tree_display (NODE_TYPE * node, int level) {
  int i;

  if (node != NULL) {
    tree_display (node->right, level + 1);
    printf ("\n");
    for (i = 0; i < level; i++) {
      printf ("__");
    }
    printf ("%d", node->data);
    tree_display (node->left, level + 1);
  }
}

/* ------------------------------------------ */
NODE_TYPE *tree_insert (NODE_TYPE * node, int data) {
  if (node == NULL) {
    if (NULL == (node = malloc (sizeof (NODE_TYPE)))) {
      printf ("\nERROR: Can not allocate memory");
      exit (-1);
    }
    node->left = NULL;
    node->right = NULL;
    node->data = data;
  }
  else {
    if (data < node->data) {
      node->left = tree_insert (node->left, data);
    }
    else if (data > node->data) {
      node->right = tree_insert (node->right, data);
    }
  }
  return node;
}

/* ------------------------------------------ */
int main () {
  NODE_TYPE *root;
  int i, v;

  root = NULL;

  printf ("binary search tree\n");
  printf ("  data: %d \n", DATA_SIZE);
  fflush (stdout);
  for (i = 0; i < DATA_SIZE; i++) {
    v = rand ();
    root = tree_insert (root, v);
  }
  printf ("done\n");

  return 0;
}
