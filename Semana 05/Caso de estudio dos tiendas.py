"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
metas_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.

total_centro = sum(ventas_centro) #total de ventas semanal
cantidad_centro = len(ventas_centro) #cantidad de días registradas

promedio_centro = total_centro / cantidad_centro #promedio ventas diario
menor_centro = min(ventas_centro) #venta minima de la tienda del centro
mayor_centro = max(ventas_centro) #venta maxima de la tienda del centro
meta_centro = 640000
porcentaje_centro = total_centro * 100 / meta_centro
print(total_centro)
print(porcentaje_centro)

#TODO: calcula promedio, rango, diferencia y porcentaje para Centro.
total_norte = sum(ventas_norte) #total de ventas semanal
cantidad_norte = len(ventas_norte) #cantidad de días registradas

promedio_centro = total_norte / cantidad_norte #promedio ventas diario
menor_norte = min(ventas_norte) #venta minima de la tienda del centro
mayor_norte = max(ventas_norte) #venta maxima de la tienda del centro
meta_norte = 700000
porcentaje_norte = total_norte * 100 / meta_norte
print(total_norte)
print(porcentaje_norte)
# TODO: repite los indicadores para Norte.

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else:
    estado_centro = "meta no alcanzada"

# TODO: compara los totales y los rangos.
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte = "meta alcanzada"
else:
    estado_norte = "meta no alcanzada"

# TODO: presenta un reporte con etiquetas claras y f-strings.
if total_centro > total_norte:
    tienda_mayor_ventas = "Tienda del centro"
elif total_norte > total_centro:
    tienda_mayor_venta = "tienda del norte"
else:
    tienda_mayor_venta = 'Ambas tiendas tienen el mismo total'

print(' COMPARACION SEMANAL DE TIENDAS')
print(f"Centro | total: ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro: {estado_centro}\n")
print(f"Norte | total: ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro: {estado_norte}\n")
# TODO: escribe las tres conclusiones solicitadas en la guía.