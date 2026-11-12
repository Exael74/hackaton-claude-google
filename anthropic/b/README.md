# Prueba Anthropic · API de Claude — Ejercicio B: Uso de herramientas

- **Participante:** Stiven Esneider Pardo Gutiérrez
- **Código de la prueba:** `ANTHROPIC-03`
- **Estado:** Correcto — OK (22 verificaciones, todas correctas)

## Cómo se ejecutó
```
python solucion.py < entrada.txt > salida.txt
```

## Verificación
La salida fue comprobada con el verificador del propio enunciado (`verificar.js` en la raíz), usando mi nombre y el código `ANTHROPIC-03`:

```
OK (22 verificaciones, todas correctas)
```
Resultado completo de los 10 ejercicios: [`evidencia/verificacion.txt`](../../evidencia/verificacion.txt).

## Entrada oficial (`entrada.txt`, 10 líneas)
```
{"stop_reason":"tool_use","content":[{"type":"tool_use","id":"toolu_01","name":"calculadora","input":{"operacion":"sumar","a":846,"b":355}},{"type":"tool_use","id":"toolu_02","name":"clima","input":{"ciudad":"Bogotá"}},{"type":"tool_use","id":"toolu_03","name":"clima","input":{"ciudad":"Pasto"}}]}
{"stop_reason":"tool_use","content":[{"type":"tool_use","id":"toolu_04","name":"clima","input":{"ciudad":"Cali"}},{"type":"tool_use","id":"toolu_05","name":"traductor","input":{"texto":"hola"}}]}
{"stop_reason":"tool_use","content":[{"type":"text","text":"Un momento."},{"type":"tool_use","id":"toolu_06","name":"clima","input":{"ciudad":"Cali"}}]}
{"stop_reason":"tool_use","content":[{"type":"text","text":"Voy a revisarlo."},{"type":"tool_use","id":"toolu_07","name":"correo","input":{"texto":"hola"}}]}
{"stop_reason":"tool_use","content":[{"type":"tool_use","id":"toolu_08","name":"calculadora","input":{"operacion":"sumar","a":237,"b":106}},{"type":"tool_use","id":"toolu_09","name":"calculadora","input":{"operacion":"multiplicar","a":329,"b":71}},{"type":"tool_use","id":"toolu_10","name":"clima","input":{"ciudad":"Medellín"}}]}
{"stop_reason":"tool_use","content":[{"type":"tool_use","id":"toolu_11","name":"calculadora","input":{"operacion":"multiplicar","a":987,"b":264}},{"type":"tool_use","id":"toolu_12","name":"calculadora","input":{"operacion":"multiplicar","a":165,"b":316}}]}
… (4 líneas más en el archivo)
```

## Salida ejecutada (`salida.txt`, 22 líneas)
```
tool_result toolu_01 1201
tool_result toolu_02 14 °C
tool_result toolu_03 error: ciudad desconocida: Pasto
tool_result toolu_04 26 °C
tool_result toolu_05 error: herramienta desconocida: traductor
tool_result toolu_06 26 °C
tool_result toolu_07 error: herramienta desconocida: correo
tool_result toolu_08 343
tool_result toolu_09 23359
tool_result toolu_10 24 °C
tool_result toolu_11 260568
tool_result toolu_12 52140
tool_result toolu_13 14 °C
tool_result toolu_14 error: herramienta desconocida: correo
tool_result toolu_15 26 °C
tool_result toolu_16 19068
tool_result toolu_17 error: ciudad desconocida: Tunja
tool_result toolu_18 -52
tool_result toolu_19 14 °C
tool_result toolu_20 570
final: Listo, revisé 20 resultados.
resumen: 20 llamadas, 5 errores
```
