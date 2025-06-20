class Producto:
    # Constructor de la clase Producto.
    # Inicializa un producto con nombre, precio y stock.
    # Si el stock no se proporciona, se asume 0.
    # Si el stock es menor a 0, se asigna 0.
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre  # El nombre del producto es privado.
        self.__precio = precio  # El precio del producto es privado.
        # El stock del producto es privado y se valida para no ser negativo.
        self.__stock = stock if stock >= 0 else 0

    # Método getter para obtener el nombre del producto.
    @property
    def nombre(self):
        return self.__nombre

    # Método getter para obtener el precio del producto.
    @property
    def precio(self):
        return self.__precio

    # Método getter para obtener el stock del producto.
    @property
    def stock(self):
        return self.__stock

    # Método setter para modificar el stock del producto.
    # Si el nuevo stock es menor a 0, se asigna 0.
    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock if nuevo_stock >= 0 else 0

    # Método para representar el objeto Producto como una cadena.
    # Útil para imprimir el producto de forma legible.
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

    # Sobrecarga del operador de igualdad (==).
    # Dos productos se consideran iguales si tienen el mismo nombre (ignorando mayúsculas/minúsculas).
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre.lower() == other.nombre.lower()
        return False

    # Sobrecarga del operador de suma (+).
    # Cuando se suman dos productos, se devuelve un nuevo producto con el stock combinado.
    # Se conserva el nombre y precio del primer producto.
    def __add__(self, other):
        if isinstance(other, Producto):
            # Se crea un nuevo producto con el nombre y precio del producto actual,
            # y el stock sumado al del otro producto.
            return Producto(self.nombre, self.precio, self.stock + other.stock)
        return NotImplemented

    # Sobrecarga del operador de resta (-).
    # Cuando se resta stock de un producto, se devuelve un nuevo producto con el stock ajustado.
    # El stock resultante no puede ser negativo.
    def __sub__(self, cantidad):
        if isinstance(cantidad, int) or isinstance(cantidad, float):
            nuevo_stock = self.stock - cantidad
            # El stock no puede ser menor a 0.
            return Producto(self.nombre, self.precio, nuevo_stock if nuevo_stock >= 0 else 0)
        return NotImplemented