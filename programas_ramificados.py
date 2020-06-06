nombre1 = (input('ingresa tu nombre: '))
edad1 = int(input('ingresa tu edad: '))
nombre2 = (input('ingresa el nombre de tu hermano: '))
edad2 = int(input('ingresa la edad de tu hermano: '))

if edad1 > edad2:
    print(f'vos  {nombre1} sos mayor que {nombre2}')
elif edad2 > edad1:
    print(f'tu hermano {nombre2} es mayor que vos {nombre1}')
else:
    print(f'{nombre1} y {nombre2} tienen la misma edad')
