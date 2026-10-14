'''
ALGORITMO SUMA N PRIMEROS NUMEROS
Funcion suma <- sumar_hasta_n(n)
    Definir suma, contador Como Entero
    
    suma <- 0
    contador <- 1
    
    Mientras contador <= n Hacer
        suma <- suma + contador
        contador <- contador + 1
    FinMientras
FinFuncion

Algoritmo Principal
    Definir n, resultado Como Entero
    
    Escribir "Ingrese un número: "
    Leer n
    
    resultado <- sumar_hasta_n(n)
    
    Escribir "La suma de los números desde 1 hasta ", n, " es: ", resultado
FinAlgoritmo'''


def sumar_hasta_n(n):
    suma = 0
    contador = 1

    while contador <= n:
        suma = suma + contador
        contador = contador + 1
    return suma

n = int(input("Ingrese un número: "))

resultado = sumar_hasta_n(n)
print("La suma de los números desde 1 hasta", n, "es:", resultado)
