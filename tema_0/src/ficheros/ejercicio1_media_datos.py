import os

def main():
    try:
        # Carpeta donde está el script
        carpeta_script = os.path.dirname(os.path.abspath(__file__))
        # Subimos dos niveles hasta 'tema_0'
        carpeta_proyecto = os.path.abspath(os.path.join(carpeta_script, "..", ".."))
        # Ruta correcta al archivo
        ruta = os.path.join(carpeta_proyecto, "data", "Alumnos.txt")

        # Depuración
        print("Carpeta del script:", carpeta_script)
        print("Carpeta del proyecto:", carpeta_proyecto)
        print("Ruta absoluta del archivo:", ruta)
        print("¿Existe el archivo?", os.path.exists(ruta))
        print()

        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        edades = []
        estaturas = []

        print("Datos de alumnos:")
        for linea in lineas:
            datos = linea.strip().split()
            if len(datos) >= 3:
                nombre = datos[0]
                edad = int(datos[1])
                estatura = float(datos[2])

                print(f"{nombre}: {edad} años, {estatura}m")
                edades.append(edad)
                estaturas.append(estatura)
        
        if edades:
            print(f"\nMedia de edad: {sum(edades)/len(edades):.1f} años")
            print(f"Media de estatura: {sum(estaturas)/len(estaturas):.2f} m")
        else:
            print("No se encontraron datos válidos")

    except FileNotFoundError:
        print(f"Error: El archivo {ruta} no existe")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
