"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

#FASE 1 : Contar MEDICAMENTOS
conteo_medicamentos = {}
conteo_recetas = 0

# Comencemos aquí con la muestra y después construyamos nuestro contador.
print("\nMUESTRA DE DATOS")
for indice in range(3): # 0 1 2 3
    registro = registros[indice]
    print(registro["codigo"])
    #Registro - Cédula - Nombre - Diagnostico  Medicamentos 
print(f"\nCédula: {registro['paciente_cedula']}\n - Paciente:{registro['paciente_nombre']}\n - Diagnóstico:{registro['diagnostico']}\n - Medicamententos: {registro['medicamentos']}\n")


#FASE 1 : COTAR MEDICAMENTOS
conteo_medicamento = {}
conteo_recetas = 0
#FASE 2: Limpieza de datos
equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan"
}

for registro in registros:
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower() #PARACETAMOL -> "paracetamol"
        # Aplicación de FASE 2
        if nombre in equivalencias:
            nombre = equivalencias[nombre]

        if nombre in conteo_medicamento:
            conteo_medicamento[nombre] += 1
        else:
            conteo_medicamento[nombre] = 1
        conteo_recetas += 1

for medicamento, cantidad in conteo_medicamento.items():
    print(f"- {medicamento}: {cantidad}")

print("\n CONTEO DE MEDICAMENTOS")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamento)

#FASE 3 Conteo de pacientes por hospital
conteo_hospital = {}
for registro in registros:
    hospital = registro["hospital"]
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0
    conteo_hospital[hospital] += 1

print("\nANTECIONES POR HOSPITAL")
for hospital, cantidad in conteo_hospital.items():
    print("-", hospital, ":", cantidad)