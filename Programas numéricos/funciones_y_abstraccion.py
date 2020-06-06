objetivo = int(input('Escoge un numero: '))
opcion = int(input('Seleccione el tipo de algoritmo a usar:\n 1 - Enumeracion exustiva\n 2 - Aproximacion de Soluciones\n 3 - Busqueda Binaria\n-> '))

respueta = 0.0
epsilon = 0.0

def busquedaBinaria(Objetivo, Epsilon):
	bajo = 0.0
	alto = max(1.0, Objetivo)
	respuesta = (alto + bajo) / 2

	while abs(respuesta**2 - Objetivo) >= Epsilon:
		if respuesta**2 < Objetivo:
			bajo = respuesta
		else:
			alto = respuesta

		respuesta = (alto + bajo) / 2

	print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def aproximacionSoluciones(Objetivo, Epsilon):
	respuesta = 0.0
	paso = Epsilon**2

	while abs(respuesta**2 - Objetivo) >= Epsilon and respuesta <= Objetivo:
			respuesta += paso

	if abs(respuesta**2 - Objetivo) >= Epsilon:
		print(f'No se encontro raiz cuadrada del objetivo')
	else:
		print(f'La raiz cuadrada de {Objetivo} es {respuesta}')


def enumeracionExaustiva(Objetivo):
	respuesta = 0

	while respuesta**2 < Objetivo:
		respuesta += 1
	if respuesta**2 == Objetivo:
		print(f'La raiz cuadrada de {Objetivo} es {respuesta}')
	else:
		print(f'{Objetivo} no tiene una raiz cuadrada exacta')

if(opcion == 1):
	enumeracionExaustiva(objetivo)
elif (opcion == 2):
	epsilon = float(input('Introduzca el porcentage decimal de error respecto al real: '))
	aproximacionSoluciones(objetivo, epsilon)
elif(opcion == 3):
	epsilon = float(input('Introduzca el porcentage decimal de error respecto al real: '))
	busquedaBinaria(objetivo, epsilon)
else:
	print(f'La opcion {opcion} esta fuera de rango, escoja una opcion del numero valido.')
