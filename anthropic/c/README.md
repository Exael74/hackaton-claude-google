# Prueba Anthropic · API de Claude — Ejercicio C: Costos con caché de prompts

- **Participante:** Stiven Esneider Pardo Gutiérrez
- **Código de la prueba:** `ANTHROPIC-03`
- **Estado:** Correcto — OK (16 verificaciones, todas correctas)

## Cómo se ejecutó
```
python solucion.py < entrada.txt > salida.txt
```

## Verificación
La salida fue comprobada con el verificador del propio enunciado (`verificar.js` en la raíz), usando mi nombre y el código `ANTHROPIC-03`:

```
OK (16 verificaciones, todas correctas)
```
Resultado completo de los 10 ejercicios: [`evidencia/verificacion.txt`](../../evidencia/verificacion.txt).

## Entrada oficial (`entrada.txt`, 12 líneas)
```
{"input_tokens":4455,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":524}
{"input_tokens":2753,"cache_creation_input_tokens":10896,"cache_read_input_tokens":27660,"output_tokens":1780}
{"input_tokens":1808,"cache_creation_input_tokens":776,"cache_read_input_tokens":0,"output_tokens":530}
{"input_tokens":1857,"cache_creation_input_tokens":0,"cache_read_input_tokens":19090,"output_tokens":1688}
{"input_tokens":4979,"cache_creation_input_tokens":0,"cache_read_input_tokens":1330,"output_tokens":251}
{"input_tokens":3386,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":291}
… (6 líneas más en el archivo)
```

## Salida ejecutada (`salida.txt`, 16 líneas)
```
solicitud 1: $0.021225
solicitud 2: $0.084117
solicitud 3: $0.016284
solicitud 4: $0.036618
solicitud 5: $0.019101
solicitud 6: $0.014523
solicitud 7: $0.009540
solicitud 8: $0.035280
solicitud 9: $0.039552
solicitud 10: $0.026910
solicitud 11: $0.034101
solicitud 12: $0.038649
total: $0.375900
sin_cache: $0.538587
ahorro: $0.162687
aciertos_de_cache: 5/12
```
