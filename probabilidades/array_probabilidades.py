#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase para representar el array de probabilidades p[k]

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 05/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

import numpy as np

class ArrayProbabilidades:
    def __init__(self, distribucion_conjunta):
        """
        Inicializa el array de probabilidades p[k] a partir de una
        distribución conjunta binaria.
        
        IMPLEMENTACIÓN ADAPTATIVA:
        - N ≤ 20: array denso NumPy.
        - N > 20: diccionario disperso.
        - En ambos casos, la estructura es unidimensional. Se ha implementado 
        para permitir el cálculo con N=32, y se ha comprobado que funciona para
        N=64.

        Argumento:
            distribucion_conjunta: objeto que contiene la distribución 
            conjunta (dict) y el número de variables N.
        """
        self.N = distribucion_conjunta.N
        UMBRAL_SPARSE = 20
        
        if self.N > UMBRAL_SPARSE:
            self.p_sparse = {}
            self.is_sparse = True
            self.cargar_sparse(distribucion_conjunta.distribucion)
            print(f"[Array disperso] N={self.N} → {len(self.p_sparse):,} configuraciones de {2**self.N:,}")
        else:
            self.p = np.zeros(2 ** self.N, dtype=np.float64)
            self.is_sparse = False
            self.cargar_denso(distribucion_conjunta.distribucion)

    def cargar_denso(self, distribucion):
        """
        Carga el array p[k] completo
        
        Cada máscara binaria se convierte a índice k = int(máscara, 2)

        Argumento:
            distribucion (dict): Diccionario con claves = máscara binaria (str) y valores = probabilidad (float)
        """
        for mascara, probabilidad in distribucion.items():
            k = int(mascara, 2)
            self.p[k] = probabilidad

    def cargar_sparse(self, distribucion):
        """
        Carga solo las probabilidades no-cero
        
        Argumento:
            distribucion (dict): Diccionario con claves = máscara binaria (str) y valores = probabilidad (float)
        """
        for mascara, probabilidad in distribucion.items():
            if probabilidad > 0:
                k = int(mascara, 2)
                self.p_sparse[k] = probabilidad

    def get(self, k):
        """
        Obtiene p[k] de forma transparente (compatible con ambos modos).
        
        Argumento:
            k(int): Índice de la configuración (0 ≤ k < 2^N).
        Retorna:
            float: probabilidad de la configuración k, o 0.0 si no existe.
        """
        if self.is_sparse:
            return self.p_sparse.get(k, 0.0)
        else:
            return self.p[k]
    
    def items(self):
        """
        Itera sobre (k, p[k]) 
        """
        if self.is_sparse:
            return self.p_sparse.items()
        else:
            nonzero_indices = np.nonzero(self.p)[0]
            return ((int(k), float(self.p[k])) for k in nonzero_indices)
    
    def num_nonzero(self):
        """
        Retorna el número de configuraciones con probabilidad no-cero.
        """
        if self.is_sparse:
            return len(self.p_sparse)
        else:
            return int(np.count_nonzero(self.p))

    def mostrar(self):
        """
        Muestra por pantalla el contenido del array de probabilidades p[k].
        Para N grande, muestra solo configuraciones no-cero.
        """
        print(f"\nArray de probabilidades p[k] (N={self.N}):")
        
        if self.is_sparse:
            print(f"Modo disperso: {len(self.p_sparse):,} de {2**self.N:,} configuraciones")
            for k in sorted(self.p_sparse.keys())[:50]:  # Limitar a primeras 50 para N grande
                print(f"k={k:>10} ({format(k, f'0{self.N}b')}): {self.p_sparse[k]:.10f}")
            if len(self.p_sparse) > 50:
                print(f"... ({len(self.p_sparse) - 50} configuraciones más)")
        else:
            count = 0
            for i, val in enumerate(self.p):
                if val > 0:
                    print(f"k={i:>3} ({format(i, f'0{self.N}b')}): {val:.10f}")
                    count += 1
            if count == 0:
                print("(Todas las probabilidades son cero)")