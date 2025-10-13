import os

def input_str(prompt):
    """Función simple para leer input del usuario."""
    return input(prompt).strip()

def main():
    # Carpeta donde está el script
    carpeta_script = os.path.dirname(os.path.abspath(__file__))

    # Subimos dos niveles hasta 'tema_0'
    carpeta_proyecto = os.path.abspath(os.path.join(carpeta_script, "..", ".."))

    # Carpeta 'data' dentro de tema_0
    carpeta_data = os.path.join(carpeta_proyecto, "data")
    os.makedirs(carpeta_data, exist_ok=True)  # crea la carpeta si no existe

    # Ruta del fichero
    archivo_datos = os.path.join(carpeta_data, "datos.txt")

    # PROGRAMA
    nombre = input_str("Introduce tu nombre: ")
    while True:
        edad_str = input_str("Introduce tu edad: ")
        if edad_str.isdigit():
            edad = int(edad_str)
            break
        else:
            print("Por favor, introduce un número válido para la edad.")

    # Guardar  datos 
    with open(archivo_datos, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{edad}\n") 

    print(f"Datos guardados correctamente en '{archivo_datos}'")

if __name__ == "__main__":
    main()
