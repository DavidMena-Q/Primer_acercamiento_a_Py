import random


menu = print('''Adivina el número que piensa la máquina
Pero recuerda que tienes 6 vidas
 ''')

def run():
    num_aleatorio = random.randint(1, 100)
    num_elegido = int(input('Adivina el número del 1 al 100: '))
    vidas = 0
    while vidas < 6:
        if num_elegido == num_aleatorio:
            print('Ganaste!!')
            break
        if num_elegido < num_aleatorio:
            print('Más alto')
        else:
            print('Más bajo')
        vidas += 1
        if vidas == 6:
            print('Pero se te acabaron tus vidas')
            break
        num_elegido = int(input('Intenta de nuevo: '))
    
    
if __name__ == ('__main__'):
    run()
        