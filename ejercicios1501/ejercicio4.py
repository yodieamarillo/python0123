vLista=[10,23,45,'hello']

a=type(vLista[-1])

if a==str:
    print("el ultimo elemento es string")
else:
    print('el elemento no es string')
vLista.append(2)