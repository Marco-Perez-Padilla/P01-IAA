import csv 
class DistribucionConjunta:
    def __init__(self, N):
        self.N = N
        self.distribucion = {}

    def leer_csv(cls, nombre_archivo):
        distribucion = {}
        with open(nombre_archivo, newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                mascara = fila[0].strip()
                prob = float(fila[1])
                distribucion[mascara] = prob

        N = len(next(iter(distribucion)))
        instancia = cls(N)
        instancia.distribucion = distribucion
        instancia._comprobar_normalizacion()
        return instancia

    def aleatoria(cls, N):
        instancia = cls(N)
        num_estados = 2 ** N
        valores = [random.random() for _ in range(num_estados)]
        suma = sum(valores)

        for k in range(num_estados):
            mascara = format(k, f"0{N}b")
            instancia.distribucion[mascara] = valores[k] / suma

        return instancia

    def _comprobar_normalizacion(self):
        suma = sum(self.distribucion.values())
        if abs(suma - 1.0) > 1e-6:
            raise ValueError("La distribución no está normalizada")

    def mostrar(self):
        print("\nDistribución conjunta:")
        for m, p in self.distribucion.items():
            print(m, "->", round(p, 5))