#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csvcode.distribucion_conjunta import DistribucionConjunta
from seleccionador.seleccionador import SelectorVariables
from probabilidades.array_probabilidades import ArrayProbabilidades
from InferenciaCondicional.InferenciaCondicional import InferenciaCondicional
from csvcode.guardar_csv import GuardarCSV
import time

def main():
    print("Inferencia Condicional en Distribuciones Binarias")

    opcion = input("1) Cargar distribución desde CSV\n2) Generar distribución aleatoria\nSelecciona (1/2): ")

    if opcion == "1":
        nombre = input("Nombre del archivo CSV: ")
        distribucion = DistribucionConjunta.leer_csv(DistribucionConjunta, nombre)
    else:
        N = int(input("Número de variables binarias N: "))
        distribucion = DistribucionConjunta.aleatoria(DistribucionConjunta, N)

    distribucion.mostrar()

    selector = SelectorVariables(distribucion.N)
    selector.pedir_variables()
    selector.mostrar()

    array_p = ArrayProbabilidades(distribucion)
    array_p.mostrar()

    print("\n[Calculando distribución condicional...]")
    inicio = time.time()

    condicional = InferenciaCondicional.prob_cond_bin(
        array_p=array_p,
        N=distribucion.N,
        maskC=selector.maskC,
        valC=selector.valC,
        maskI=selector.maskI
    )

    tiempo = time.time() - inicio
    print(f"[Tiempo de ejecución: {tiempo*1000:.2f} ms]")

    print("\nDistribución condicional resultante:")
    num_I = len(condicional)
    num_bits_I = bin(selector.maskI).count("1")

    if num_I == 1:
        print(f"P(condición) = {condicional[0]:.5f}")
    else:
        for idx, prob in enumerate(condicional):
            mask_str = format(idx, f"0{num_bits_I}b")
            print(f"{mask_str} -> {prob:.5f}")

    print("\n--- Opciones de guardado (CSV) ---")
    resp = input("¿Guardar distribución conjunta? (S/N): ").strip().lower()
    if resp in ('s', 'si', 'sí'):
        nombre = input("Nombre del archivo [distribucion_conjunta.csv]: ").strip()
        if nombre == "":
            nombre = "distribucion_conjunta.csv"
        GuardarCSV.guardar_conjunta(
            distribucion.distribucion,
            distribucion.N,
            nombre
        )

    resp = input("¿Guardar distribución condicional? (S/N): ").strip().lower()
    if resp in ('s', 'si', 'sí'):
        nombre = input("Nombre del archivo [distribucion_condicional.csv]: ").strip()
        if nombre == "":
            nombre = "distribucion_condicional.csv"
        GuardarCSV.guardar_condicional(
            condicional,
            selector.maskI,
            nombre
        )

if __name__ == "__main__":
    main()