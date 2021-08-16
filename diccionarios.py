def run():
    # my_dictionary = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    #     'llave4': 4,
    # }
    
    # print(my_dictionary['llave1'])
    # print(my_dictionary['llave2'])
    # print(my_dictionary['llave3'])
    # print(my_dictionary['llave4'])

    poblacion_paises = {
        'Argentina': 44940000,
        'Brasil': 211000000,
        'Ecuador':17370000,
        'USA': 328200000,
    }

    # for pais in poblacion_paise.keys():
    #     print(pais)
    
    # for pais in poblacion_paise.values():
    #     print(pais)
    
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene una población de: ' + str(poblacion) + ' habitantes')


if __name__ == ('__main__'):
    run()