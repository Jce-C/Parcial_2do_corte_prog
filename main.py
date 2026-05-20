import time

from api   import CountryAPI
from tabla import imprimir_tabla, imprimir_metricas

NOMBRE = "Jose Carlos"

LETRAS_PAISES = [
    ("J", "Japan"),
    ("o", "Oman"),
    ("s", "Spain"),
    ("e", "Ecuador"),
    ("C", "Canada"),
    ("a", "Argentina"),
    ("r", "Romania"),
    ("l", "Laos"),
    ("s", "Sudan"),
]


def main():
    print(f"Nombre : {NOMBRE}")
    print(f"Letras : {' '.join(l for l, _ in LETRAS_PAISES)}")
    print(f"Paises : {', '.join(p for _, p in LETRAS_PAISES)}")
    print()
    print("Lanzando todas las requests en paralelo...")
    print()

    api = CountryAPI()

    inicio = time.time()
    paises = api.by_names(LETRAS_PAISES)
    tiempo_paralelo = time.time() - inicio

    imprimir_tabla(paises)
    imprimir_metricas(paises, tiempo_paralelo)

    print("=== COMPARACION ===")
    paises[0].comparar(paises[1:])


if __name__ == "__main__":
    main()
