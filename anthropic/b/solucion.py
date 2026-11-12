import sys
import json

sys.stdout.reconfigure(encoding="utf-8")

CLIMA = {"Bogotá": 14, "Medellín": 24, "Cali": 26}


def dividir_entero(a, b):
    # division entera truncada hacia cero
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def ejecutar(nombre, args):
    if nombre == "calculadora":
        op = args.get("operacion")
        a, b = args.get("a"), args.get("b")
        if op == "sumar":
            return str(a + b)
        if op == "restar":
            return str(a - b)
        if op == "multiplicar":
            return str(a * b)
        if op == "dividir":
            if b == 0:
                return "error: división por cero"
            return str(dividir_entero(a, b))
        return f"error: operación desconocida: {op}"
    if nombre == "clima":
        ciudad = args.get("ciudad")
        if ciudad in CLIMA:
            return f"{CLIMA[ciudad]} °C"
        return f"error: ciudad desconocida: {ciudad}"
    return f"error: herramienta desconocida: {nombre}"


def main():
    llamadas = 0
    errores = 0

    for linea in sys.stdin.read().splitlines():
        linea = linea.strip()
        if not linea:
            continue
        msg = json.loads(linea)
        bloques = msg.get("content", [])

        if msg.get("stop_reason") == "tool_use":
            for b in bloques:
                if b.get("type") != "tool_use":
                    continue
                resultado = ejecutar(b["name"], b.get("input", {}))
                llamadas += 1
                if resultado.startswith("error:"):
                    errores += 1
                print(f"tool_result {b['id']} {resultado}")
        elif msg.get("stop_reason") == "end_turn":
            texto = "".join(b.get("text", "") for b in bloques if b.get("type") == "text")
            print(f"final: {texto}")

    print(f"resumen: {llamadas} llamadas, {errores} errores")


main()
