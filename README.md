# Hackatón individual 2026-2 — Prueba Google y Prueba Anthropic

**Participante:** Stiven Esneider Pardo Gutiérrez
**Códigos de prueba:** `GOOGLE-03` (Prueba Google · Code Jam) · `ANTHROPIC-03` (Prueba Anthropic · API de Claude)

## Evidencia de ingreso con nombre y código
- `evidencia/google_ingreso_nombre_y_codigo.png`
- `evidencia/anthropic_ingreso_nombre_y_codigo.png`

Cada captura muestra el enunciado (HTML) con el nombre y el código escritos, el estado "Entradas de … listas" y la entrada oficial generada.

## Ejercicios
Cada carpeta contiene un `README.md` con la evidencia (entrada, salida y verificación), `solucion.py`, `entrada.txt` (entrada oficial generada con mi nombre y código) y `salida.txt` (salida ejecutada).

| Ejercicio | Google (`google/`) | Anthropic (`anthropic/`) |
|---|---|---|
| A | [`a/`](google/a/README.md) d1000000 | [`a/`](anthropic/a/README.md) Streaming |
| B | [`b/`](google/b/README.md) Moons and Umbrellas | [`b/`](anthropic/b/README.md) Uso de herramientas |
| C | [`c/`](google/c/README.md) Parenting Partnering Returns | [`c/`](anthropic/c/README.md) Costos con caché |
| D | [`d/`](google/d/README.md) Chain Reactions | [`d/`](anthropic/d/README.md) Límites de velocidad |
| E | [`e/`](google/e/README.md) Bathroom Stalls | [`e/`](anthropic/e/README.md) Evaluación de respuestas |

## Verificación
Resultado de ejecutar cada solución y comprobar la salida con el verificador del propio enunciado: `evidencia/verificacion.txt`.

```
bash ejecutar_y_verificar.sh
```
Requiere Python 3 y Node.js. Los enunciados originales están en `enunciados/`.
