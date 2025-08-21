import sys
import time

def factorial_iterativo(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_recursivo(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    # Iterativo
    start = time.time()
    factorial_iterativo(n)
    end = time.time()
    print(f"Iterativo,{n},{end - start},Python")

    # Recursivo
    start = time.time()
    factorial_recursivo(n)
    end = time.time()
    print(f"Recursivo,{n},{end - start},Python")

