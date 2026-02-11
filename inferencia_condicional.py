from csvcode.distribucion_conjunta import DistribucionConjunta
from seleccionador.seleccionador import SelectorVariables
from probabilidades.array_probabilidades import ArrayProbabilidades
from InferenciaCondicional.InferenciaCondicional import InferenciaCondicional


def main():
    print("Inferencia Condicional en Distribuciones Binarias")

    opcion = input("1) Cargar distribución desde CSV\n2) Generar distribución aleatoria\nSelecciona (1/2): ")

    if opcion == "1":
        nombre = input("Nombre del archivo CSV: ")
        distribucion = DistribucionConjunta.desde_csv(nombre)
    else:
        N = int(input("Número de variables binarias N: "))
        distribucion = DistribucionConjunta.aleatoria(DistribucionConjunta, N)

    distribucion.mostrar()

    selector = SelectorVariables(distribucion.N)
    selector.pedir_variables()
    selector.mostrar()

    array_p = ArrayProbabilidades(distribucion)
    array_p.mostrar()

    # --- Punto 4 y 5: cálculo distribución condicional ---
    condicional = InferenciaCondicional.prob_cond_bin(
        p=array_p.p,
        N=distribucion.N,
        maskC=selector.maskC,
        valC=selector.valC,
        maskI=selector.maskI
    )

    # --- Punto 6: salida de la distribución condicional ---
    print("\nDistribución condicional resultante:")
    num_I = len(condicional)
    if num_I == 1:
        print(f"P(condición) = {condicional[0]:.5f}")
    else:
        for idx, prob in enumerate(condicional):
            # Representación binaria de variables de interés
            mask_str = format(idx, f"0{bin(selector.maskI).count('1')}b")
            print(f"{mask_str} -> {prob:.5f}")


if __name__ == "__main__":
    main()