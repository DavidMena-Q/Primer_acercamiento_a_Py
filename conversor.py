menu = '''
Conversor de monedas con fecha 2021 ©

1 - Euro
2 - Libra Esterlina
3 - Franco Suizo 

Elige una opción: '''

def conversor(moneda, coin):
    dolar = float(input('Escriba cantidad de dólares: '))
    moneda = dolar * moneda
    moneda = str(round(moneda, 2))
    print('Tus dólares equivalen a: ' + moneda + coin)
   

opcion = int(input(menu))

if opcion == 1:
    conversor(1.18, ' Euros')
    
elif opcion == 2:
    conversor(1.39, ' Libras Esterlinas')
     
elif opcion == 3:
    conversor(1.09,' Francos Suizos')

else:
    print('No existe esta opción')
   

# elif opcion == 2:
#     dolar = float(input('Escribe la cantidad de dólares: '))
#     valor_libra = 1.39
#     libra = dolar * valor_libra
#     libra = str(libra)
#     print('Tus dólares equivalen a: ' + libra + ' Libras Esterlinas.')
# elif opcion == 3:
#     dolar = float(input('Escribe la cantidad de dólares: '))
#     valor_franco = 1.09
#     franco = dolar * valor_franco
#     franco = str(franco)
#     print('Tus dólares equivalen a: ' + franco + ' Francos Suizos.')
# else:
#     print('No existe esa opción')








