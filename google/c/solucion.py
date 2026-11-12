import sys


def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    pos = 1
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        actividades = []
        for i in range(n):
            s, e = int(datos[pos]), int(datos[pos + 1])
            pos += 2
            actividades.append((s, e, i))
        actividades.sort()  # por minuto de inicio

        libre = {"C": 0, "J": 0}   # minuto en que cada uno queda libre
        resultado = [""] * n
        posible = True
        for s, e, i in actividades:
            # puede empezar justo cuando termina la anterior: libre <= s
            if libre["C"] <= s:
                quien = "C"
            elif libre["J"] <= s:
                quien = "J"
            else:
                posible = False
                break
            libre[quien] = e
            resultado[i] = quien

        print(f"Case #{caso}: " + ("".join(resultado) if posible else "IMPOSSIBLE"))


main()
