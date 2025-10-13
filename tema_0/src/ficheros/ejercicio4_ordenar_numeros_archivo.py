import os

def main():
    # Carpeta donde está el script
    carpeta_script = os.path.dirname(os.path.abspath(__file__))

    # Subimos dos niveles hasta 'tema_0'
    carpeta_proyecto = os.path.abspath(os.path.join(carpeta_script, "..", ".."))

    # Carpeta 'data' dentro de tema_0
    carpeta_data = os.path.join(carpeta_proyecto, "data")
    os.makedirs(carpeta_data, exist_ok=True)  # crea la carpeta si no existe

    # Archivo de entrada
    archivo_entrada = os.path.join(carpeta_data, "numeros.txt")
    # Archivo de salida
    archivo_salida = os.path.join(carpeta_data, "numeros_ordenados.txt")

    
    numeros = []
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:  # evitar líneas vacías
                    try:
                        numero = int(linea)
                        numeros.append(numero)
                    except ValueError:
                        print(f"Se ignoró la línea no válida: {linea}")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no existe.")
        return

    if not numeros:
        print("No se encontraron números válidos en el archivo.")
        return

    numeros.sort()

    # Guardar en otro archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for numero in numeros:
            f.write(f"{numero}\n")

    print(f"Números ordenados guardados correctamente en '{archivo_salida}'")

if __name__ == "__main__":
    main()
