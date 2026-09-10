from AulasPraticas.AP_03_ordenacao import *
import random as r
import time
import sys

r.seed(1001)
sys.setrecursionlimit(max(10000, 6000))

def caso_medio(N):
    lista = []
    for _ in range(N):
        lista.append(r.randint(0, 50000))
    return lista

def pior_caso(N):
    return list(range(N, 0, -1))

def medir_tempo(algoritmo, lista, k=50):
    tempo_total = 0.0
    for _ in range(k):
        dados = lista.copy()
        inicio = time.perf_counter()
        algoritmo(dados)
        fim = time.perf_counter()
        tempo_total += (fim-inicio)
    return tempo_total/k


def benchmark():
    algoritmos = [selection_sort, quick_sort, divide_and_conquer_sort]
    print(f"{'Algoritmo':<24} | {'N':<6} | {'Caso Médio (s)':<15} | {'Pior caso (s)':<15}")
    print("-"*65)

    for algoritmo in algoritmos:
        for N in [100, 500, 1000, 5000]:
            medio = caso_medio(N)
            pior = pior_caso(N)
            tempo_caso_medio = medir_tempo(algoritmo, medio)
            tempo_pior_caso = medir_tempo(algoritmo, pior)
            print(f"{algoritmo.__name__:<24} | {N:<6} | {tempo_caso_medio:<15.6f} | {tempo_pior_caso:<15.6f}")
        print("-" * 65)

benchmark()