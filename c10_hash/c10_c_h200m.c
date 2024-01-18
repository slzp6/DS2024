/* code: c10_c_h200m.c   (v1.24.00) */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define TABLE_SIZE  200000000
#define DATA_SIZE   100000000

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
  int i, key, data, index, a, b, total;
  HASH_TABLE_TYPE *hash_table;
  clock_t t_start, t_end;

  printf ("table_size: %d\n", TABLE_SIZE);
  printf ("data_size:  %d\n", DATA_SIZE);
  fflush (stdout);

  hash_table = malloc (sizeof (HASH_TABLE_TYPE) * TABLE_SIZE);

  printf ("hash table init. ... ");
  fflush (stdout);
  hash_table_init (hash_table);
  printf ("done\n");
  fflush (stdout);

  srand (1);
  printf ("hash table insert ... ");
  fflush (stdout);
  for (i = 0; i < DATA_SIZE; i++) {
    data = rand ();
    hash_table_insert (data, hash_table);
  }
  printf ("done\n");
  fflush (stdout);

  a = b = 0;
  srand (2);

  printf ("hash table search ... ");
  fflush (stdout);
  t_start = clock ();
  for (i = 0; i < DATA_SIZE; i++) {
    key = rand ();
    index = hash_table_search (key, hash_table);
    if (index == -1) {
      b++;			/* not found */
    }
    else {
      a++;			/* found */
    }
  }
  t_end = clock ();
  printf ("done\n");
  fflush (stdout);

  total = a + b;

  printf ("data:       %d\n", total);
  printf ("found:      %d (%2.2f%%)\n", a,
	  ((float) a / (float) total) * 100.0);
  printf ("not_found:  %d (%2.2f%%)\n", b,
	  ((float) b / (float) total) * 100.0);

  printf ("search time: %.3lf sec.\n",
	  (double) (t_end - t_start) / (double) CLOCKS_PER_SEC);
  free (hash_table);

  return 0;
}
