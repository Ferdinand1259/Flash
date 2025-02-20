import random

password = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
longitud = int(input('Ingresa la cantidad de caracteres.'))
caracteres = ''

for i in range(longitud):
    caracter = random.choice(password)
    caracteres = caracteres + caracter

print('Este es tu password: ' + caracteres)
