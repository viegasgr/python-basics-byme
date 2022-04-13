#Calculadora de Equações

import math
import cmath

def raizes_equa(a, b, c):
    delta = b**2 - (4 * a * c)
    if (delta==0):
        raiz_1 = -b/2*a
        raiz_2 = "não tem"
    elif (delta > 0):
        raiz_1 = (-b + math.sqrt(delta))/(2*a)
        raiz_2 = (-b - math.sqrt(delta))/(2*a)
    else:
        raiz_1 = (-b + cmath.sqrt(delta))/(2*a)
        raiz_2 = (-b - cmath.sqrt(delta))/(2*a)
    return [raiz_1, raiz_2]

affirmative_resp = {"yes", "sim", "claro", "com certeza", "uhum", "s", "si", "ye", "ss"}
negative_resp = {"nop", "não", "hmm, não", "no", "nao", "not", "n", "np"}

print("Olá! Essa é uma calculadora de raízes de equações de segundo grau")
response = input("Vamos lá? ").lower().strip()

while (1):
    if (response in negative_resp) == True:
        print("Ok, fica para a próxima!")
        break
    
    elif (response in affirmative_resp) == True:
        print("Ok, me informe o valor de...")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        
        raizes = raizes_equa(a, b, c)
        if raizes[1] == "não tem":
            print("Essa função tem apenas uma raíz! A raíz é", raizes[0])
        else:
            print("As raízes dessa função são:", raizes[0], "e", raizes[1])
       
        response = input("Você quer calcular outra função?").lower().strip()
    else:
        print("Desculpe, não entendi.")
        response = input("Você quer calcular uma função?").lower().strip()