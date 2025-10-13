from utils import input_float, input_str

class CuentaCorriente:
    def __init__(self, dni, saldo=0, nombre=""):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.dni = dni
        self.nombre = nombre

        self.saldo = saldo

    def sacar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a sacar debe ser positiva")
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True

        return False

    def ingresar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser positiva")
        self.saldo += cantidad

    def __str__(self):
        return f"Cuenta: nombre: {self.nombre} dni: {self.dni} saldo:{self.saldo: .2f}€"

    def __eq__(self, other):
        return self.dni == other.dni

    def __lt__(self, other):
        return self.saldo < other.saldo

def main():
        try:
            dni = input_str("DNI: ")
            nombre = input_str("Nombre: ")
            saldo = input_float("Saldo inicial: ", min_val=0)

            cuenta = CuentaCorriente(dni, saldo, nombre)
            print(f"Cuenta creada: {cuenta}")

            while True:
                print("\n1. Ingresar")
                print("2. Sacar")
                print("3. Ver saldo")
                print("4. Salir")
            
                opcion = input_str("Opcion (1-4): ", opciones_validas=['1','2','3','4'])

                if opcion == '1':
                    cantidad = input_float("Cantidad a ingresar: ", min_val=0.01)
                    cuenta. ingresar_dinero(cantidad)
                    print("Ingreso realizado")

                elif opcion == '2':
                    cantidad = input_float("Cantidad a sacar: ", min_val=0.01)
                    if cuenta.sacar_dinero(cantidad):
                        print("Retiro realizado")
                    else:
                        print("Saldo insuficiente")

                elif opcion == '3':
                    print(cuenta)

                elif opcion == '4':
                    break
        except ValueError as e:
            print(f"Error: {e}")

if __name__== "_main_":
    main()