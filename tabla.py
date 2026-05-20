def imprimir_tabla(paises):
    encabezados = ["Letra", "Pais", "Capital", "Region", "Poblacion", "Tiempo (s)"]
    anchos = [len(e) for e in encabezados]

    for p in paises:
        fila = _fila_basica(p)
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(valor)))

    _imprimir_separador(anchos)
    _imprimir_fila(encabezados, anchos)
    _imprimir_separador(anchos)
    for p in paises:
        _imprimir_fila(_fila_basica(p), anchos)
    _imprimir_separador(anchos)


def imprimir_comparacion(paises):
    encabezados = ["Pais", "Poblacion", "Area (km2)", "Densidad (hab/km2)"]
    anchos = [len(e) for e in encabezados]

    for p in paises:
        fila = _fila_comparacion(p)
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(valor)))

    print()
    _imprimir_separador(anchos)
    _imprimir_fila(encabezados, anchos)
    _imprimir_separador(anchos)
    for p in paises:
        _imprimir_fila(_fila_comparacion(p), anchos)
    _imprimir_separador(anchos)

    mayor_pob  = max(paises, key=lambda p: p.poblacion)
    mayor_area = max(paises, key=lambda p: p.area)
    mayor_den  = max(paises, key=lambda p: p.density())

    print()
    print(f"  Mayor poblacion : {mayor_pob.nombre}")
    print(f"  Mayor area      : {mayor_area.nombre}")
    print(f"  Mayor densidad  : {mayor_den.nombre}")
    print()


def imprimir_metricas(paises, tiempo_paralelo):
    tiempo_secuencial_estimado = sum(p.tiempo_request for p in paises)
    total_requests = len(paises)

    print()
    print("=== METRICAS ===")
    print(f"  Total de requests realizadas : {total_requests}")
    print(f"  Tiempo paralelo (real)        : {tiempo_paralelo:.3f} s")
    print(f"  Tiempo secuencial (estimado)  : {tiempo_secuencial_estimado:.3f} s")
    print(f"  Ahorro aproximado             : {tiempo_secuencial_estimado - tiempo_paralelo:.3f} s")
    print()
    print("  Tiempo por request individual:")
    for p in paises:
        print(f"    [{p.letra}] {p.nombre:<15} -> {p.tiempo_request:.3f} s")
    print()


def _fila_basica(pais):
    return [
        pais.letra,
        pais.nombre,
        pais.capital,
        pais.region,
        f"{pais.poblacion:,}",
        f"{pais.tiempo_request:.3f}",
    ]


def _fila_comparacion(pais):
    return [
        pais.nombre,
        f"{pais.poblacion:,}",
        f"{pais.area:,.2f}",
        f"{pais.density():.2f}",
    ]


def _imprimir_separador(anchos):
    print("+" + "+".join("-" * (a + 2) for a in anchos) + "+")


def _imprimir_fila(valores, anchos):
    print("|" + "|".join(f" {str(valores[i]):<{anchos[i]}} " for i in range(len(valores))) + "|")
