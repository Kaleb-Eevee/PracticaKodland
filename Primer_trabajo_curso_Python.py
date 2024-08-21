import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_lenght= int(input("¿Cual va a ser la lngitud de su contraseña?"))
password = ""
for i in range(password_lenght):
    password += random.choice(characters)

print("Contraseña generada", password)