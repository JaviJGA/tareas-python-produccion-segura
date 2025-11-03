alumnos = {}

# crear un par de alumnos a mano
alumnos["5113397"] = {
    "nombre": "javi jota",
    "apellidos": "apellidos",
    "telefono": "600123456",
    "asistencia": [
        {"fecha": "2025-11-01", "asiste": True},
        {"fecha": "2025-11-02", "asiste": False}
    ]
}

alumnos["1113397"] = {
    "nombre": "fanta roberto",
    "apellidos": "vegeta",
    "telefono": "600654321",
    "asistencia": [
        {"fecha": "2025-11-01", "asiste": True},
        {"fecha": "2025-11-02", "asiste": True}
    ]
}

# mostrar diccionario inicial
print("registro inicial de alumnos:")
print(alumnos)

# parte opcional: añadir alumnos nuevos
while True:
    opcion = input("\n¿quieres añadir un alumno nuevo o registrar asistencia? (AÑADIR/ASISTENCIA/SALIR): ").upper()

    if opcion == "SALIR":
        print("adiososososoo")
        break

    elif opcion == "AÑADIR":
        nre = input("introduce el NRE del alumno:\n")
        nombre = input("introduce el nombre:\n")
        apellidos = input("introduce los apellidos:\n")
        telefono = input("introduce el número de teléfono:\n")

        alumnos[nre] = {
            "nombre": nombre,
            "apellidos": apellidos,
            "telefono": telefono,
            "asistencia": []
        }
        print("alumno añadido correctamente WTF")

    elif opcion == "ASISTENCIA":
        nre = input("introduce el NRE del alumno:\n")
        if nre in alumnos:
            fecha = input("introduce la fecha (AAAA-MM-DD):\n")
            asiste_input = input("¿asistió? (S/N): ").upper()
            asiste = True if asiste_input == "S" else False
            alumnos[nre]["asistencia"].append({"fecha": fecha, "asiste": asiste})
            print("asistencia registrada correctamente.")
        else:
            print("no se encontró el NRE.")

    else:
        print("erm... opción no válida 🤓☝️")

# mostrar diccionario final
print("\nregistro de alumnos:")
print(alumnos)
