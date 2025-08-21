gcc -O3 maqui.c -o maqui_c -lm

echo "Metodo,N,Tiempo,Lenguaje" > resultados.csv

for n in 5 10 50 100 200 300 400 500; do

    ./maqui_c $n >> resultados.csv
    
    python3 maqui.py $n >> resultados.csv
done

echo "Ejecución completada. Resultados guardados en resultados.csv"

