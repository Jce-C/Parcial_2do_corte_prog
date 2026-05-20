class Country:
    def __init__(self, data: dict, letra: str, tiempo_request: float):
        self.letra          = letra
        self.tiempo_request = tiempo_request
        self.nombre    = data["name"]["common"]
        self.capital   = data.get("capital", ["N/A"])[0]
        self.region    = data.get("region",    "N/A")
        self.subregion = data.get("subregion", "N/A")
        self.poblacion = data.get("population", 0)
        self.area      = data.get("area",       0.0)

    def __str__(self) -> str:
        return (
            f"{self.nombre} ({self.region})\n"
            f"  Capital   : {self.capital}\n"
            f"  Poblacion : {self.poblacion:,}\n"
            f"  Area      : {self.area:,.2f} km2\n"
            f"  Densidad  : {self.density():.2f} hab/km2"
        )

    def __repr__(self) -> str:
        return f"Country(nombre={self.nombre!r}, letra={self.letra!r})"

    def density(self) -> float:
        if self.area == 0:
            return 0.0
        return self.poblacion / self.area

    def comparar(self, otros: list) -> None:
        from tabla import imprimir_comparacion
        todos = [self] + otros
        imprimir_comparacion(todos)
