#Generar una lista aleatoria con valores aleatorios

from random import randint

lista_aleatoria= []

#Solicitar cuántos valores necesita
elementos = input('¿Cuantos elementos necesitas?')
elementos = int(elementos)

contador = 1

while contador <= elementos:
    #Generamos un número aleatorio:
    matriz = randint(1, 100)
    #Número aleatorio lo multiplicamos por el número dado por el usuario:
    valor = matriz * elementos
    #Guardar valor aleatorio en la lista:
    lista_aleatoria.append(valor)
    #Sumar valor a contador para la siguiente vuelta:
    contador = contador + 1

print(lista_aleatoria)






