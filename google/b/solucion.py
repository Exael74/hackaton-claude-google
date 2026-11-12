import sys


def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    pos = 1
    INF = float("inf")
    for caso in range(1, t + 1):
        x, y, s = int(datos[pos]), int(datos[pos + 1]), datos[pos + 2]
        pos += 3

        # dp[c] = costo minimo del prefijo si su ultima letra queda en c
        dp = {"C": INF, "J": INF}
        primera = s[0]
        for c in "CJ":
            if primera in (c, "?"):
                dp[c] = 0

        for ch in s[1:]:
            nuevo = {"C": INF, "J": INF}
            for c in "CJ":
                if ch not in (c, "?"):
                    continue
                for prev in "CJ":
                    if dp[prev] == INF:
                        continue
                    costo = dp[prev]
                    if prev == "C" and c == "J":
                        costo += x   # aparece un CJ
                    elif prev == "J" and c == "C":
                        costo += y   # aparece un JC
                    if costo < nuevo[c]:
                        nuevo[c] = costo
            dp = nuevo

        print(f"Case #{caso}: {min(dp.values())}")


main()
