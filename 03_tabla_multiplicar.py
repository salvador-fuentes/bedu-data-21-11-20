#Script que calcula la tabla de multiplicar de un numero


#Solicitar numero al usuario por consola
numero = input('¿Que numero quieres multiplicar?')
#El dato ingresado por el usuario es una cadena "<str>"
#Se debe convertir a numero "<int>" para poder multiplicar
numero = int(numero)


for n in range(10):
    r= numero * (n+1)
    print(r)

# TAREA
# A continuación se muestra la tabla de multiplicar del número <numero>
# --------
# 8 * 1 = 8 
# 8 * 2 = 16
# 8 * 3 = 24  


