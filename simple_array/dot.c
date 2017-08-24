#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

double dot(double* x, int len_x, double* y, int len_y){
  double sum = 0.0;
  if (len_x != len_y) return -INFINITY;

  for(int i = 0; i < len_x; i++){
    sum += x[i] * y[i];
  }
  return sum;
}

int main(void){
  int N = 10000;
  const int len_x = 100000;
  clock_t start, end;
  double x[len_x], y[len_x], diff, sum;

  srand(0);
  diff = 0.0;
  for(int i = 0; i < N; i++){
    for(int i = 0; i < len_x; i++){
      x[i] = rand();
      y[i] = rand();
    }
    start = clock();
    sum = dot(x, len_x, y, len_x);
    end = clock();
    diff += (double)(end - start);
  }
  diff /= (double) CLOCKS_PER_SEC;
  printf("Time in seconds %f", diff);
  return 0;
}
