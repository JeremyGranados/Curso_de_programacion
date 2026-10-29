"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
precios_sobre_promedio = 0
while indice < len(precios):
    if precios[indice] > promedio:
        precios_sobre_promedio += 1
    indice += 1

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "Alta"
elif rango >= 150:
    variacion = "Moderada"
else:
    variacion = "Baja"

# TODO: Muestre producto y todos los resultados.
print(f"Producto: {producto}")
print(f"Promedio: ₡{promedio:.0f}")
print(f"Mínimo: ₡{minimo}")
print(f"Máximo: ₡{maximo}")
print(f"Rango: ₡{rango}")
print(f"Precios sobre el promedio: {precios_sobre_promedio}")
print(f"Variación: {variacion}")

# rango ₡350, 2 precios sobre el promedio, variación alta.
range = maximo - minimo
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
precios = [1000, 1000, 1000, 1000, 1000]
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
indice = 0
precios_sobre_promedio = 0
while indice < len(precios):
    if precios[indice] > promedio:
        precios_sobre_promedio += 1
    indice += 1
if rango >= 300:
    variacion = "Alta"
elif rango >= 150:
    variacion = "Moderada"
else:
    variacion = "Baja"
print("\nPrueba: cinco precios iguales")
print(f"Producto: {producto}")
print(f"Promedio: ₡{promedio:.0f}")
print(f"Mínimo: ₡{minimo}")
print(f"Máximo: ₡{maximo}")
print(f"Rango: ₡{rango}")
print(f"Precios sobre el promedio: {precios_sobre_promedio}")
print(f"Variación: {variacion}")
