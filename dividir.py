numero1=float(input("Ingrese el numero a dividir: "))
numero2=float(input("Ingrese el numero divisor: "))

def dividir(nro, nro2):
    total=nro/nro2
    print("el total de la division es: ",round(total,2))

dividir(numero1,numero2)