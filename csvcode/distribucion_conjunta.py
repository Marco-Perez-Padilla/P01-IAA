#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase para crear la distribución conjunta, desde un CSV o con generación aleatoria

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 05/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

import csv 
import random

class DistribucionConjunta:
    def __init__(self, N):
        """
        Inicializa una distribución conjunta binaria vacía.

        Argumento: N número de variables binarias.
        """
        self.N = N
        self.distribucion = {}

    def leer_csv(cls, nombre_archivo):
        """
        Crea una distribución conjunta a partir de un archivo CSV.

        El archivo debe contener dos columnas: una máscara binaria que
        representa el estado y su probabilidad asociada.

        Argumentos:
            cls: La propia clase
            nombre_archivo (str): nombre del archivo CSV a leer.

        Retorna:
            DistribucionConjunta: instancia con la distribución cargada
            y normalizada.
        """
        distribucion = {}
        with open(nombre_archivo, newline='') as file:
            lector = csv.reader(file)
            for fila in lector:
                mascara = fila[0].strip()
                probabilidad = float(fila[1])
                distribucion[mascara] = probabilidad

        N = len(next(iter(distribucion)))
        instancia = cls(N)
        instancia.distribucion = distribucion
        instancia._comprobar_normalizacion()
        return instancia

    def aleatoria(cls, N):
        """
        Genera una distribución conjunta aleatoria normalizada.

        Las probabilidades se generan de forma uniforme aleatoria y
        posteriormente se normalizan para que su suma sea 1.

        Argumentos:
            cls: La propia clase
            N (int): número de variables binarias.

        Retorna:
            DistribucionConjunta: instancia con la distribución generada.
        """
        instancia = cls(N)
        num_estados = 2 ** N
        valores = [random.random() for _ in range(num_estados)]
        suma = sum(valores)

        for i in range(num_estados):
            mascara = format(i, f"0{N}b")
            instancia.distribucion[mascara] = valores[i] / suma

        return instancia

    def _comprobar_normalizacion(self):
        """
        Comprueba que la distribución conjunta está correctamente normalizada.

        Lanza una excepción si la suma de probabilidades difiere de 1
        más allá de un pequeño margen de tolerancia.
        """
        suma = sum(self.distribucion.values())
        if abs(suma - 1.0) > 1e-6:
            raise ValueError("La distribución no está normalizada")

    def mostrar(self):
        """
        Muestra por pantalla la distribución conjunta, indicando cada
        estado binario y su probabilidad asociada.
        """
        print("\nDistribución conjunta:")
        for mascara, probabilidad in self.distribucion.items():
            print(mascara, "->", round(probabilidad, 5))