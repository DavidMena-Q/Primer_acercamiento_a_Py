menu = int(input('''"Métodos para buscar la raíz cuadrada"

método de enumeración = 1

método de aproximación = 2

método de busqueda binaria = 3

Elija el método:'''))

objetivo = int(input('Ingrese un número entero: '))
respuesta = 0
epsilon = 0.001

def enumeracion_exaustiva(respuesta):
        while respuesta**2 < objetivo:
            respuesta += 1
    
        if respuesta**2 == objetivo:
            print(f'La raíz cuadrada de {objetivo} es {respuesta}')

        else:
            print(f'{objetivo} no tiene raíz exacta')


def aproximacion(respuesta):
    paso = epsilon**2
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    respuesta = round(respuesta)
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


def b_binaria(respuesta):
    bajo = 0.0
    alto = max(1, objetivo)
    respuesta = (bajo + alto)/ 2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        
        if respuesta**2 > objetivo:
            alto = respuesta
        else:
            bajo = respuesta
        
        respuesta = (bajo + alto)/2

    respuesta = round(respuesta, 3)
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    

def run():
    if menu == 1:
        enumeracion_exaustiva(respuesta)
    
    elif menu == 2:
        aproximacion(respuesta)

    elif menu == 3:
        b_binaria(respuesta)
    
    else:
        print('Opción no válida')
        return run()


if __name__ == ('__main__'):
    run()