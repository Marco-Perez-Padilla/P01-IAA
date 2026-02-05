#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase para representar el array de probabilidades

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 05/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

class ArrayProbabilidades:
    def __init__(self, distribucion_conjunta):
        """
        Inicializa el array de probabilidades p[k] a partir de una
        distribución conjunta binaria.

        Argumento:
            distribucion_conjunta: objeto que contiene la distribución 
            conjunta y el número de variables N.
        """
        self.N = distribucion_conjunta.N
        self.p = [0.0] * (2 ** self.N)
        self._cargar(distribucion_conjunta.distribucion)

    def _cargar(self, distribucion):
        """
        Carga el array p[k] a partir de la distribución conjunta.

        Cada clave binaria de la distribución se interpreta como una máscara
        y se convierte en un índice entero del array.

        Argumento:
            distribucion: diccionario que asocia máscaras binarias
            con sus probabilidades.
        """
        for mascara, prob in distribucion.items():
            k = int(mascara, 2)
            self.p[k] = prob

    def mostrar(self):
        """
        Muestra por pantalla el contenido del array de probabilidades p[k],
        indicando el índice y su representación binaria.
        """
        print("\nArray de probabilidades p[k]:")
        for i, val in enumerate(self.p):
            print(f"k={i:>3} ({format(i, f'0{self.N}b')}): {round(val, 5)}")