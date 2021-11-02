''' 
Escribir un programa en python que calcule e imprima en pantalla la superficie de un triangulo en funcion
de la base y la altura  (S = 1/2 Base × Altura). Los valores son introducidos por el usr.
'''
def triangulo(base,altura):
    s = (base*altura)/2
    if base>0 and altura>0:
     print(f"la superficie del triangulo es {s}")
    else:
        print("No hay superficies")
base = float(input("Digite la base del Triangulo: "))
altura = float(input("Digite la altura del Triangulo: "))
triangulo(base, altura)