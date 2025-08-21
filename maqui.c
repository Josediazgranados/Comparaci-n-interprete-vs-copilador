#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool es_primo(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= (int) sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int contar_primos(int limite) {
    int total = 0;
    for (int i = 2; i <= limite; i++) {
        if (es_primo(i)) total++;
    }
    return total;
}

int main(int argc, char** argv) {
    int n = 100000;
    if (argc > 1) {
        n = atoi(argv[1]);
    }
    printf("%d\n", contar_primos(n));
    return 0;
}
