'''
Calcular y visualizar la longitud de la circunferencia y el área de un círculo de radio dado.
'''
import math
def circunferencia(radio):
    l = 2*math.pi*radio
    area = math.pi * radio**2
    if radio>0:
     print(f"la longitud de la circunferencia es: {l}, y el area del circulo es: {area}")
    else:
        print("no hay area")

radio = float(input("Digite el radio de la circunferencia: "))
circunferencia(radio)