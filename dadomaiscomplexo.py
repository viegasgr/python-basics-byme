#Simulador de Dado completo

import random

print("Simulador de dado")

response = input("Você quer rolar o dado?").lower().strip()

affirmative_resp = {"yes", "sim", "claro", "com certeza", "quero", "uhum", "s", "si", "ye", "ss"}
negative_resp = {"nop", "não", "nananinanão", "não quero", "hmm, não", "no", "nao", "not", "n"}

while (response in negative_resp) == False:
    if (response in affirmative_resp) == False:
        print("Desculpa, não te entendi.")
        response = input("Você quer rolar o dado?").lower()
    elif (response in affirmative_resp) == True:
        lados = input("Quantos lados deve ter seu dado?")
        if lados.isdigit() == True:
            if int(lados) <= 2:
                print("Hm... Não posso rolar algo plano. Coloque um valor maior, por favor.")
            elif 2 < int(lados) < 101:
                aleatorio = random.randint(1,int(lados))
                print("Seu número é...", aleatorio)
                response = input("Você quer rolar o dado novamente?").lower()
            else:
                print("Hm... Não conheço um dado com tantos lados. O maior que achei tem 100!")
        else:
            print("Por favor, utilize apenas números")

if (response in negative_resp) == True:
  print("Ok, fica para outro dia então.")
