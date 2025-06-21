# Trabajo Integrador – Programación I  
## Árbol Binario con Listas Anidadas - Simulación de Inventario de Ferretería  

👤 **Alumno:** Nicolás Monaco  
🏫 **Comisión:** 17  
enlase al video: https://youtu.be/8rRGAn2pfP8
---

## 📌 Descripción  
Este proyecto implementa un sistema de inventario para una ferretería usando una estructura de **árbol binario con listas anidadas en Python**.  

Permite:  
- Crear una jerarquía de categorías y productos.  
- Ingresar productos o categorías dinámicamente desde consola.  
- Visualizar el árbol con indentación para reflejar la jerarquía.  
- Recorrer el árbol en Preorden, Inorden y Postorden.  

---

## ⚙️ Requisitos  
- Python 3.x (recomendado).  

---

## 🚀 Cómo ejecutar  
1. Cloná o descargá el repositorio.  
2. Abrí una terminal y navegá hasta la carpeta del proyecto.  
3. Ejecutá el archivo principal con:  
   ```bash
   python nombre_de_tu_archivo.py

# Trabajo Integrador – Programación I

### Árbol Binario con Listas Anidadas - Simulación de Inventario de Ferretería  
**Alumno:** Nicolás Monaco  
**Comisión:** 17  
**Docente:** Julieta Trape  
**Tutor:** David López  
**Fecha:** Junio 2025

---

## 1. Introducción

Este trabajo práctico implementa un sistema de inventario para una ferretería utilizando una estructura de **árbol binario con listas anidadas en Python**. Se utiliza un nodo raíz con categorías a izquierda y derecha, permitiendo agregar tanto **productos** como **subcategorías**.  

El árbol puede visualizarse jerárquicamente y recorrerse en forma preorden, inorden o postorden. Además, se permite el ingreso dinámico de productos o categorías desde consola.

---

## 2. Objetivos

- Comprender el funcionamiento de árboles binarios sin usar programación orientada a objetos (POO).  
- Usar listas anidadas para representar estructuras jerárquicas.  
- Aplicar funciones recursivas para mostrar y recorrer el árbol.  
- Simular un inventario real de ferretería con ingreso de datos dinámico.  

---

## 3. Marco Teórico

Un **árbol binario** es una estructura jerárquica donde cada nodo tiene hasta dos hijos: izquierdo y derecho. En este trabajo, se implementa cada nodo como una lista de cinco elementos:


[nombre, stock, precio, hijo_izquierdo, hijo_derecho]
Se construye con funciones que permiten insertar hijos, recorrer el árbol y mostrarlo visualmente.

4. Desarrollo
El programa define funciones para:

crear_nodo(nombre, stock, precio): crea un nodo con datos de producto o categoría.

insertar_hijoizq / insertar_hijoder: agregan nodos a izquierda o derecha de otro nodo.

mostrar_arbol: imprime el árbol con indentación según el nivel.

recorrido_preorden / inorden / postorden: imprimen los recorridos respectivos.

También se incluye una sección que permite ingresar productos o categorías desde la consola, eligiendo el lado en que se insertan respecto al nodo raíz.

5. Ejemplo de Ejecución Inicial
Estructura inicial creada manualmente:

- Ferretería
  - Herramientas
    - Llave Inglesa (stock: 15, precio: $1200)
    - Sierra (stock: 8, precio: $950)
  - Materiales
    - Tornillo (stock: 10, precio: $1100)
    - Pintura blanca (stock: 25, precio: $3000)
Recorrido Preorden:

Ferretería  
Herramientas  
Llave Inglesa  
Sierra  
Materiales  
Tornillo  
Pintura blanca
6. Ingreso Dinámico desde Consola
El programa permite ingresar nodos dinámicamente:

Si se trata de un producto, se ingresan nombre, stock y precio.

Si se trata de una categoría, se asignan stock y precio en 0.

Se elige si se inserta a la izquierda o derecha del nodo raíz.

Este sistema simula un inventario que puede expandirse según la necesidad del usuario.

7. Conclusión
El trabajo permitió aplicar estructuras no lineales para representar inventarios de forma lógica y visual. El uso de listas anidadas resultó funcional para construir árboles binarios sin recurrir a clases.

Se logró reforzar conceptos como:

Recursión

Estructuras condicionales

Representación jerárquica de datos

Interacción dinámica por consola

8. Mejoras Posibles
Reescribir con Programación Orientada a Objetos (POO) para mayor modularidad.

Implementar eliminación y modificación de nodos.

Agregar búsquedas por nombre o por características.

Guardar y cargar el árbol desde archivos.

Crear una interfaz visual con Tkinter o herramientas web.

9. Video Explicativo
🎥 Ver video explicativo del proyecto

10. Código Fuente Principal

def crear_nodo(nombre, stock, precio):
    return [nombre, stock, precio, [], []]

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
