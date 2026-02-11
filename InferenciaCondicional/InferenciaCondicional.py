class InferenciaCondicional:
    """
    Calcula distribuciones condicionales a partir de
    un array unidimensional de probabilidades p[k].
    """

    @staticmethod
    def prob_cond_bin(p, N, maskC, valC, maskI):
        """
        Calcula P(X_I | X_C = valC)
        
        Parámetros:
        - p: lista de probabilidades p[k] (2^N elementos)
        - N: número de variables binarias
        - maskC: máscara de variables condicionadas
        - valC: valores de variables condicionadas
        - maskI: máscara de variables de interés
        
        Retorna:
        - out: lista con la distribución condicional normalizada
        """
        # Número de combinaciones posibles de variables de interés
        num_I = 2 ** bin(maskI).count("1")
        out = [0.0] * num_I

        # Iterar sobre todas las configuraciones posibles
        for k in range(2**N):
            # Verificar si cumple la condición
            if (k & maskC) == valC:
                # Extraer índice relativo de las variables de interés
                idx = 0
                bit_pos = 0
                for i in range(N):
                    if maskI & (1 << i):
                        if k & (1 << i):
                            idx |= (1 << bit_pos)
                        bit_pos += 1
                out[idx] += p[k]

        # Normalizar
        suma = sum(out)
        if suma > 0:
            out = [x / suma for x in out]

        return out
