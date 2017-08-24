#include <math.h>
#include <stdio.h>
#include <time.h>

double nop(double a, double b, double x){
    return x;
}

double xlogy(double x, double y){
  if(x == 0.0 || y == 0.0){
    return 0.0;
  }
  return x * log(y);
}

double beta_logpdf(double a, double b, double x){
  double prefactor;
  prefactor = lgamma(a + b) - (lgamma(a) + lgamma(b));
  return prefactor + xlogy(a - 1.0, x) + xlogy(b - 1.0, 1.0 - x);
}

int main(void){
  int N;
  clock_t start, end;
  double diff;
  N = 1000000;
  start = clock();
  for(int i = 0; i < N; i++){
    beta_logpdf(1.0, 2.0, i);
  }
  end = clock();
  diff = (double)(end - start) / (CLOCKS_PER_SEC);
  printf("Time in seconds %f", diff);
  return 0;
}
