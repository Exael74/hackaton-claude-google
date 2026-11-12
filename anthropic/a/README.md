# Prueba Anthropic · API de Claude — Ejercicio A: Respuesta en streaming

- **Participante:** Stiven Esneider Pardo Gutiérrez
- **Código de la prueba:** `ANTHROPIC-03`
- **Estado:** Correcto — OK (24 verificaciones, todas correctas)

## Cómo se ejecutó
```
python solucion.py < entrada.txt > salida.txt
```

## Verificación
La salida fue comprobada con el verificador del propio enunciado (`verificar.js` en la raíz), usando mi nombre y el código `ANTHROPIC-03`:

```
OK (24 verificaciones, todas correctas)
```
Resultado completo de los 10 ejercicios: [`evidencia/verificacion.txt`](../../evidencia/verificacion.txt).

## Entrada oficial (`entrada.txt`, 417 líneas)
```
event: message_start
data: {"type":"message_start","message":{"id":"msg_01","type":"message","role":"assistant","model":"claude-ejemplo","content":[],"stop_reason":null,"usage":{"input_tokens":3328,"output_tokens":1}}}

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}

… (411 líneas más en el archivo)
```

## Salida ejecutada (`salida.txt`, 24 líneas)
```
texto: el errores errores respuesta ¿listo? código café la Bogotá código despacio respuesta en errores sin rápido compila responde arepa servidor calma
stop_reason: end_turn
input_tokens: 3328
output_tokens: 592
texto: tinto la tinto mañana modelo mañana Bogotá datos código hola
stop_reason: max_tokens
input_tokens: 1775
output_tokens: 647
texto: la tinto servidor errores compila arepa tinto en despacio ¡vamos! la errores
stop_reason: end_turn
input_tokens: 2617
output_tokens: 328
texto: código código despacio está tinto Bogotá
stop_reason: end_turn
input_tokens: 1479
output_tokens: 140
texto: hola en la lloverá en calma
stop_reason: max_tokens
input_tokens: 2617
output_tokens: 683
texto: gracias en Bogotá datos servidor arepa responde la calma ¿listo?
stop_reason: end_turn
input_tokens: 1397
output_tokens: 711
```
