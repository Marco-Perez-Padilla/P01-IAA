#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cálculo de distribuciones condicionales

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 11/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

import numpy as np
import time

class InferenciaCondicional:
    def prob_cond_bin(array_p, N, maskC, valC, maskI):
        """
        Calcula P(X_I | X_C = valC) según la fórmula del guion.

        Parámetros:
        - array_p: objeto ArrayProbabilidades (puede ser denso o disperso)
        - N: número de variables binarias
        - maskC: máscara de variables condicionadas
        - valC: valores de variables condicionadas
        - maskI: máscara de variables de interés
        
        Retorna:
        - list: lista con la distribución condicional normalizada
        """
        # Calcular número de combinaciones de variables de interés
        num_bits_I = bin(maskI).count("1")
        num_I = 2 ** num_bits_I
        
        # Array resultado
        out = np.zeros(num_I, dtype=np.float64)
        
        for k, prob in array_p.items():
            # Verificar si cumple la condición
            if (k & maskC) == valC:
                # Extraer índice de las variables de interés
                idx = InferenciaCondicional.extraer_indice_interes(k, maskI, N)
                # Acumular probabilidad (marginalización)
                out[idx] += prob

        # Normalizar
        suma = np.sum(out)
        if suma > 0:
            out = out / suma

        return out.tolist()  

    def extraer_indice_interes(k, maskI, N):
        """
        Extrae el índice correspondiente a las variables de interés
        desde la configuración completa k.
        
        Parámetros:
        - k: configuración completa (índice en array original)
        - maskI: máscara de variables de interés
        - N: número total de variables
        
        Retorna:
        - int: índice en el array de distribución condicional
        """
        idx = 0
        bit_pos = 0 
        
        for i in range(N):
            if maskI & (1 << i):  
                if k & (1 << i): 
                    idx |= (1 << bit_pos)
                bit_pos += 1
        
        return idx