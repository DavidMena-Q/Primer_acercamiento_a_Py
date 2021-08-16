# def potencia(numero, exponente):
#     if exponente > 0:
#         bandera = numero**exponente
#         bandera = str(bandera)
#         print('La potencia de {} a la {} es: {}'.format(numero, exponente, bandera))
#         exponente = exponente - 1
#     else:
#         print('OK')


# def run():
#     numero = float(input("Dame un número: "))
#     exponente = float(input("Dame una potencia: "))
#     potencia(numero, exponente)


# if __name__ == '__main__':
#     run()
    

def run():
    numero = int(input('Dame un número: '))
    exponente = int(input('Dame un exponente: '))
    while exponente > 0:
        bandera = numero ** exponente
        print(f'La potencia de {numero} elevado a la {exponente} es: {bandera}')
        exponente -= 1
    


if __name__ == '__main__':
    run()





    
