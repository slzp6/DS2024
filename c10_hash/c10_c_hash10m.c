/* code: c10_c_hash10m.c   (v1.24.00) */
#include<stdio.h>
#include<stdlib.h>

#define TABLE_SIZE  20000000
#define DATA_SIZE   10000000

enum data_status { EMPTY, OCCUPIED, DELETED };

struct hash_table_type {
  int data;
  enum data_status status;
};
typedef struct hash_table_type HASH_TABLE_TYPE;


/* ------------------------------------------- */
int hash_function (int key) {
  return (key % TABLE_SIZE);
}


/* ------------------------------------------- */
int hash_table_search (int key, HASH_TABLE_TYPE hash_table[]) {
  int i, index, new_index;

  index = hash_function (key);
  new_index = index;
  for (i = 1; i != TABLE_SIZE - 1; i++) {
    if (hash_table[new_index].status == EMPTY) {
      return -1;
    }
    if (hash_table[new_index].data == key) {
      return new_index;
    }
    new_index = (index + i) % TABLE_SIZE;
  }
  return -1;
}

/* ------------------------------------------- */
void hash_table_insert (int data, HASH_TABLE_TYPE hash_table[]) {
  int i, new_index, index;
  int key = data;

  index = hash_function (key);
  new_index = index;
  for (i = 1; i != TABLE_SIZE - 1; i++) {
    if (hash_table[new_index].status == EMPTY
	|| hash_table[new_index].status == DELETED) {
      hash_table[new_index].data = data;
      hash_table[new_index].status = OCCUPIED;
      return;
    }
    if (hash_table[new_index].data == key) {
      return;
    }
    new_index = (index + i) % TABLE_SIZE;
  }
  printf ("ERROR: table size limit exceeded [%d]\n", TABLE_SIZE);
  exit (-1);
}


/* ------------------------------------------- */
void hash_table_delete (int key, HASH_TABLE_TYPE hash_table[]) {
  int new_index = hash_table_search (key, hash_table);
  if (new_index == -1) {
    printf ("Not found\n");
  }
  else {
    hash_table[new_index].status = DELETED;
  }
}

/* ------------------------------------------- */
void hash_table_init (HASH_TABLE_TYPE hash_table[]) {
  int i;
  for (i = 0; i < TABLE_SIZE; i++) {
    hash_table[i].status = EMPTY;
  }
}

/* ------------------------------------------- */
void hash_table_display (HASH_TABLE_TYPE hash_table[]) {
  int i;
  printf ("--- hash table ---\n");
  for (i = 0; i < TABLE_SIZE; i++) {
    printf ("[%03d]:", i);
    if (hash_table[i].status == OCCUPIED) {
      printf ("[%04d]\n", hash_table[i].data);
    }
    else if (hash_table[i].status == DELETED) {
      printf ("[deleted]\n");
    }
    else {
      printf ("[empty]\n");
    }
  }
  printf ("------------------\n\n");
}




/* ------------------------------------------- */
int main () {
  int i, data;
  HASH_TABLE_TYPE *hash_table;

  hash_table = malloc (sizeof (HASH_TABLE_TYPE) * TABLE_SIZE);

  hash_table_init (hash_table);

  srand (1);
  printf ("hash table\n");
  printf ("  data:   %d \n", DATA_SIZE);
  printf ("  bucket: %d \n", TABLE_SIZE);
  fflush (stdout);
  for (i = 0; i < DATA_SIZE; i++) {
    data = rand ();
    hash_table_insert (data, hash_table);
  }
  printf ("done\n");
  free (hash_table);

  return 0;
}
