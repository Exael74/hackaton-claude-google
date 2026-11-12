import sys


def main():
    datos = sys.stdin.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        caras = sorted(int(x) for x in datos[pos:pos + n]); pos += n
        # voraz: con los dados ordenados, cada dado sirve para la siguiente
        # cifra de la escalera si tiene al menos esa cantidad de caras
        largo = 0
        for s in caras:
            if s > largo:
                largo += 1
        print(f"Case #{caso}: {largo}")


main()
