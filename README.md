# Comparación: Intérprete (Python) vs Compilador (C)

La siguiente implementacion corre un mismo algoritmo (`maqui`) en Python y en C con el objetivo de comparar su rendimiento.  
Se utiliz un codigo que calcula números primos para medir el tiempo de ejecución en ambos lenguajes.

Archivos del proyecto
- `maqui.py`:Python (intérprete).
- `maqui.c`: C(copilador).
- `compara.sh`:Script que ejecuta ambos programas y mide el tiempo.
- `plot_results.py`:Script para graficar resultados.
- `resultados.csv`:Archivo con los tiempos obtenidos.

Cómo ejecutar
ejecuta siguiente comando
gcc -O3 -o maqui maqui.c
luego
./compara.sh
esto es para correr los dos programas en los cuales compara el rendimiento entre c y python.
para ver graficamente la comparacion se coloca 
python3 pgraficar.py
