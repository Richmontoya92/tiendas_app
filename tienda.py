from abc import ABC, abstractmethod # Importa ABC y abstractmethod para clases abstractas
from producto import Producto # Importa la clase Producto

# Clase abstracta Tienda, sirve como base para los diferentes tipos de tiendas.
# Define la interfaz común que todas las tiendas deben implementar.
class Tienda(ABC):
    # Constructor de la clase Tienda.
    # Inicializa una tienda con nombre y costo de delivery.
    # El listado de productos se inicializa vacío.
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre  # El nombre de la tienda es privado.
        self.__costo_delivery = costo_delivery  # El costo de delivery es privado.
        self.__productos = []  # La lista de productos es privada.

    # Método getter para obtener el nombre de la tienda.
    @property
    def nombre(self):
        return self.__nombre

    # Método getter para obtener el costo de delivery de la tienda.
    @property
    def costo_delivery(self):
        return self.__costo_delivery

    # Método abstracto para ingresar un producto.
    # Las subclases deben implementar su lógica específica.
    @abstractmethod
    def ingresar_producto(self, producto):
        pass

    # Método abstracto para listar los productos.
    # Las subclases deben implementar su lógica específica de visualización.
    @abstractmethod
    def listar_productos(self):
        pass

    # Método abstracto para realizar una venta.
    # Las subclases deben implementar su lógica específica de venta y validación.
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

    # Método para encontrar un producto por su nombre en la lista de productos de la tienda.
    # Retorna el objeto Producto si lo encuentra, de lo contrario None.
    def _encontrar_producto(self, nombre_producto):
        for p in self.__productos:
            if p.nombre.lower() == nombre_producto.lower():
                return p
        return None

    # Método para añadir o actualizar un producto en la lista de la tienda.
    # Si el producto ya existe, actualiza su stock. Si no, lo añade.
    def _add_or_update_producto(self, nuevo_producto):
        producto_existente = self._encontrar_producto(nuevo_producto.nombre)
        if producto_existente:
            # Si el producto ya existe, actualiza su stock sumando el nuevo stock.
            producto_existente.stock += nuevo_producto.stock
        else:
            # Si el producto no existe, lo añade a la lista.
            self.__productos.append(nuevo_producto)

    # Método getter para la lista de productos (privado, solo para uso interno de las subclases).
    @property
    def _productos(self):
        return self.__productos


# Clase Restaurante, hereda de Tienda.
class Restaurante(Tienda):
    # Constructor de Restaurante. Llama al constructor de la clase base (Tienda).
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    # Implementación del método abstracto ingresar_producto para Restaurante.
    # Los productos de restaurante siempre se añaden con stock 0.
    def ingresar_producto(self, producto):
        # Asegura que el stock del producto sea 0 para los restaurantes.
        producto.stock = 0
        # Añade o actualiza el producto en la lista interna.
        self._add_or_update_producto(producto)
        print(f"Producto '{producto.nombre}' ingresado en {self.nombre} (stock: {producto.stock}).")

    # Implementación del método abstracto listar_productos para Restaurante.
    # Oculta el stock de los productos.
    def listar_productos(self):
        productos_str = f"Productos en {self.nombre} (Restaurante):\n"
        if not self._productos:
            productos_str += "  No hay productos disponibles.\n"
        else:
            for p in self._productos:
                # El stock se oculta para Restaurantes.
                productos_str += f"  - {p.nombre}: ${p.precio}\n"
        return productos_str

    # Implementación del método abstracto realizar_venta para Restaurante.
    # No valida stock ya que siempre es 0.
    def realizar_venta(self, nombre_producto, cantidad):
        producto = self._encontrar_producto(nombre_producto)
        if producto:
            # No se necesita validación de stock ni modificación para Restaurantes.
            print(f"Venta de {cantidad} unidades de '{nombre_producto}' realizada en {self.nombre}.")
            return True
        else:
            print(f"Producto '{nombre_producto}' no encontrado en {self.nombre}.")
            return False


# Clase Supermercado, hereda de Tienda.
class Supermercado(Tienda):
    # Constructor de Supermercado. Llama al constructor de la clase base (Tienda).
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    # Implementación del método abstracto ingresar_producto para Supermercado.
    # Añade o actualiza el producto normalmente.
    def ingresar_producto(self, producto):
        self._add_or_update_producto(producto)
        print(f"Producto '{producto.nombre}' ingresado en {self.nombre} (stock: {producto.stock}).")

    # Implementación del método abstracto listar_productos para Supermercado.
    # Muestra un mensaje especial si el stock es bajo.
    def listar_productos(self):
        productos_str = f"Productos en {self.nombre} (Supermercado):\n"
        if not self._productos:
            productos_str += "  No hay productos disponibles.\n"
        else:
            for p in self._productos:
                stock_info = f"Stock: {p.stock}"
                if p.stock < 10:
                    stock_info += " (Pocos productos disponibles)" # Mensaje si el stock es bajo.
                productos_str += f"  - {p.nombre}: ${p.precio}, {stock_info}\n"
        return productos_str

    # Implementación del método abstracto realizar_venta para Supermercado.
    # Valida el stock existente antes de la venta.
    def realizar_venta(self, nombre_producto, cantidad):
        producto = self._encontrar_producto(nombre_producto)
        if producto:
            if producto.stock == 0:
                print(f"No hay stock de '{nombre_producto}' en {self.nombre}.")
                return False
            if producto.stock < cantidad:
                # Si la cantidad solicitada es mayor al stock, vende lo disponible.
                print(f"Solo se venderán {producto.stock} unidades de '{nombre_producto}' (stock insuficiente).")
                producto.stock = 0
                print(f"Venta de {producto.stock} unidades de '{nombre_producto}' realizada en {self.nombre}.")
                return True
            else:
                # Reduce el stock en la cantidad vendida.
                producto.stock -= cantidad
                print(f"Venta de {cantidad} unidades de '{nombre_producto}' realizada en {self.nombre}.")
                return True
        else:
            print(f"Producto '{nombre_producto}' no encontrado en {self.nombre}.")
            return False


# Clase Farmacia, hereda de Tienda.
class Farmacia(Tienda):
    # Constructor de Farmacia. Llama al constructor de la clase base (Tienda).
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    # Implementación del método abstracto ingresar_producto para Farmacia.
    # Añade o actualiza el producto normalmente.
    def ingresar_producto(self, producto):
        self._add_or_update_producto(producto)
        print(f"Producto '{producto.nombre}' ingresado en {self.nombre} (stock: {producto.stock}).")

    # Implementación del método abstracto listar_productos para Farmacia.
    # Oculta el stock y añade mensaje de envío gratis para productos caros.
    def listar_productos(self):
        productos_str = f"Productos en {self.nombre} (Farmacia):\n"
        if not self._productos:
            productos_str += "  No hay productos disponibles.\n"
        else:
            for p in self._productos:
                precio_info = f"${p.precio}"
                if p.precio > 15000:
                    precio_info += " (Envío gratis al solicitar este producto)" # Mensaje de envío gratis.
                # El stock se oculta para Farmacias.
                productos_str += f"  - {p.nombre}: {precio_info}\n"
        return productos_str

    # Implementación del método abstracto realizar_venta para Farmacia.
    # Valida stock y la cantidad máxima de venta por producto.
    def realizar_venta(self, nombre_producto, cantidad):
        producto = self._encontrar_producto(nombre_producto)
        if producto:
            if producto.stock == 0:
                print(f"No hay stock de '{nombre_producto}' en {self.nombre}.")
                return False
            if cantidad > 3: # Validación específica de Farmacia: no más de 3 unidades por venta.
                print(f"En Farmacia no se puede solicitar una cantidad superior a 3 por producto.")
                return False
            if producto.stock < cantidad:
                # Si la cantidad solicitada es mayor al stock, vende lo disponible.
                print(f"Solo se venderán {producto.stock} unidades de '{nombre_producto}' (stock insuficiente).")
                producto.stock = 0
                print(f"Venta de {producto.stock} unidades de '{nombre_producto}' realizada en {self.nombre}.")
                return True
            else:
                # Reduce el stock en la cantidad vendida.
                producto.stock -= cantidad
                print(f"Venta de {cantidad} unidades de '{nombre_producto}' realizada en {self.nombre}.")
                return True
        else:
            print(f"Producto '{nombre_producto}' no encontrado en {self.nombre}.")
            return False