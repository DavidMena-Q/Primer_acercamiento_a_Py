# num_1 = int(input('Escoge un entero: '))
# num_2 = int(input('Escoge otro entero: '))

# if num_1 > num_2:
#     print('El primer número es mayor que el segundo')
# elif num_1 < num_2:
#     print('El primero es menor que el segundo')
# else:
#     print('Los dos son iguales')
# usuario_1 = input('Elige el nombre para el usuario 1: ')
# num_1 = int(input('Qué edad tiene el usuario 1: '))
# usuario_2 = input('Nombre usuario 2: ')
# num_2 = int(input('Que edad tiene el usuario 2: '))

# if num_1 > num_2:
#     print(f'{usuario_1} es mayor que {usuario_2}')
# elif num_1 < num_2:
#     print(f'{usuario_1} es menor que {usuario_2}')
# else:
#     print(f'{usuario_1} tiene la misma edad que {usuario_2}')


# Iteraciones

# count_interno = 0
# count_esterno = 0

# while count_esterno < 5:
#     while count_interno < 8:
#         print(count_esterno, count_interno)
#         count_interno += 1
#         if count_interno >= 3:
#             break
    
#     count_esterno +=1 
#     count_interno = 0



x = 0.0
for i in range(10):
    x += 0.1

# if x == 1.0:
if x < 1.0 and x > 0.9999999:
    print(f'x = {x}')
else:
    print(f'x != {x}')




