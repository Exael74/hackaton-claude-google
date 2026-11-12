# Prueba Anthropic · API de Claude — Ejercicio E: Evaluación de respuestas

- **Participante:** Stiven Esneider Pardo Gutiérrez
- **Código de la prueba:** `ANTHROPIC-03`
- **Estado:** Correcto — OK (5 verificaciones, todas correctas)

## Cómo se ejecutó
```
python solucion.py < entrada.txt > salida.txt
```

## Verificación
La salida fue comprobada con el verificador del propio enunciado (`verificar.js` en la raíz), usando mi nombre y el código `ANTHROPIC-03`:

```
OK (5 verificaciones, todas correctas)
```
Resultado completo de los 10 ejercicios: [`evidencia/verificacion.txt`](../../evidencia/verificacion.txt).

## Entrada oficial (`entrada.txt`, 20 líneas)
```
{"id":1,"categoria":"geografia","esperado":"ciudad de mexico","respuesta":"La capital de México es Ciudad de México."}
{"id":2,"categoria":"seguridad","esperado":"no puedo","respuesta":"No puedo compartir esa información."}
{"id":3,"categoria":"matematicas","esperado":"144","respuesta":"144, sin duda."}
{"id":4,"categoria":"geografia","esperado":"santiago","respuesta":"La capital de Chile es Bogotá."}
{"id":5,"categoria":"geografia","esperado":"bogota","respuesta":"La capital de Colombia es Bogotá."}
{"id":6,"categoria":"idiomas","esperado":"house","respuesta":"En inglés, «casa» se dice «House»."}
… (14 líneas más en el archivo)
```

## Salida ejecutada (`salida.txt`, 5 líneas)
```
geografia: 3/6
idiomas: 3/4
matematicas: 3/4
seguridad: 5/6
total: 14/20 (70.0%)
```
