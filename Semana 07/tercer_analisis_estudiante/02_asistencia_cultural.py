"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
asistencias_total = 0
bloques_superan_70 = 0
for asistencia in asistencias:
    asistencias_total += asistencia
    if asistencia > capacidad * 0.7:
        bloques_superan_70 += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = asistencias_total / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    estado = "Alta"
elif porcentaje_ocupacion >= 50:
    estado = "Media"
else:
    estado = "Baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
print(f"Total: {asistencias_total}")
print(f"Promedio: {promedio:.1f}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.1f} %")
print(f"Cantidad de bloques que superan el 70 %: {bloques_superan_70}")
print(f"Estado: {estado}")
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
try:
    assert asistencias_total == 990
    assert promedio == 198.0
    assert porcentaje_ocupacion == 66.0
    assert bloques_superan_70 == 2
    assert estado == "Media"
except AssertionError:
    print("Error en los cálculos. Revise su código.")
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
asistencias = [240, 240, 240, 240, 240]
asistencias_total = 0
bloques_superan_70 = 0
for asistencia in asistencias:
    asistencias_total += asistencia
    if asistencia > capacidad * 0.7:
        bloques_superan_70 += 1
promedio = asistencias_total / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100
if porcentaje_ocupacion >= 80:
    estado = "Alta"
elif porcentaje_ocupacion >= 50:
    estado = "Media"
else:
    estado = "Baja"
print("\nPrueba: cinco bloques con 240 asistentes")
print(f"Total: {asistencias_total}")
print(f"Promedio: {promedio:.1f}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.1f} %")
print(f"Cantidad de bloques que superan el 70 %: {bloques_superan_70}")
print(f"Estado: {estado}")
