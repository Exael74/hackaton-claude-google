#!/usr/bin/env bash
# Ejecuta las 10 soluciones con su entrada oficial y verifica cada salida con el verificador del enunciado.
NOMBRE="Stiven Esneider Pardo Gutiérrez"
GH="enunciados/Prueba Google · Code Jam · Hackatón individual.html"
AH="enunciados/Prueba Anthropic · La API de Claude · Hackatón individual.html"
i=1
for l in a b c d e; do
  (cd google/$l && python -X utf8 solucion.py < entrada.txt > salida.txt)
  (cd anthropic/$l && python -X utf8 solucion.py < entrada.txt > salida.txt)
  echo "GOOGLE-03     ejercicio ${l^^}: $(node verificar.js "$GH" google "$NOMBRE" GOOGLE-03 g$i google/$l/salida.txt)"
  echo "ANTHROPIC-03  ejercicio ${l^^}: $(node verificar.js "$AH" anthropic "$NOMBRE" ANTHROPIC-03 b$i anthropic/$l/salida.txt)"
  i=$((i+1))
done
