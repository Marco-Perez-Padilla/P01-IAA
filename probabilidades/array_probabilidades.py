
class ArrayProbabilidades:
    def __init__(self, distribucion_conjunta):
        self.N = distribucion_conjunta.N
        self.p = [0.0] * (2 ** self.N)
        self._cargar(distribucion_conjunta.distribucion)

    def _cargar(self, distribucion):
        """
        Carga p[k] a partir de la distribución conjunta
        """
        for mascara, prob in distribucion.items():
            k = int(mascara, 2)
            self.p[k] = prob

    def mostrar(self):
        """
        Muestra el array p[k]
        """
        print("\nArray de probabilidades p[k]:")
        for i, val in enumerate(self.p):
            print(f"k={i:>3} ({format(i, f'0{self.N}b')}): {round(val, 5)}")