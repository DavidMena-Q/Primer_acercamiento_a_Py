
# from typing import List


# def divide_elementos_lista(lista, divisor):
#     try:
#         return [i / divisor for i in lista]
#     except ZeroDivisionError as e:
#         print(e)
#         return lista



# lista = list(range(10))
# divisor = 0

# print(divide_elementos_lista(lista, divisor))

print('Buscador de capitales')

pais = input('\nCuál capital de algún país deseas conocer?:')

def busca_pais(paises, pais):
    try:
        return paises[pais]
    except KeyError:
        return print('\n\nEn el país que buscas, no se encuentra en la base de datos')
    
paises = {
    'Argentina': 'Buenos Aires',
    'Bolivia':'La Paz',
    'Chile':'Santiago de Chile',
    'Uruguay':'Montevideo',
    'Paraguay':'Asuncion',
    'Perú':'Lima',
    'Brasil':'Brasilia',
    'Ecuador':'Quito',
    'Colombia':'Bogotá',
    'Venezuela':'Caracas',
    'Surinan':'Paramaribo',
    'Panamá':'Panamá',
    'México':'Ciudad de México',
    'República Dominicana':'Santo Domingo',
    'Haití':'Puerto Principe',
    'Cuba':'La Habana',
    'Estados Unidos':'Washington',
    'Canadá':'Otawwa',
    'España':'Madrid',
    'Portugal':'Lisboa',
    'Francia':'París',
    'Alemania':'Berlín',
    'Suiza':'Berna',
    'Italia':'Roma',
    'Grecia':'Atenas',
    'Bélgica':'Bruselas',
    'Paises Bajos':'Amsterdam',
    'Dinamarca':'Conpenhague',
    'Suecia':'Estocolmo',
    'Noruega':'Oslo',
    'Finlandia':'Helsinki',
    'Reino Unido':'Londres',
    'Irlanda':'Dublín',
    'Rusia':'Moscú',
    'Turquía':'Ankara',
    'Hungría':'Budapest',
    'Austria':'Viena',
    'Sudáfrica':'Pretoria',
    'Egipto':'El Cairo',
    'Marruecos':'Rabat',
    'Túnez':'Túnez',
    'Senegal':'Dakar',
    'Santo Tomé y Principe':'Santo Tomé',
    'Yibuti':'Yibuti',
    'Arabia Saudita':'Riad',
    'Emiratos Arabes Unidos':'Abu Dabi',
    'Qatar':'Doha',
    'Israel':'Jerusalen',
    'Líbano':'Beirut',
    'Irak':'Bagdad',
    'India':'Nueva Deli',
    'Nepal':'Katmandú',
    'Vietnan':'Hanói',
    'Tailandia':'Bangkok',
    'Filipinas':'Manila',
    'Indonesia':'Yakarta',
    'China':'Pekín',
    'Corea del Sur':'Seul',
    'Japón':'Tokio',
    'Singapur':'Singapur',
    'Malasia':'Kuala Lumpur',
    'Australia':'Camberra',
    'Nueva Zelanda':'Wellington',}

print(f'La capital de {pais} es {busca_pais(paises, pais)}')

