"""Expediente de 12 atenciones ficticias.

Complete lector_csv.py y siga la guía de Semana 09. Cambie ETAPA de 1 a 2
y luego a 3 conforme verifique cada parte con python analisis_atenciones.py.
"""

from lector_csv import cargar_atenciones


ETAPA = 1


def explorar_atenciones(atenciones):
    """Recibe la lista de atenciones y muestra el total, los tipos y los campos."""
    # P1. Complete el lector y compruebe el mensaje de archivo faltante.
    


    print("P1. Archivo leído correctamente.")

    # P2. Cuente las filas con un ciclo. Compruebe que obtuvo 12.
    contador = 0
    for atencion in atenciones:
        contador += 1
    print("P2. Total de atenciones:", contador)

    # P3. Ejemplo listo para ejecutar. Explique qué tipos y campos observa.
    primer_registro = atenciones[0]
    tipos = {type(valor) for valor in primer_registro.values()}
    campos = list(primer_registro.keys())
    print("P3. Tipos de valores:", tipos)
    print("P3. Campos:", campos)

    


def contar_y_limpiar(atenciones):
    """Recibe la lista de atenciones y muestra los conteos y sus comprobaciones."""
    print("Etapa 2. Complete y compruebe las preguntas 4 a 8.")
    # P4. Cuente los medicamentos tal como aparecen en el CSV con .get().
    # Muestre el contador y su total.
    contador_medicamentos = {}
    for atencion in atenciones:
        medicamento = atencion.get("medicamento")

        if medicamento in contador_medicamentos:
            contador_medicamentos[medicamento] += 1
        else:
            contador_medicamentos[medicamento] = 1
    print("Medicamentos: ", contador_medicamentos)
    print("Total de medicamentos:", sum(contador_medicamentos.values()))

    # P5. Muestre ejemplos de espacios o mayúsculas en hospital,
    # diagnostico y medicamento.
    for atencion in atenciones:
        hospital = atencion.get("hospital")
        diagnostico = atencion.get("diagnostico")
        medicamento = atencion.get("medicamento")

        if hospital != hospital.strip() or diagnostico != diagnostico.strip() or medicamento != medicamento.strip():
            print("Ejemplo con espacios o mayúsculas:")
            print("Hospital:", hospital)
            print("Diagnóstico:", diagnostico)
            print("Medicamento:", medicamento)
    # P6. Cuente los medicamentos con strip() y lower(). Muestre el
    # contador limpio y su total. Compare con P4.
    contador_limpio = {}
    for atencion in atenciones:
        medicamento = atencion.get("medicamento")
        medicamento = medicamento.strip().lower()

        if medicamento in contador_limpio:
            contador_limpio[medicamento] += 1
        else:
            contador_limpio[medicamento] = 1
    print("Medicamentos limpios:", contador_limpio)
    print("Total de medicamentos limpios:", sum(contador_limpio.values()))


    # P7. Agrupe los nombres limpios con las equivalencias de la guía.
    # Complete el diccionario. La clave es la variante y el valor es
    # el nombre que conservará. El nuevo contador debe sumar 12.
    equivalencias = {}

    # P8. Cuente hospitales y diagnósticos con los nombres limpios.
    # Muestre ambos contadores, sus totales y la categoría más frecuente de
    # cada campo.


def concluir(atenciones):
    """Recibe la lista de atenciones y muestra el resumen de pacientes y esperas."""
    print("Etapa 3. Complete y compruebe las preguntas 9 y 10.")
    # P9. Cuente por cédula. Muestre cuántas personas hay, cuáles cédulas
    # se repiten y si coinciden el nombre, la edad y la provincia.

    # P10. Sume minutos_espera con un ciclo. Muestre el total y el promedio.
    # Redacte un hallazgo que use el promedio y un conteo.


atenciones = cargar_atenciones()
if not atenciones:
    print("Revise los TODO de lector_csv.py antes de continuar.")
elif ETAPA == 1:
    explorar_atenciones(atenciones)
elif ETAPA == 2:
    contar_y_limpiar(atenciones)
elif ETAPA == 3:
    concluir(atenciones)
else:
    print("Seleccione 1, 2 o 3 en ETAPA.")
