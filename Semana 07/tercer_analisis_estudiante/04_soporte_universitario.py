"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
incidencias_total = len(incidencias)
minutos_total = 0
conteo_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
casos_pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = (None, 0)


# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
acepted_categories = {"Acceso", "Equipo", "Red"}


# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias:
    minutos_total += incidencia["minutos_atencion"]
    if incidencia["categoria"] in acepted_categories:
        conteo_categorias[incidencia["categoria"]] += 1
    if not incidencia["resuelto"]:
        casos_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])
        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))
    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])

# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
total_promedio = minutos_total / incidencias_total
print(f"Total de incidencias: {incidencias_total}")
print(f"Total de minutos: {minutos_total}")
print(f"Promedio de minutos: {total_promedio:.1f}")
print(f"Conteo por categoría: {conteo_categorias}")
print(f"Casos pendientes: {casos_pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"Caso más largo: {caso_mas_largo}")
print(f"¿San Jose tiene pendientes? {'San Jose' in provincias_pendientes}")


# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
total_promedio = minutos_total / incidencias_total
try:
    assert incidencias_total == 10
    assert minutos_total == 500
    assert total_promedio == 50.0
    assert conteo_categorias == {"Acceso": 4, "Equipo": 3, "Red": 3}
    assert casos_pendientes == 4
    assert provincias_pendientes == {"San Jose", "Alajuela", "Heredia", "Cartago"}
    assert casos_urgentes == [("INC-02", 60), ("INC-05", 75), ("INC-07", 95)]
    assert caso_mas_largo == ("INC-07", 95)
    assert "San Jose" in provincias_pendientes
except AssertionError:
    print("Error en los cálculos. Revise su código.")

# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
incidencias[6]["resuelto"] = True



