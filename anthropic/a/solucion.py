import sys
import json

sys.stdout.reconfigure(encoding="utf-8")


def main():
    bloques = {}
    input_tokens = 0
    output_tokens = 0
    stop_reason = None

    for linea in sys.stdin.read().splitlines():
        if not linea.startswith("data:"):
            continue  # las lineas "event:" y las vacias no aportan nada
        evento = json.loads(linea[len("data:"):].strip())
        tipo = evento.get("type")

        if tipo == "message_start":
            bloques = {}
            input_tokens = evento["message"]["usage"]["input_tokens"]
            output_tokens = 0
            stop_reason = None
        elif tipo == "content_block_start":
            bloques[evento["index"]] = ""
        elif tipo == "content_block_delta":
            delta = evento["delta"]
            if delta.get("type") == "text_delta":
                idx = evento["index"]
                bloques[idx] = bloques.get(idx, "") + delta["text"]
        elif tipo == "message_delta":
            stop_reason = evento["delta"]["stop_reason"]
            output_tokens = evento["usage"]["output_tokens"]
        elif tipo == "message_stop":
            texto = "".join(bloques[i] for i in sorted(bloques))
            print(f"texto: {texto}")
            print(f"stop_reason: {stop_reason}")
            print(f"input_tokens: {input_tokens}")
            print(f"output_tokens: {output_tokens}")
        # "ping" y cualquier otro evento se ignoran


main()
