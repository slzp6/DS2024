/* q3_6.c   (v1.24.00) */
#include<stdio.h>
#include<stdlib.h>

#define MAX 128
#define PUSH_SUCCESS    1
#define PUSH_FAILURE   -1
#define POP_SUCCESS     2
#define POP_FAILURE    -2

/* ------------------------------------------- */
int peek (int stack[], int *top, int *data)
{
  if ((*top) > 0) {
    *data = stack[(*top) - 1];
    return POP_SUCCESS;
  }
  else {
    /* stack empty */
    return POP_FAILURE;
  }
}

/* ------------------------------------------- */
void stack_init (int *top)
{
  *top = 0;
}

/* ------------------------------------------- */
void display (int stack[], int top)
{
  int i;
  printf ("STACK(%d): ", top);
  for (i = 0; i < top; i++) {
    printf ("%d ", stack[i]);
  }
  printf ("\n");
}

/* ------------------------------------------- */
int push (int stack[], int *top, int data)
{
  if (*top >= MAX) {
    /* stack overflow */
    return PUSH_FAILURE;
  }
  else {
    stack[*top] = data;
    (*top)++;
    return PUSH_SUCCESS;
  }
}

/* ------------------------------------------- */
int pop (int stack[], int *top, int *data)
{
  if ((*top) > 0) {
    *data = stack[(*top) - 1];
    (*top)--;
    return POP_SUCCESS;
  }
  else {
    /* stack empty */
    return POP_FAILURE;
  }
}

/* ------------------------------------------- */
int main ()
{
  int stack[MAX];
  int top, data;

  stack_init (&top);

  display (stack, top);

  data = 500;
  push (stack, &top, data);
  data = 200;
  push (stack, &top, data);
  data = 600;
  push (stack, &top, data);

  display (stack, top);

  data = 300;
  printf ("push: %d\n", data);
  push (stack, &top, data);
  data = 100;
  printf ("push: %d\n", data);
  push (stack, &top, data);

  display (stack, top);

  pop (stack, &top, &data);
  printf ("pop:  %d\n", data);
  pop (stack, &top, &data);
  printf ("pop:  %d\n", data);

  display (stack, top);

  return 0;
}
