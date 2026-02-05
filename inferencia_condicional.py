#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa principal para hacer inferencia condicional

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 05/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

from csvcode.distribucion_conjunta import DistribucionConjunta
from probabilidades.array_probabilidades import ArrayProbabilidades
from seleccionador.seleccionador import SelectorVariables

class Main:
    def ejecutar():
        """
        Ejecuta el flujo principal del programa.

        Permite cargar una distribución conjunta desde un archivo CSV o
        generarla de forma aleatoria, seleccionar variables condicionadas
        y mostrar el array de probabilidades resultante.
        """
        print("Inferencia Condicional en Distribuciones Binarias")
        print("1) Cargar distribución desde CSV")
        print("2) Generar distribución aleatoria")

        opcion = input("Selecciona una opción (1/2): ")

        if opcion == "1":
            nombre = input("Nombre del archivo CSV: ")
            distribucion = DistribucionConjunta.leer_csv(DistribucionConjunta, nombre)
        elif opcion == "2":
            N = int(input("Número de variables binarias N: "))
            distribucion = DistribucionConjunta.aleatoria(DistribucionConjunta, N)
        else: 
            raise ValueError("Opción no valida")

        distribucion.mostrar()

        selector = SelectorVariables(distribucion.N)
        selector.pedir_variables()
        selector.mostrar()

        array_p = ArrayProbabilidades(distribucion)
        array_p.mostrar()


if __name__ == "__main__":
    Main.ejecutar()