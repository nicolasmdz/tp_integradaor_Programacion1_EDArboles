# Trabajo Integrador – Programación I
# Árbol Binario con Listas Anidadas - Simulación de Inventario de Ferretería
# Alumno: Nicolás Monaco
# Comisión: 17


# === FUNCIONES PRINCIPALES PARA ÁRBOL BINARIO ===

def crear_nodo(nombre, stock, precio):
    return [nombre, stock, precio, [], []]  # [nombre, stock, precio, hijo_izq, hijo_der]

def insertar_hijoizq(raiz, nombre, stock, precio):
    t = raiz[3]
    if t:
        raiz[3] = [nombre, stock, precio, t, []]
    else:
        raiz[3] = [nombre, stock, precio, [], []]

def insertar_hijoder(raiz, nombre, stock, precio):
    t = raiz[4]
    if t:
        raiz[4] = [nombre, stock, precio, [], t]
    else:
        raiz[4] = [nombre, stock, precio, [], []]

def mostrar_arbol(nodo, nivel=0):
    if nodo:
        print("  " * nivel + f"- {nodo[0]} (stock: {nodo[1]}, precio: ${nodo[2]})")
        mostrar_arbol(nodo[3], nivel + 1)
        mostrar_arbol(nodo[4], nivel + 1)

def recorrido_preorden(nodo):
    if nodo:
        print(nodo[0])
        recorrido_preorden(nodo[3])
        recorrido_preorden(nodo[4])

def recorrido_inorden(nodo):
    if nodo:
        recorrido_inorden(nodo[3])
        print(nodo[0])
        recorrido_inorden(nodo[4])

def recorrido_postorden(nodo):
    if nodo:
        recorrido_postorden(nodo[3])
        recorrido_postorden(nodo[4])
        print(nodo[0])

# === CREACIÓN INICIAL DEL ÁRBOL ===

raiz = crear_nodo("Ferretería", 0, 0)

# Cargar nodos manualmente
insertar_hijoizq(raiz, "Herramientas", 0, 0)
insertar_hijoder(raiz, "Materiales", 0, 0)

insertar_hijoizq(raiz[3], "Llave Inglesa", 15, 1200)
insertar_hijoder(raiz[3], "Sierra", 8, 950)

insertar_hijoizq(raiz[4], "Tornillo", 10, 1100)
insertar_hijoder(raiz[4], "Pintura blanca", 25, 3000)

# === VISUALIZACIÓN INICIAL ===

print("\nÁrbol generado:")
mostrar_arbol(raiz)

print("\nRecorrido preorden:")
recorrido_preorden(raiz)

print("\nRecorrido inorden:")
recorrido_inorden(raiz)

print("\nRecorrido postorden:")
recorrido_postorden(raiz)

# === INGRESO DINÁMICO DE PRODUCTOS DESDE CONSOLA ===

def agregar_hijo_izq(raiz, nuevo_nodo):
    if raiz[3]:
        nuevo_nodo[3] = raiz[3]
    raiz[3] = nuevo_nodo

def agregar_hijo_der(raiz, nuevo_nodo):
    if raiz[4]:
        nuevo_nodo[4] = raiz[4]
    raiz[4] = nuevo_nodo

while True:
    nombre = input("\nNombre del producto o categoría (FIN para terminar): ")
    if nombre.upper() == "FIN":
        break
    tipo = input("¿Es categoría o producto?: ").lower()

    if tipo == "producto":
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
        except ValueError:
            print("Error: precio y stock deben ser numéricos.")
            continue
        nuevo = crear_nodo(nombre, stock, precio)
    else:
        nuevo = crear_nodo(nombre, 0, 0)

    lado = input("¿Insertar a la izquierda (i) o derecha (d) de la raíz?: ").lower()
    if lado == "i":
        agregar_hijo_izq(raiz, nuevo)
    else:
        agregar_hijo_der(raiz, nuevo)

# === MOSTRAR RESULTADO FINAL ===

print("\nÁrbol final:")
mostrar_arbol(raiz)
