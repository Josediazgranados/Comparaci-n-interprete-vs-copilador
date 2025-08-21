#se crea un archivo python en la cual se ejecute un programa de contador de numeros primos.
import sys

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(limite):
    total = 0
    for i in range(2, limite + 1):
        if es_primo(i):
            total += 1
    return total

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    print(contar_primos(n))
