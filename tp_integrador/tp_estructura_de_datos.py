# Definimos una función para crear un "nodo" del árbol binario.
# Un nodo representa un producto y almacena su nombre, cantidad en stock y precio.
# Además, contiene dos espacios vacíos para los hijos izquierdo y derecho del árbol.
def binary_tree(product_name, stock, price):
    return [product_name, stock, price, [], []]  # Lista con el nombre del producto, stock y precio, más dos listas vacías (hijos)

# Función para insertar un nuevo producto en el lado IZQUIERDO del árbol.
def insert_left(root, product_name, stock, price):
    t = root[3]  # Obtenemos el hijo izquierdo actual.
    if t:  # Si ya existe un hijo izquierdo, lo desplazamos hacia abajo y agregamos el nuevo producto arriba.
        root[3] = [product_name, stock, price, t, []]
    else:  # Si el espacio está vacío, simplemente agregamos el nuevo producto.
        root[3] = [product_name, stock, price, [], []]
    return root

# Función para insertar un nuevo producto en el lado DERECHO del árbol.
def insert_right(root, product_name, stock, price):
    t = root[4]  # Obtenemos el hijo derecho actual.
    if t:  # Si ya existe un hijo derecho, lo desplazamos hacia abajo y agregamos el nuevo producto arriba.
        root[4] = [product_name, stock, price, [], t]
    else:  # Si el espacio está vacío, simplemente agregamos el nuevo producto.
        root[4] = [product_name, stock, price, [], []]
    return root

# Función para obtener la cantidad en stock de un producto dado.
def get_stock(root):
    return root[1]  # Devolvemos el valor del stock almacenado en la posición 1 de la lista.

# Función para actualizar el stock de un producto específico.
def update_stock(root, new_stock):
    root[1] = new_stock  # Modificamos el valor del stock con el nuevo número.

# Función para obtener el precio de un producto.
def get_price(root):
    return root[2]  # Devolvemos el precio almacenado en la posición 2 de la lista.

# Función para actualizar el precio de un producto.
def update_price(root, new_price):
    root[2] = new_price  # Modificamos el precio con el nuevo valor.

# Función para obtener el hijo izquierdo de un nodo del árbol.
def get_left_child(root):
    return root[3] if root[3] else None  # Retorna el hijo izquierdo si existe, sino retorna "None" (vacío).

# Función para obtener el hijo derecho de un nodo del árbol.
def get_right_child(root):
    return root[4] if root[4] else None  # Retorna el hijo derecho si existe, sino retorna "None".

# ----------------- EJEMPLO DE USO -----------------

# Creamos la "categoría principal" del árbol: Electrónicos (sin stock ni precio inicial).
almacen = binary_tree("Electrónicos", 0, 0)

# Insertamos dos productos dentro de la categoría principal:
insert_left(almacen, "Laptop", 10, 800)  # Agrega una Laptop al lado izquierdo.
insert_right(almacen, "Smartphone", 15, 600)  # Agrega un Smartphone al lado derecho.
insert_left(almacen,"consolas",20,100)
insert_right(almacen,"camaras",100,5)
# Agregamos más productos dentro de los existentes.
insert_left(get_left_child(almacen), "Accesorios Laptop", 20, 50)  # Accesorios para laptop en el lado izquierdo de Laptop.
insert_right(get_right_child(almacen), "Fundas Smartphone", 25, 20)  # Fundas para smartphone en el lado derecho de Smartphone.
insert_left(get_left_child(almacen), "joestick", 20, 50)
insert_right(get_right_child(almacen), "Fundas Smartphone", 25, 20)
# Mostramos la cantidad de stock de un producto específico.
print(f"Stock de Laptop: {get_stock(get_left_child(almacen))}")  # Devuelve "10"

# Actualizamos el stock de Laptop y lo volvemos a mostrar.
update_stock(get_left_child(almacen), 8)  # Modificamos el stock de la Laptop a 8 unidades.
print(f"Stock actualizado de Laptop: {get_stock(get_left_child(almacen))}")  # Devuelve "8"

# Función para recorrer el árbol binario en preorden (Raíz -> Izquierdo -> Derecho)
def recorrido_preorden(raiz):
    if raiz:  # Verificamos si el nodo no está vacío
        print(f"Producto: {raiz[0]}  , Stock: {raiz[1]}, Precio: {raiz[2]}")  # Mostramos el nodo actual
        recorrido_preorden(raiz[3])  # Recorremos el hijo izquierdo
        recorrido_preorden(raiz[4])  # Recorremos el hijo derecho


# Función para recorrer el árbol en orden (Izquierdo -> Raíz -> Derecho)
def recorrido_inorden(raiz):
    if raiz:
        recorrido_inorden(raiz[3])  # Recorremos el hijo izquierdo
        print(f"Producto: {raiz[0]} , Stock: {raiz[1]}, Precio: {raiz[2]}")  # Mostramos el nodo actual
        recorrido_inorden(raiz[4])  # Recorremos el hijo derecho

# Función para recorrer el árbol en postorden (Izquierdo -> Derecho -> Raíz)
def recorrido_postorden(raiz):
    if raiz:
        recorrido_postorden(raiz[3])  # Recorremos el hijo izquierdo
        recorrido_postorden(raiz[4])  # Recorremos el hijo derecho
        print(f"Producto: {raiz[0]} , Stock: {raiz[1]}  , Precio: {raiz[2]}")  # Mostramos el nodo actual

print("Recorrido en preorden:")
recorrido_preorden(almacen)

print("Recorrido en inorden:")
recorrido_inorden(almacen)

print("Recorrido en postorden:")
recorrido_postorden(almacen)