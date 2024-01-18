/* code: c9_c_avl_1m.c   (v1.24.00) */
#include<stdio.h>
#include<stdlib.h>

struct node_type {
  int data;
  int height;
  struct node_type *left;
  struct node_type *right;
};
typedef struct node_type NODE_TYPE;

/* ------------------------------------------ */
void shuffle (int *v, int n) {
  int i, j, t;
  for (i = 0; i < n; i++) {
    j = rand () % n;
    t = v[i];
    v[i] = v[j];
    v[j] = t;
  }
}

/* ------------------------------------------ */
void rand_nd (int *v, int n) {
  int i;

  for (i = 0; i < n; i++) {
    v[i] = i;
  }
  shuffle (v, n);
}

/* ------------------------------------------ */
int avl_max (int x, int y) {
  return (x > y) ? x : y;
}

/* ------------------------------------------ */
int avl_height (NODE_TYPE * node) {
  if (node == NULL) {
    return 0;
  }
  return node->height;
}

/* ------------------------------------------ */
NODE_TYPE *avl_newnode (int data) {
  NODE_TYPE *node;

  node = malloc (sizeof (NODE_TYPE));
  node->data = data;
  node->height = 1;
  node->left = NULL;
  node->right = NULL;
  return (node);
}

/* ------------------------------------------ */
NODE_TYPE *avl_right_r (NODE_TYPE * node_b) {
  NODE_TYPE *node_a;
  NODE_TYPE *temp_node;

  node_a = node_b->left;
  temp_node = node_a->right;
  node_a->right = node_b;
  node_b->left = temp_node;

  node_b->height =
    avl_max (avl_height (node_b->left), avl_height (node_b->right)) + 1;
  node_a->height =
    avl_max (avl_height (node_a->left), avl_height (node_a->right)) + 1;

  return node_a;
}

/* ------------------------------------------ */
NODE_TYPE *avl_left_r (NODE_TYPE * node_a) {
  NODE_TYPE *node_b;
  NODE_TYPE *temp_node;

  node_b = node_a->right;
  temp_node = node_b->left;
  node_b->left = node_a;
  node_a->right = temp_node;

  node_a->height =
    avl_max (avl_height (node_a->left), avl_height (node_a->right)) + 1;
  node_b->height =
    avl_max (avl_height (node_b->left), avl_height (node_b->right)) + 1;

  return node_b;
}


/* ------------------------------------------ */
int avl_height_diff (NODE_TYPE * node) {
  int diff;

  if (node == NULL) {
    return 0;
  }

  diff = avl_height (node->left) - avl_height (node->right);
  return diff;
}


/* ------------------------------------------ */
NODE_TYPE *avl_insert (NODE_TYPE * node, int data) {
  int diff;
  if (node == NULL) {
    return (avl_newnode (data));
  }
  if (data < node->data) {
    node->left = avl_insert (node->left, data);
  }
  else {
    node->right = avl_insert (node->right, data);
  }

  node->height =
    avl_max (avl_height (node->left), avl_height (node->right)) + 1;

  diff = avl_height_diff (node);

  if ((diff > 1) && (data < node->left->data)) {
    return avl_right_r (node);
  }

  if ((diff < -1) && (data > node->right->data)) {
    return avl_left_r (node);

  }

  if ((diff > 1) && (data > node->left->data)) {
    node->left = avl_left_r (node->left);
    return avl_right_r (node);
  }

  if ((diff < -1) && (data < node->right->data)) {
    node->right = avl_right_r (node->right);
    return avl_left_r (node);
  }

  return node;
}



/* ------------------------------------------ */
NODE_TYPE *avl_node_min (NODE_TYPE * node) {
  NODE_TYPE *temp_node;

  temp_node = node;
  while (temp_node->left != NULL) {
    temp_node = temp_node->left;
  }
  return temp_node;
}


/* ------------------------------------------ */
NODE_TYPE *deleteNode (NODE_TYPE * root, int data) {
  int diff;

  if (root == NULL) {
    return root;
  }
  if (data < root->data) {
    root->left = deleteNode (root->left, data);
  }
  else if (data > root->data) {
    root->right = deleteNode (root->right, data);
  }
  else {
    if ((root->left == NULL) || (root->right == NULL)) {
      NODE_TYPE *temp = root->left ? root->left : root->right;
      if (temp == NULL) {
	temp = root;
	root = NULL;
      }
      else {
	*root = *temp;
      }
      free (temp);
    }
    else {
      NODE_TYPE *temp = avl_node_min (root->right);
      root->data = temp->data;
      root->right = deleteNode (root->right, temp->data);
    }
  }


  if (root == NULL) {
    return root;
  }
  root->height =
    avl_max (avl_height (root->left), avl_height (root->right)) + 1;

  diff = avl_height_diff (root);
  if ((diff > 1) && (avl_height_diff (root->left) >= 0)) {
    return avl_right_r (root);
  }

  if ((diff > 1) && (avl_height_diff (root->left) < 0)) {
    root->left = avl_left_r (root->left);
    return avl_right_r (root);
  }

  if ((diff < -1) && (avl_height_diff (root->right) <= 0)) {
    return avl_left_r (root);
  }

  if ((diff < -1) && (avl_height_diff (root->right) > 0)) {
    root->right = avl_right_r (root->right);
    return avl_left_r (root);
  }

  return root;
}

/* ------------------------------------------ */
void tree_display (NODE_TYPE * root, int level) {
  int i;

  if (root != NULL) {
    tree_display (root->right, level + 1);
    printf ("\n");
    for (i = 0; i < level; i++) {
      printf ("_");
    }
    printf ("%d", root->data);
    tree_display (root->left, level + 1);
  }
}



/* ------------------------------------------ */
int main () {
  NODE_TYPE *root;
  int i, n;
  int *v;

  root = NULL;
  v = NULL;
  n = 1000000;

  srand (1);
  printf ("%d nodes\n", n);
  fflush (stdout);

  v = malloc (sizeof (int) * n);

  rand_nd (v, n);

  srand (1);
  for (i = 0; i < n; i++) {
    root = avl_insert (root, v[i]);
  }

  // tree_display (root, 0);
  // printf ("\n\n");

  free (v);

  return 0;
}
