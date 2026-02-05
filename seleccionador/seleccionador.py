#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase para seleccionar variables de interés y condicionadas

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 05/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

class SelectorVariables:
    def __init__(self, N):
        """
        Inicializa el selector de variables condicionadas y de interés.

        Argumento: N número total de variables binarias.
        """
        self.N = N
        self.maskC = 0
        self.valC = 0
        self.maskI = 0

    def pedir_variables(self):
        """
        Solicita al usuario las variables condicionadas y las variables
        de interés, construyendo las máscaras binarias correspondientes.

        Las variables condicionadas se introducen como pares variable=valor
        y las de interés como una lista de índices.
        """
        print("\nVariables disponibles: 1 a", self.N)

        entrada = input("Variables condicionadas (ej: 2=1,4=0) o ENTER si ninguna: ")
        if entrada.strip():
            pares = entrada.split(",")
            for par in pares:
                var, val = par.split("=")
                i = int(var) - 1
                v = int(val)
                self.maskC |= (1 << i)
                if v == 1:
                    self.valC |= (1 << i)

        entrada = input("Variables de interés (ej: 1,3) o ENTER si ninguna: ")
        if entrada.strip():
            indices = entrada.split(",")
            for var in indices:
                i = int(var) - 1
                self.maskI |= (1 << i)

    def mostrar(self):
        """
        Muestra por pantalla las máscaras binarias de las variables
        condicionadas, sus valores y las variables de interés.
        """
        print("\nMáscara condicionadas :", format(self.maskC, f"0{self.N}b"))
        print("Valores condicionadas :", format(self.valC, f"0{self.N}b"))
        print("Máscara interés       :", format(self.maskI, f"0{self.N}b"))
