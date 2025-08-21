import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("resultados.csv")


plt.figure(figsize=(10,6))

plt.plot(df[(df["Metodo"]=="Iterativo") & (df["Lenguaje"]=="C")]["N"],
         df[(df["Metodo"]=="Iterativo") & (df["Lenguaje"]=="C")]["Tiempo"],
         marker="o", linestyle="-", color="blue", label="C - Iterativo")

plt.plot(df[(df["Metodo"]=="Recursivo") & (df["Lenguaje"]=="C")]["N"],
         df[(df["Metodo"]=="Recursivo") & (df["Lenguaje"]=="C")]["Tiempo"],
         marker="s", linestyle="-", color="red", label="C - Recursivo")

plt.plot(df[(df["Metodo"]=="Iterativo") & (df["Lenguaje"]=="Python")]["N"],
         df[(df["Metodo"]=="Iterativo") & (df["Lenguaje"]=="Python")]["Tiempo"],
         marker="^", linestyle="-", color="green", label="Python - Iterativo")

plt.plot(df[(df["Metodo"]=="Recursivo") & (df["Lenguaje"]=="Python")]["N"],
         df[(df["Metodo"]=="Recursivo") & (df["Lenguaje"]=="Python")]["Tiempo"],
         marker="d", linestyle="-", color="orange", label="Python - Recursivo")

plt.title("Comparación de tiempos Factorial (Iterativo vs Recursivo)", fontsize=14)
plt.xlabel("N (número)", fontsize=12)
plt.ylabel("Tiempo (segundos)", fontsize=12)

plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=10)

plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("comparacion_factorial.png", dpi=300)
plt.show()

