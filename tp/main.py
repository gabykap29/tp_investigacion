import matplotlib.pyplot as plt
from funcion_calcular import *


plt.figure(figsize=(12, 8))

plt.plot(n_values, times_constant, label='O(1) - Constante', marker='o')
plt.plot(n_values, times_logarithmic, label='O(log n) - Logarítmica', marker='o')
plt.plot(n_values, times_linear, label='O(n) - Lineal', marker='o')
plt.plot(n_values, times_nlogn, label='O(n log n) - Linealítmica', marker='o')
plt.plot(n_values, times_quadratic, label='O(n^2) - Cuadrática', marker='o')
plt.plot(n_values[:6], times_exponential, label='O(2^n) - Exponencial', marker='o')

plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de complejidad de algoritmos')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Escala logarítmica para visualizar mejor
plt.show()
