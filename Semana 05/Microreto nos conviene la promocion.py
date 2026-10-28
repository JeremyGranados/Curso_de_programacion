
producto = ["cafe", 5000, 20]

ingreso_actual = producto[1] * producto[2]
porcentaje_aumento = 20
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento
print("Precio Promocional: ", precio_promocional)

ingreso_actual = producto[1] * producto[2]
unidades_proyectadas = (producto[2] * porcentaje_aumento / 100) + producto[2]
ingreso_proyectado = (precio_promocional * unidades_proyectadas) - ingreso_actual

diferencia = ingreso_proyectado - ingreso_actual

print("Diferencia:" , diferencia)

if diferencia > 0:
    print("si es recomendable")

else:
    print("no es recomendable")