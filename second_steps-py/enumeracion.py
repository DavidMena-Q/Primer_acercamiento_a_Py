import time

objetivo = int(input('Escoge un número entero: '))
respuesta = 0
tiempo = time.time()

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

else:
    print(f'{objetivo} no tiene raíz cuadrada exacta')

print(f'El programa se demoró {time.time()-tiempo} segundos')