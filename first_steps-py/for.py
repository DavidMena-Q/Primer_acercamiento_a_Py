# count = 1
# print(count)
# while count < 10:
#     count += 1
#     print(count)

# a = list(range(100))
# print(a)

# for count in range(1, 101):
#     print(count)

# for i in range(10):
#     print(11 * i)

menu = print('           "Las tablas de multiplicar"')


def run():
    multiplicador = float(input('De cuál número quieres ver su tabla de multiplicación? : '))
    rango =  int(input('Cuál quieres que sea el rango de la multiplicación? '))
    for count in range(rango + 1):
        print(round(count * multiplicador, 4))


if __name__ == ('__main__'):
    run()


