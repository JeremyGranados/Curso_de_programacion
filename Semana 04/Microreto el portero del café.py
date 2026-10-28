"""Microreto: el portero del café."""

energia = int(input("(Cuanta energía tienes de 0-100?: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

print ("Energia: ",energia)
print ("Trae café: ", trae_cafe)

mensaje_1= "Completa las reglas del portero."

if energia < 30 and not (trae_cafe):
    mensaje = "Acceso denegado: necesitas dormar o tomar café."
# TODO: usa and para detectar energía baja sin café.
elif energia >=30 or trae_cafe: #trae_cafe == True
    mensaje = "Acceso permitido: pasa, pero comparte café."
# TODO: usa or para permitir energía suficiente o café.
else:
    mensaje = "El guarda esta confunido, revisa las respuestas."