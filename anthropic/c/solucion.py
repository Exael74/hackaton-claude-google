import sys
import json

# Precios en unidades de 1e-8 dolares por token (enteros, sin flotantes):
#   entrada $3/M = 3 us/token = 300      escritura de cache = 1.25 x entrada = 375
#   lectura de cache = 0.1 x entrada = 30      salida $15/M = 1500
ENTRADA, ESCRITURA, LECTURA, SALIDA = 300, 375, 30, 1500


def fmt(v):
    # v en 1e-8 dolares -> "$X.XXXXXX" (redondeo a la millonesima, mitad hacia arriba)
    micro = (v + 50) // 100
    return f"${micro // 1_000_000}.{micro % 1_000_000:06d}"


def main():
    total = 0
    sin_cache = 0
    aciertos = 0
    n = 0

    for linea in sys.stdin.read().splitlines():
        linea = linea.strip()
        if not linea:
            continue
        u = json.loads(linea)
        n += 1
        entrada = u.get("input_tokens", 0)
        escritura = u.get("cache_creation_input_tokens", 0)
        lectura = u.get("cache_read_input_tokens", 0)
        salida = u.get("output_tokens", 0)

        costo = entrada * ENTRADA + escritura * ESCRITURA + lectura * LECTURA + salida * SALIDA
        # sin cache: todos los tokens de entrada se cobran como entrada normal
        costo_sin = (entrada + escritura + lectura) * ENTRADA + salida * SALIDA

        total += costo
        sin_cache += costo_sin
        if lectura > 0:
            aciertos += 1
        print(f"solicitud {n}: {fmt(costo)}")

    print(f"total: {fmt(total)}")
    print(f"sin_cache: {fmt(sin_cache)}")
    print(f"ahorro: {fmt(sin_cache - total)}")
    print(f"aciertos_de_cache: {aciertos}/{n}")


main()
