import time
from algoritmos.constante import * 
from algoritmos.cuadratica import *
from algoritmos.exponencial import *
from algoritmos.lineal import * 
from algoritmos.logaritmica import *
from algoritmos.Linealitmica import *

def measure_time(func, n_values):
    times = []
    for n in n_values:
        start_time = time.time()
        func(n)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

n_values = [2, 4, 8, 16, 32, 64, 128, 256]

times_constant = measure_time(constant_time, n_values)
times_logarithmic = measure_time(logarithmic_time, n_values)
times_linear = measure_time(linear_time, n_values)
times_nlogn = measure_time(nlogn_time, n_values)
times_quadratic = measure_time(quadratic_time, n_values)
times_exponential = measure_time(exponential_time, n_values[:6])  # Limit to avoid long runtimes
