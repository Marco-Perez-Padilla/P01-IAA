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

    def aleatoria(cls, N, num_configs=None):
        """
        Genera una distribución conjunta aleatoria normalizada.
        
        Parámetros:
            cls: La propia clase
            N (int): número de variables binarias.
            num_configs (int, opcional):
                - None: comportamiento automático (10000 si N>20, 2^N si N≤20).
                - 0: generar TODAS las configuraciones posibles (si N≤20, genera 2^N;
                     si N>20, muestra advertencia y sugiere un valor).
                - positivo: generar exactamente ese número de configuraciones (mínimo entre
                            num_configs y 2^N).
        Retorna:
            DistribucionConjunta: instancia con la distribución generada.
        """
        instancia = cls(N)
        total_posibles = 2 ** N
        UMBRAL_SPARSE = 20

        # Cuántas configuraciones generar
        if num_configs is None:
            if N > UMBRAL_SPARSE:
                num_configs = 10000
            else:
                num_configs = total_posibles
        elif num_configs == 0:
            if N <= UMBRAL_SPARSE:
                num_configs = total_posibles
            else:
                print(f"[AVISO] N={N} → 2^{N} = {total_posibles:,} configuraciones.")
                print("         Generar todas es inviable en muchos ordenadores.")
                
                resp = input("¿Continuar de todas formas? (S/N): ").strip().lower()
                if resp in ('S', 's', 'Si', 'si', 'Sí', 'sí'):
                    num_configs = total_posibles
                else:
                    while True:
                        try:
                            propuesta = int(input("Introduce número de configuraciones (ej. 10000): "))
                            if propuesta > 0:
                                num_configs = min(propuesta, total_posibles)
                                break
                        except:
                            pass
                    print(f"Generando {num_configs:,} configuraciones...")
        else:
            num_configs = min(num_configs, total_posibles)

        if num_configs == total_posibles:
            print(f"[Generando distribución completa] N={N} → {total_posibles:,} configuraciones")
            valores = [random.random() for _ in range(total_posibles)]
            suma = sum(valores)
            for i in range(total_posibles):
                mascara = format(i, f"0{N}b")
                instancia.distribucion[mascara] = valores[i] / suma
        else:
            print(f"[Generando distribución dispersa] N={N} → {num_configs:,} configuraciones")
            configs_generadas = set()
            valores = []

            while len(configs_generadas) < num_configs:
                config = random.randint(0, total_posibles - 1)
                if config not in configs_generadas:
                    configs_generadas.add(config)
                    valor = random.random()
                    valores.append((config, valor))

            valores.sort(key=lambda x: x[0])
            suma = sum(v for _, v in valores)
            for config, valor in valores:
                mascara = format(config, f"0{N}b")
                instancia.distribucion[mascara] = valor / suma

        print(f"[Completado] {len(instancia.distribucion)} configuraciones generadas")
        return instancia

    def _comprobar_normalizacion(self):
        """
        Comprueba que la distribución conjunta está correctamente normalizada.

        Lanza una excepción si la suma de probabilidades difiere de 1
        más allá de un pequeño margen de tolerancia.
        """
        suma = sum(self.distribucion.values())
        if abs(suma - 1.0) > 1e-10:
            raise ValueError(f"La distribución no está normalizada (suma={suma})")

    def mostrar(self):
        """
        Muestra por pantalla la distribución conjunta, indicando cada
        estado binario y su probabilidad asociada.
        
        Para N grande, limita la salida en consola a las primeras 50 configuraciones.
        """
        print(f"\nDistribución conjunta (N={self.N}, {len(self.distribucion)} configuraciones):")
        
        count = 0
        for mascara, probabilidad in sorted(self.distribucion.items()):
            print(f"{mascara} -> {probabilidad:.5f}")
            count += 1
            if count >= 50 and len(self.distribucion) > 50:
                print(f"... ({len(self.distribucion) - 50} configuraciones más)")
                break