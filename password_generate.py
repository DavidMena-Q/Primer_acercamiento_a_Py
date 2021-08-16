import random
import string


def password_generate():
   
    chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

    password = []

    rangee = int(input('Cuántos caracteres quieres?: '))

    for i in range(rangee):
        chars_random = random.choice(chars)
        password.append(chars_random)

    password = ''.join(password)
    return password


def run():
    password = password_generate()
    print(f'Tu nueva contraseña es: {password}')


if __name__ == ('__main__'):
    run()



