
import os

class OperasBas:
    #declaracion de variables
    num1=0
    num2=0
    res=0

    #declaracion de constructor
    def __init__(self):
        self.num1=0
        self.num2=0
        self.res=0

    def suma(self):
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        self.res=num1+num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        self.res=num1-num2
        print("La resta es: {}".format(self.res))
    
    def multiplicacion(self):
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        self.res=num1*num2
        print("La multiplicacion es: {}".format(self.res))
    
    def division(self):
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        self.res=num1/num2
        print("La dicvision es: {}".format(self.res))

def main():
        obj=OperasBas()
        accion=0
        while accion!=5:
            print("Menu \n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Salir")
            accion=int(input("Operacion a realizar: "))
            if accion ==1:
                obj.suma()
            if accion ==2:
                obj.resta()
            if accion ==3:
                obj.multiplicacion()
            if accion ==4:
                obj.division()
            if accion ==5:
                print("Adios")
                os.system('cls')

    #declaracion de metodos de clase
if __name__ == "__main__":
        main()