/* q2_7.c */
/* gcc q2_7.c -Wall -O2 -o q2_7 */
/* splint q2_7.c -compdef -usedef */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static void rand_nd(int *, int);
static int linear_search(int a[], int, int);
static int sentinel_search(int a[], int, int);

/* ------------------------------------------ */
void rand_nd(int *v, int n) {
  int i, j, t;
  for (i = 0; i < n; i++) {
    v[i] = i;
  }
  for (i = 0; i < n; i++) {
    j = rand() % n;
    t = v[i];
    v[i] = v[j];
    v[j] = t;
  }
}

/* ------------------------------------------- */
int linear_search(int array[], int n, int key) {
  int i;
  for (i = 0; i < n; i++) {
    if (array[i] == key) {
      return i;
    }
  }
  return -1;
}

/* ------------------------------------------- */
int sentinel_search(int array[], int n, int key) {
  int high, index, temp;

  high = n - 1;
  temp = array[high];
  array[high] = key;
  index = 0;
  while (array[index] != key) {
    index += 1;
  }
  array[high] = temp;
  if ((index == high) && (key != temp)) {
    return -1;
  }
  return index;
}

/* ------------------------------------------ */
int main() {
  int i, n, m, r, found, not_found;
  clock_t t_start, t_end;
  int *v = NULL;
  int *k = NULL;

  n = 5000;
  m = n * 2;
  v = malloc(sizeof(int) * n);
  if (v == NULL) {
    exit(EXIT_FAILURE);
  }
  k = malloc(sizeof(int) * m);
  if (k == NULL) {
    exit(EXIT_FAILURE);
  }

  rand_nd(v, n);
  rand_nd(k, m);

  printf("--- C lang. ---\n");
  printf("linear search\n");
  found = 0;
  not_found = 0;
  t_start = clock();
  for (i = 0; i < m; i++) {
    r = linear_search(v, n, k[i]);
    if (r == -1) {
      not_found += 1;
    } else {
      found += 1;
    }
  }
  t_end = clock();

  printf("found:%d , not_found:%d\n", found, not_found);
  printf("elapsed time: %.5lf sec.\n",
         (double)(t_end - t_start) / (double)CLOCKS_PER_SEC);

  printf("---\n");
  printf("sentinel search\n");
  found = 0;
  not_found = 0;
  t_start = clock();
  for (i = 0; i < m; i++) {
    r = sentinel_search(v, n, k[i]);
    if (r == -1) {
      not_found += 1;
    } else {
      found += 1;
    }
  }
  t_end = clock();
  printf("found:%d , not_found:%d\n", found, not_found);
  printf("elapsed time: %.5lf sec.\n",
         (double)(t_end - t_start) / (double)CLOCKS_PER_SEC);

  free(k);
  free(v);
  return 0;
}
