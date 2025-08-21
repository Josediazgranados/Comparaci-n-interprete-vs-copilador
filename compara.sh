echo "Lenguaje,Tiempo(s)" > resultados.csv

echo ">> Ejecutando versión en Python"
START=$(date +%s.%N)
python3 maqui.py 100000 > /dev/null
END=$(date +%s.%N)
TIME=$(echo "$END - $START" | bc)
echo "Python,$TIME" >> resultados.csv

echo ""

echo ">> Compilando y ejecutando versión en C"
gcc -O3 maqui.c -o maqui -lm
START=$(date +%s.%N)
./maqui 100000 > /dev/null
END=$(date +%s.%N)
TIME=$(echo "$END - $START" | bc)
echo "C,$TIME" >> resultados.csv

echo ""
echo "Comparación completada."

