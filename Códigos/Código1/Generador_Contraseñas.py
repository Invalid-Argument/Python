#InvalidArgument
import random
import string

print("Bienvenido a mi generador de contraseñas")
num_carac=int(input("Ingrese el número de caracteres que desee que contenga su contraseña: "))

def generandocontra (num_carac):
  pass=""
  for i in range(num_carac):
    char=random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)
    pass = pass + char
  print(f"La contraseña que se creó es: {pass}")

generandocontra(num_carac)
