#Importamos las librerias a utilizar.
import random
import time

#Datos base ficticios (evitar crear una base de datos manualmente)
nombres = ["Lucía", "Tomás", "María", "Juan", "Sofía", "Mateo", "Camila", "Agustín", "Valentina", "Benjamín","Pedro","Jaime","Lucas","Sandra","Esteban","Ezequiel","Milagros"]
apellidos = ["González", "Rodríguez", "Pérez", "Fernández", "López", "Martínez", "García", "Sánchez", "Romero", "Torres","Oviedo","Santillan","Escudero","Felice","Herrera"]
deportes = ["Fútbol", "Básquet", "Natación", "Tenis", "Atletismo", "Vóley", "Hockey", "Handball","Rugby"]

#Con los datos base anterior creamos una funcion para generar deportistas utilizando 'random'.
def generar_deportistas(cantidad):
    deportistas = []
    for i in range(1, cantidad + 1):
        deportista = {
            "id": i,
            "dni": random.randint(10000000, 50000000),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "edad": random.randint(12, 60),
            "deporte": random.choice(deportes)
        }
        deportistas.append(deportista)
    return deportistas

# Definimos una funcion para la medición de tiempo utilizando la libreria 'time'.
def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

# Creamos 4 funciones de ordenamientos por 'TimSort' (combina MergeSort e InsertionSort)
def ordenar_por_apellido(lista): return sorted(lista, key=lambda x: x["apellido"])
def ordenar_por_edad(lista): return sorted(lista, key=lambda x: x["edad"])
def ordenar_por_deporte(lista): return sorted(lista, key=lambda x: x["deporte"])
def ordenar_por_dni(lista): return sorted(lista, key=lambda x: x["dni"])

#Creamos una funcion de Bubble Sort (edad).
def bubble_sort_por_edad(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["edad"] > lista[j + 1]["edad"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Funcion de busqueda lineales por DNI
def buscar_por_dni_lineal(lista, dni_buscado):
    for deportista in lista:
        if deportista["dni"] == dni_buscado:
            return deportista
    return None
#Funcion de busqueda binaria por DNI
def buscar_por_dni_binaria(lista_ordenada, dni_buscado):
    izquierda, derecha = 0, len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio]["dni"] == dni_buscado:
            return lista_ordenada[medio]
        elif lista_ordenada[medio]["dni"] < dni_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None
#Funcion de busqueda lineal por deporte.
def buscar_por_deporte(lista, deporte_buscado):
    return [d for d in lista if d["deporte"].lower() == deporte_buscado.lower()]

# Funcion para mostrar en pantalla la lista generada aleatoriamente.
def mostrar_lista(lista):
    for d in lista:
        print(f"{d['id']:02d} | {d['dni']} | {d['nombre']} {d['apellido']} | Edad: {d['edad']} | Deporte: {d['deporte']}")

# Funcion para crear el menú interactivo que se vera en pantalla.
# Primeramente ordenamos la lista por dni, ya que lo requeriremos para nuestra busqueda binaria; y es recomendable tenerla ordenada primeramente
# para no tener que ordenarla cada vez que el usuario elige esa opcion dentro del ciclo.

def menu(deportistas):
    deportistas_ordenados_dni = ordenar_por_dni(deportistas)
    continuar = True

    while continuar:
        print("\n=== MENÚ DEL SISTEMA DEPORTIVO ===")
        print("1. Mostrar lista original")
        print("2. Ordenar por apellido")
        print("3. Ordenar por edad ('TimSort')")
        print("4. Ordenar por edad ('BubbleSort')")
        print("5. Ordenar por deporte") 
        print("6. Buscar por DNI (Lineal)")
        print("7. Buscar por DNI (Binaria)")
        print("8. Buscar por deporte")
        print("9. Salir")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print("\n LISTA ORIGINAL")
            mostrar_lista(deportistas)

        elif opcion == "2":
            lista_ordenada, tiempo = medir_tiempo(ordenar_por_apellido, deportistas)
            print("\n ORDENADA POR APELLIDO")
            mostrar_lista(lista_ordenada)
            print(f" Tiempo: {tiempo:.6f} segundos")

        elif opcion == "3":
            lista_ordenada, tiempo = medir_tiempo(ordenar_por_edad, deportistas)
            print("\n ORDENADA POR EDAD ('TimSort')")
            mostrar_lista(lista_ordenada)
            print(f" Tiempo: {tiempo:.6f} segundos")

        elif opcion == "4":
            lista_ordenada, tiempo = medir_tiempo(bubble_sort_por_edad, deportistas)
            print("\n ORDENADA POR EDAD (BubbleSort)")
            mostrar_lista(lista_ordenada)
            print(f" Tiempo: {tiempo:.6f} segundos")

        elif opcion == "5":
            lista_ordenada, tiempo = medir_tiempo(ordenar_por_deporte, deportistas)
            print("\n ORDENADA POR DEPORTE")
            mostrar_lista(lista_ordenada)
            print(f" Tiempo: {tiempo:.6f} segundos")

        elif opcion == "6":
            try:
                dni = int(input("Ingresá el DNI a buscar: "))
                resultado, tiempo = medir_tiempo(buscar_por_dni_lineal, deportistas, dni)
                print("\n Resultado:" if resultado else "ERROR: No encontrado.")
                if resultado: print(resultado)
                print(f" Tiempo: {tiempo:.6f} segundos")
            except ValueError:
                print("DNI inválido.")

        elif opcion == "7":
            try:
                dni = int(input("Ingresá el DNI a buscar: "))
                resultado, tiempo = medir_tiempo(buscar_por_dni_binaria, deportistas_ordenados_dni, dni)
                print("\n Resultado:" if resultado else " No encontrado.")
                if resultado: print(resultado)
                print(f" Tiempo: {tiempo:.6f} segundos")
            except ValueError:
                print(" DNI inválido.")

        elif opcion == "8":
            deporte = input("Ingresá el deporte a buscar: ")
            resultados, tiempo = medir_tiempo(buscar_por_deporte, deportistas, deporte)
            if resultados:
                print(f"\n Deportistas en {deporte.title()}:")
                mostrar_lista(resultados)
            else:
                print(" No se encontraron deportistas con ese deporte.")
            print(f" Tiempo: {tiempo:.6f} segundos")

        elif opcion == "9":
            print(" Saliendo del sistema.")
            continuar = False
        else:
            print(" Opción inválida.")

# Ejecutación de las funciones 'generar_deportistas' y 'menu' que tendran todo el resto del proceso anidado.
deportistas = generar_deportistas(30)
menu(deportistas)

