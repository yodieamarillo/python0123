msg = """Elija una de las siguientes opciones:

a) Mostrar la suma de los dos números
b) Mostrar la resta de los dos números (el primero menos el segundo)
c) Mostrar la multiplicación de los dos números
"""
print(msg)
##obtener inputs desde teclado
numeroOne=int(input('ingrese un valor:'))
numeroTwo=int(input('ingrese segundo valor:'))
opcionMenu=input('ingrese la opcion del menu:').upper()
## Menu

print(numeroOne,numeroTwo,opcionMenu)

if(opcionMenu!='A' or opcionMenu!='B' or opcionMenu!='C'):
    if opcionMenu=='A':
        print(numeroOne+numeroTwo)
    elif opcionMenu=='B':
        print(numeroOne-numeroTwo)
    elif opcionMenu=='C':
        print(numeroOne*numeroTwo)
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')

if True:
    pass
elif True:
    pass
elif True:
    pass
else:
    pass