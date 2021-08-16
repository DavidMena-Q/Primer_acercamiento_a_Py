# def factorial(num):
#     '''Obtener la factorial del número que registres
#     num int > 0
#     return n!  
#     '''
#     print(num)
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)

# num = int(input('Escribe un número int: '))


# print(factorial(num))
def fibo(num):
    '''Realizar la suceción de finacci con relación a pasos
    num int > 0
    return n...
    '''
    if num == 1 or num == 0:
        return 1
    return fibo(num - 1) + fibo(num - 2)

num = int(input('Escribe un entero: '))
print(f'{num} es {fibo(num)}')



