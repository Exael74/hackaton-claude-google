import sys
from fractions import Fraction
from math import ceil

CAP_REQ, REC_REQ = Fraction(3), Fraction(1)      # solicitudes: capacidad 3, 1 por segundo
CAP_TOK, REC_TOK = Fraction(100), Fraction(20)   # tokens: capacidad 100, 20 por segundo


def main():
    reqs, toks = CAP_REQ, CAP_TOK   # ambas cubetas empiezan llenas
    ultimo = Fraction(0)

    for linea in sys.stdin.read().splitlines():
        partes = linea.split()
        if len(partes) != 4 or partes[0] != "REQUEST":
            continue
        t = Fraction(partes[1])
        nuevos = int(partes[2])
        # los tokens leidos de cache (partes[3]) no gastan limite de entrada

        # recarga continua desde el ultimo instante, sin pasar de la capacidad
        dt = t - ultimo
        reqs = min(CAP_REQ, reqs + dt * REC_REQ)
        toks = min(CAP_TOK, toks + dt * REC_TOK)
        ultimo = t

        if reqs >= 1 and toks >= nuevos:
            reqs -= 1
            toks -= nuevos
            print("ok")
        else:
            # segundos enteros (hacia arriba) hasta que ambas cubetas alcancen
            espera_req = max(Fraction(0), (1 - reqs) / REC_REQ)
            espera_tok = max(Fraction(0), (nuevos - toks) / REC_TOK)
            print(f"429 retry-after={ceil(max(espera_req, espera_tok))}")


main()
