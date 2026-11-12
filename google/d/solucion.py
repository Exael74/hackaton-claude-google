import sys


def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    pos = 1
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        f = [0] + [int(x) for x in datos[pos:pos + n]]; pos += n
        p = [0] + [int(x) for x in datos[pos:pos + n]]; pos += n

        # Para cada modulo v: hecho[v] = diversion de cadenas ya completas en su
        # subarbol; abierta[v] = maximo de la cadena que sigue pasando por v.
        # En cada modulo los hijos se activan de mayor a menor "abierta": la que
        # sigue por v es la menor (la que menos pierde); las demas se cierran.
        hijos = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            hijos[p[i]].append(i)

        hecho = [0] * (n + 1)
        abierta = [0] * (n + 1)
        # p[i] < i, asi que de N hacia 1 los hijos siempre van antes que el padre
        for v in range(n, 0, -1):
            if not hijos[v]:
                abierta[v] = f[v]
                continue
            menor = min(abierta[h] for h in hijos[v])
            hecho[v] = sum(hecho[h] for h in hijos[v]) + sum(abierta[h] for h in hijos[v]) - menor
            abierta[v] = max(f[v], menor)

        total = sum(hecho[v] + abierta[v] for v in range(1, n + 1) if p[v] == 0)
        print(f"Case #{caso}: {total}")


main()
