import sys


def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    pos = 1
    for caso in range(1, t + 1):
        n, k = int(datos[pos]), int(datos[pos + 1])
        pos += 2

        # En vez de simular persona por persona, se lleva la cuenta de cuantos
        # tramos vacios hay de cada tamano. Siempre se parte primero el mas grande.
        tramos = {n: 1}
        while True:
            s = max(tramos)
            c = tramos.pop(s)
            izq = (s - 1) // 2
            der = s // 2          # der = max(L, R), izq = min(L, R)
            if k <= c:
                print(f"Case #{caso}: {der} {izq}")
                break
            k -= c
            tramos[izq] = tramos.get(izq, 0) + c
            tramos[der] = tramos.get(der, 0) + c


main()
