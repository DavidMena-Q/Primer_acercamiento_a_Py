print('''Qué tan bueno eres en matemática

Tienes 3 vidas si fallas se iran restando
''')


def run():
    # for count in range(1, 101):
    #     if count % 2 != 0:
    #         continue
    #     print(count)
   
    # for i in range(1000):
    #     print(i)
    #     if i == 300:
    #         break
   
    # texto = input('Ingrese texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)
    vidas = 0
    
    while vidas < 3:
        vidas += 1
        
        num = input('Cuánto es 7 por 8: ')
        if num == '56':
            print('Correcto')
        else:
            print('mal')
        
        num1 = input('Cuánto es 238 dividido para 14: ')
        if num1 == '17':
            print('exelente')
        else:
            print('muy mal')
        
        num2= input('Cuál es la raíz cuadrada de 144: ')
        if num2 == '12':
            print('vas bien')
        else:
            print('no me lo creo')
        
        num3 = input('Cuánto es 4 al cubo?: ')
        if num3 == '64':
            print('perfecto')
        else:
            print('pésimo')
        
        num4 = input('factoriza a^2 + 8a + 16 = 0, a cuánto equivale a?: ')
        if num4 == '-4':
            print('felicitaciones eres un genio de la matemática')
            break
        else:
            if vidas == 3:
                print('Lo siento pero no tienes ni idea de matemáticas así que perdiste')
                break
            print('te toca hacerlo de nuevo')

       
        

        
if __name__ == '__main__':
    run()