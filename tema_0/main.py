import os
import importlib.util
import unicodedata
import sys
from types import ModuleType

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("      - EJERCICIOS TEMA 0 PYTHON -")
    print("="*50)
    print("1. Fundamentos de Python")
    print("2. Colecciones")
    print("3. Programación Orientada a Objetos")
    print("4. Manejo de Ficheros")
    print("5. Salir")
    print("="*50)

def mostrar_submenu(categoria, ejercicios):
    print(f"\n- EJERCICIOS {categoria.upper()} -")
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"{i}. {ejercicio}")
    print("0. Volver al menú principal")

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace(" ", "_")
    text = "".join(ch for ch in text if ch.isalnum() or ch == "_")
    return text

def importar_modulo_desde_ruta(ruta: str, nombre_modulo: str) -> ModuleType:
    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"No se encontró el fichero de módulo: {ruta}")
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo crear spec para {ruta}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def encontrar_fichero_ejercicio(base_dir: str, categoria: str, numero: int, nombre_slug: str) -> str:
    """
    Busca en la carpeta src/<categoria> cualquier fichero que empiece por
    ejercicio{numero}_ y devuelve la ruta completa del fichero seleccionado.
    Selecciona el que mejor case con palabras de nombre_slug si hay varios.
    """
    carpeta = os.path.join(base_dir, "src", categoria)
    if not os.path.isdir(carpeta):
        raise FileNotFoundError(f"No existe la carpeta de categoría: {carpeta}")

    prefijo = f"ejercicio{numero}_"
    candidatos = [f for f in os.listdir(carpeta) if f.startswith(prefijo) and f.endswith(".py")]

    if not candidatos:
        raise FileNotFoundError(f"No se encontraron ficheros que comiencen por '{prefijo}' en {carpeta}")

    # Si hay un solo candidato, devolverlo
    if len(candidatos) == 1:
        return os.path.join(carpeta, candidatos[0])

    # Si hay varios, intentamos emparejar por palabras clave del slug
    partes = [p for p in nombre_slug.split("_") if p]
    # ordenamos candidatos por cuántas partes contienen en su nombre (mayor mejor)
    puntajes = []
    for c in candidatos:
        nombre_sin_ext = c[:-3]  # quitar '.py'
        score = sum(1 for p in partes if p in nombre_sin_ext)
        puntajes.append((score, c))
    puntajes.sort(reverse=True)  # mayor score primero

    mejor = puntajes[0][1]
    return os.path.join(carpeta, mejor)

def ejecutar_ejercicio(categoria, numero, nombre):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        nombre_slug = slugify(nombre)
        ruta_modulo = encontrar_fichero_ejercicio(base_dir, categoria, numero, nombre_slug)
        nombre_mod = f"{categoria}.ejercicio{numero}_{os.path.splitext(os.path.basename(ruta_modulo))[0].split('_',1)[1]}"

        modulo = importar_modulo_desde_ruta(ruta_modulo, nombre_mod)

        if hasattr(modulo, "main") and callable(modulo.main):
            modulo.main()
        elif hasattr(modulo, "run") and callable(modulo.run):
            modulo.run()
        else:
            print("El ejercicio se cargó correctamente pero no define 'main()' ni 'run()'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ImportError as e:
        print(f"Error al importar el módulo: {e}")
    except Exception as e:
        print(f"Error al ejecutar el ejercicio: {e}")

def main():
    categorias = {
        '1': ("Fundamentos", [
            "Par o Impar", "Ordenar números menos a mayor", "Suma acumulativa",
            "Número secreto", "Contar números", "Factorial",
            "Número primo", "Triángulo", "Números entre",
            "Máximo de dos números", "Es vocal", "Calculadora"
        ]),
        '2': ("Colecciones", [
            "Lista aleatoria de números del 1-100", "Máximo y Mínimo de un conjunto de números",
            "Par y impar de una lista de números", "Ordenar de forma descendente una lista número",
            "Contar apariciones de un número 1-10 de 100 números", "Frecuencia palabras",
            "Agenda de contactos", "Venta en tienda", "Scrabble", "Encriptación"
        ]),
        '3': ("Clases", [
            "Cuenta corriente", "Libro", "Punto", "Articulo"
        ]),
        '4': ("Ficheros", [
            "Media alumnos", "Escribir", "Guardar datos", "Articulo"
        ]),
        '5': ("Salir", [])
    }

    while True:
        mostrar_menu_principal()
        opcion = input("\nSelecciona una categoría (1-5): ").strip()

        if opcion not in categorias:
            print("Opción no válida. Intenta de nuevo.")
            continue

        nombre_categoria, ejercicios = categorias[opcion]

        if opcion == '5':
            print("¡Hasta luego!")
            break

        while True:
            mostrar_submenu(nombre_categoria, ejercicios)
            sub_opcion = input("\nSelecciona un ejercicio (0 para volver): ").strip()
            if sub_opcion == '0':
                break

            try:
                num = int(sub_opcion)
                if 1 <= num <= len(ejercicios):
                    nombre_ejercicio = ejercicios[num - 1]
                    ejecutar_ejercicio(nombre_categoria.lower(), num, nombre_ejercicio)
                else:
                    print("Número de ejercicio no válido.")
            except ValueError:
                print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
