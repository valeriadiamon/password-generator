import string,random
from hash import hash_password 

cant = int(input("Teclee la cantidad de caracteres para su contraseña"))
password = ""
for x in range(cant):
    option = random.randint(0,9)
    if option < 5:
        num=random.randint(0,9)
        password = password + str(num)
    else:
        rand = random.choice(string.ascii_letters)
        password = password + rand

print("Su contraseña es: ",password)

password_hashed =  hash_password(password)
print("Su password hasheado es: ", password_hashed.hexdigest())