# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False


# def run():
#     numero = int(input('Escribe un número: '))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')
    


# if __name__ == ('__main__'):
#     run()
menu = print('''Ingresa un número y verificaremos si es primo o no es primo
''')

def primo(num):
    num -= 1
    count = 1
    while num > 1:
        count *= num
        num -= 1
    return count

def run():
    num = int(input('Escribe un número: '))
    fac = primo(num)
    fac += 1
    
    if fac % num == 0:
        print(f'El número {num} es primo')
    else:
        print('No es primo')
    
    

if __name__ == ('__main__'):
    run()


