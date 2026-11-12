import sys
import json
import unicodedata
from decimal import Decimal, ROUND_HALF_UP

sys.stdout.reconfigure(encoding="utf-8")


def normalizar(s):
    # minusculas, sin tildes, y todo lo que no sea letra o numero pasa a espacio
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = "".join(c if c.isalnum() else " " for c in s)
    return " ".join(s.split())


def pasa(respuesta, esperado):
    # "esperado" debe aparecer como palabras completas: 42 no pasa con 420
    return f" {normalizar(esperado)} " in f" {normalizar(respuesta)} "


def main():
    por_categoria = {}  # categoria -> [aprobadas, total]
    aprobadas = 0
    total = 0

    for linea in sys.stdin.read().splitlines():
        linea = linea.strip()
        if not linea:
            continue
        caso = json.loads(linea)
        ok = pasa(caso["respuesta"], caso["esperado"])
        cat = por_categoria.setdefault(caso["categoria"], [0, 0])
        cat[1] += 1
        total += 1
        if ok:
            cat[0] += 1
            aprobadas += 1

    for cat in sorted(por_categoria):
        a, n = por_categoria[cat]
        print(f"{cat}: {a}/{n}")

    pct = Decimal(aprobadas * 100) / Decimal(total) if total else Decimal(0)
    pct = pct.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    print(f"total: {aprobadas}/{total} ({pct}%)")


main()
