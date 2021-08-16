# def run():
#     # nombre = input('Dime tu nombre: ')
#     # for pi in nombre:
#     #     print(pi)
#     frase = input('Escriba frase: ')
#     for c in frase:
#         print(c.upper())




# if __name__ == ('__main__'):
#     run()
def run():
    cadena = input('Ingresa la cadena: ')
    cadena2 = ''
    cadena3 = ''
    for i in cadena:
        cadena2 += i * 2 
        cadena3 += i * 3
    print('cadena = ', cadena[::-1])
    print('cadena2 =', cadena2)
    print('cadena3 = ', cadena3[9:1:-2])

if __name__ == "__main__":
    run()
