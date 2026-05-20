import time
import requests
from concurrent.futures import (
    ThreadPoolExecutor, as_completed
)
from requests.exceptions import HTTPError, ConnectionError, Timeout

from modelos import Country

BASE    = "https://restcountries.com/v3.1"
WORKERS = 9


class CountryAPI:
    def by_name(self, nombre: str, letra: str = "") -> Country | None:
        url = f"{BASE}/name/{nombre}"
        try:
            inicio = time.time()
            r = requests.get(url, params={"fullText": "true"}, timeout=10)
            r.raise_for_status()
            tiempo = time.time() - inicio
            return Country(r.json()[0], letra, tiempo)
        except Timeout:
            print(f"  [{letra}] {nombre}: sin respuesta (timeout)")
        except ConnectionError:
            print(f"  [{letra}] {nombre}: sin conexion a internet")
        except HTTPError as e:
            print(f"  [{letra}] {nombre}: error {e.response.status_code}")
        return None

    def by_region(self, region: str) -> list:
        url = f"{BASE}/region/{region}"
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return [Country(d, d["name"]["common"][0].lower(), 0.0) for d in r.json()]
        except Timeout:
            print(f"  Region {region}: sin respuesta (timeout)")
        except ConnectionError:
            print(f"  Region {region}: sin conexion a internet")
        except HTTPError as e:
            print(f"  Region {region}: error {e.response.status_code}")
        return []

    def by_names(self, letras_paises: list) -> list:
        resultados = []

        with ThreadPoolExecutor(WORKERS) as pool:
            futuros = {
                pool.submit(self.by_name, pais, letra): (letra, pais)
                for letra, pais in letras_paises
            }
            for f in as_completed(futuros):
                resultado = f.result()
                if resultado is not None:
                    resultados.append(resultado)

        return resultados
