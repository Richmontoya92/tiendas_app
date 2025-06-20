from tienda import Restaurante, Supermercado, Farmacia # Importa las clases de tienda
from producto import Producto # Importa la clase Producto

# Función para crear una nueva tienda basada en la elección del usuario.
def crear_tienda():
    while True:
        nombre_tienda = input("Ingrese el nombre de la tienda: ").strip()
        if nombre_tienda:
            break
        else:
            print("El nombre de la tienda no puede estar vacío.")

    while True:
        try:
            costo_delivery = float(input("Ingrese el costo de delivery: "))
            if costo_delivery >= 0:
                break
            else:
                print("El costo de delivery no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número para el costo de delivery.")

    while True:
        print("\nSeleccione el tipo de tienda:")
        print("1. Restaurante")
        print("2. Supermercado")
        print("3. Farmacia")
        tipo = input("Ingrese el número de la opción: ").strip()

        if tipo == '1':
            return Restaurante(nombre_tienda, costo_delivery)
        elif tipo == '2':
            return Supermercado(nombre_tienda, costo_delivery)
        elif tipo == '3':
            return Farmacia(nombre_tienda, costo_delivery)
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Función para ingresar productos a la tienda seleccionada.
def ingresar_productos_a_tienda(tienda):
    while True:
        respuesta = input("¿Desea ingresar un producto? (s/n): ").lower().strip()
        if respuesta == 'n':
            break
        elif respuesta == 's':
            while True:
                nombre_producto = input("Ingrese el nombre del producto: ").strip()
                if nombre_producto:
                    break
                else:
                    print("El nombre del producto no puede estar vacío.")

            while True:
                try:
                    precio_producto = float(input("Ingrese el precio del producto: "))
                    if precio_producto >= 0:
                        break
                    else:
                        print("El precio del producto no puede ser negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número para el precio.")

            while True:
                try:
                    stock_input = input("Ingrese el stock del producto (dejar vacío para 0): ").strip()
                    stock_producto = int(stock_input) if stock_input else 0
                    if stock_producto >= 0:
                        break
                    else:
                        print("El stock del producto no puede ser negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para el stock.")

            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
        else:
            print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")

# Función principal del programa.
def main():
    tienda = crear_tienda()
    print(f"\nTienda '{tienda.nombre}' de tipo {type(tienda).__name__} creada con éxito.")

    ingresar_productos_a_tienda(tienda)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar productos existentes")
        print("2. Realizar una venta")
        print("3. Salir del programa")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            print(tienda.listar_productos())
        elif opcion == '2':
            nombre_producto_venta = input("Ingrese el nombre del producto a vender: ").strip()
            while True:
                try:
                    cantidad_venta = int(input("Ingrese la cantidad a vender: "))
                    if cantidad_venta > 0:
                        break
                    else:
                        print("La cantidad a vender debe ser un número positivo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
            tienda.realizar_venta(nombre_producto_venta, cantidad_venta)
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()