#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase para guardar la distribucion conjunta y condicional en formato CSV

Autores: Keran Miranda González, Marco Pérez Padilla
Fecha: 11/02/2026
Universidad de La Laguna - Inteligencia Artificial Avanzada
"""

import csv
import os

class GuardarCSV:
    def guardar_conjunta(distribucion_dict, N, nombre_archivo="distribucion_conjunta.csv"):
        """
        Guarda una distribución conjunta en un archivo CSV.
        
        Argumentos:
            distribucion_dict (dict): Diccionario con clave=máscara str, valor=probabilidad float.
            N (int): Número total de variables (para verificar longitudes).
            nombre_archivo (str): Nombre del archivo de salida.
        
        Retorna:
            bool: True si se guardó correctamente, False en caso de error.
        """
        try:
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for mascara, probabilidad in sorted(distribucion_dict.items()):
                    writer.writerow([mascara, f"{probabilidad:.10f}"])
            print(f"Distribución conjunta guardada en {nombre_archivo}")
            return True
        except Exception as error:
            print(f"Error al guardar distribución conjunta: {error}")
            return False

    def guardar_condicional(condicional_list, maskI, nombre_archivo="distribucion_condicional.csv"):
        """
        Guarda una distribución condicional en un archivo CSV.
        
        Argumentos:
            condicional_list (list): Lista de floats (tamaño = 2^(#bits en maskI)).
            maskI (int): Máscara de variables de interés.
            nombre_archivo (str): Nombre del archivo de salida.
        
        Retorna:
            bool: True si se guardó correctamente, False en caso de error.
        """
        try:
            num_bits_I = bin(maskI).count("1")
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for indice, probabilidad in enumerate(condicional_list):
                    mascara_interes = format(indice, f"0{num_bits_I}b")
                    writer.writerow([mascara_interes, f"{probabilidad:.10f}"])
            print(f"Distribución condicional guardada en {nombre_archivo}")
            return True
        except Exception as error:
            print(f"Error al guardar distribución condicional: {error}")
            return False