# Prueba Anthropic · API de Claude — Ejercicio D: Límites de velocidad

- **Participante:** Stiven Esneider Pardo Gutiérrez
- **Código de la prueba:** `ANTHROPIC-03`
- **Estado:** Correcto — OK (25 verificaciones, todas correctas)

## Cómo se ejecutó
```
python solucion.py < entrada.txt > salida.txt
```

## Verificación
La salida fue comprobada con el verificador del propio enunciado (`verificar.js` en la raíz), usando mi nombre y el código `ANTHROPIC-03`:

```
OK (25 verificaciones, todas correctas)
```
Resultado completo de los 10 ejercicios: [`evidencia/verificacion.txt`](../../evidencia/verificacion.txt).

## Entrada oficial (`entrada.txt`, 25 líneas)
```
REQUEST 2 89 6540
REQUEST 5 0 568
REQUEST 8 75 0
REQUEST 9 77 4195
REQUEST 11 0 0
REQUEST 13 0 7648
… (19 líneas más en el archivo)
```

## Salida ejecutada (`salida.txt`, 25 líneas)
```
ok
ok
ok
429 retry-after=2
ok
ok
ok
ok
429 retry-after=4
429 retry-after=4
ok
ok
ok
ok
429 retry-after=2
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
```
