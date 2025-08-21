#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long factorial_iterativo(int n) {
    long long res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

long long factorial_recursivo(int n) {
    if (n <= 1) return 1;
    return n * factorial_recursivo(n - 1);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s numero\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    clock_t start, end;
    double cpu_time;

    start = clock();
    long long fact_i = factorial_iterativo(n);
    end = clock();
    cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Iterativo,%d,%f\n", n, cpu_time);

    start = clock();
    long long fact_r = factorial_recursivo(n);
    end = clock();
    cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Recursivo,%d,%f\n", n, cpu_time);

    return 0;
}
