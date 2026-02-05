class SelectorVariables:
    def __init__(self, N):
        self.N = N
        self.maskC = 0
        self.valC = 0
        self.maskI = 0

    def pedir_variables(self):
        """
        Entrada de variables condicionadas e interés
        """
        print("\nVariables disponibles: 1 a", self.N)

        # Variables condicionadas
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

        # Variables de interés
        entrada = input("Variables de interés (ej: 1,3): ")
        if entrada.strip():
            indices = entrada.split(",")
            for var in indices:
                i = int(var) - 1
                self.maskI |= (1 << i)

    def mostrar(self):
        """
        Muestra máscaras y valores
        """
        print("\nMáscara condicionadas :", format(self.maskC, f"0{self.N}b"))
        print("Valores condicionadas :", format(self.valC, f"0{self.N}b"))
        print("Máscara interés       :", format(self.maskI, f"0{self.N}b"))
