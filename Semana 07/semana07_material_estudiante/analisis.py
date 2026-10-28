from sedes import emprendimientos

print("emprendimientos registrados:", len(emprendimientos))
print("Primer emprendimiento:", emprendimientos[0]["nombre"])
print("Primer emprendimiento ventas:", emprendimientos[0]["ventas"])

print("\nANALISIS DE VENTAS")
 
#Cada vuelta procesara un diccionario
for emprendimiento in emprendimientos:
total= sum(emprendimiento['ventas'])
porcentaje = total / emprendimiento['meta'] * 100

if porcentaje >= 100:
estado = "Meta alcanzada"
elif porcentaje >= 80:
estado = "Cerca de la meta"
else:
estado = "Requiere atención!"

print(
f"{emprendimiento["nombre"]} | Total: ₡{total:,.2f} | "
f"Cumplimiento: {porcentaje:.2f}% | {estado}"
)


