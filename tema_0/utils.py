def input_int(mensaje, min_val=None, max_val=None):
    """Solicita un número entero válido"""
    while True:
        try:
            valor = int(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El número debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f"Error: El número debe ser menor o igual a {max_val}")
                continue
            return valor
        except ValueError:
            print("Error: Debes introducir un número entero válido")

def input_float(mensaje, min_val=None, max_val=None):
    """Solicita un número decimal válido"""
    while True:
        try:
            valor = float(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"Error: El número debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f"Error: El número debe ser menor o igual a {max_val}")
                continue
            return valor
        except ValueError:
            print("Error: Debes introducir un número válido")

def input_str(mensaje, opciones_validas=None, min_len=1):
    """Solicita texto con validaciones opcionales"""
    while True:
        valor = input(mensaje).strip()
        if len(valor) < min_len:
            print(f"Error: El texto debe tener al menos {min_len} caracteres")
            continue
        if opciones_validas and valor.lower() not in [opc.lower() for opc in opciones_validas]:
            print(f"Error: Opciones válidas: {', '.join(opciones_validas)}")
            continue
        return valor

def validar_telefono(telefono):
    """Valida que el teléfono contenga solo números"""
    return telefono.isdigit() and len(telefono) >= 7

def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras y espacios"""
    return all(c.isalpha() or c.isspace() for c in nombre) and nombre.strip()
