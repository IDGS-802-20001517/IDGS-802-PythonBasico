'''
Leer el numero 5

5 x 1 =5
5 x 2 =10
.
.
5 x 10 =50

'''

print("Tabla Multiplicar")


nummero=int(input('Dame numero: '))
for num in range (1,11,):
    print("{} x {} = {}" .format(nummero,num,(nummero*num)))


