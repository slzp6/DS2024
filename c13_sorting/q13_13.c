/* q13_13.c   (v1.24.00) */
/* gcc q13_13.c -o q13_13 -Wall -O2 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100000000

/* ------------------------------------------ */
void print_array (int v[], int n) {
  int i;
  printf ("array: ");
  for (i = 0; i < n; i++) {
    printf ("%d ", v[i]);
  }
  printf ("\n");
}

/* ------------------------------------------ */
void rand_data (int v[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    v[i] = rand () % (MAX / 10);
  }
}

/* ------------------------------------------ */
int int_compare (const void *va, const void *vb) {
  int a, b;
  a = *(int *) va;
  b = *(int *) vb;
  if (a < b) {
    return (-1);
  }
  else if (a > b) {
    return (1);
  }
  else {
    return (0);
  }
}

/* ------------------------------------------ */
int main () {
  int *array;
  clock_t t_start, t_end;
  array = malloc (sizeof (int) * MAX);

  printf ("c-lang.\n");
  rand_data (array, MAX);
  printf ("n=%d\n", MAX);
  fflush (stdout);

  print_array (array, 10);
  t_start = clock ();
  qsort (array, MAX, sizeof (int), int_compare);
  t_end = clock ();
  print_array (array, 10);
  printf ("elapsed time: %.3lf sec.\n",
    (double) (t_end - t_start) / (double) CLOCKS_PER_SEC);
  free (array);

  return 0;
}
