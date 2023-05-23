import math
import random


print("==Menu de Opções==")
print("1. Somar 2 números: ")
print("2. Potência de um número : ")
print("3. Raiz quadrada de X: ")
print("4. Gerar um número aleatório: ")
option = input("\nEscolha uma das opções do menu: ")


#1 soma
if(option == "1"):
    print("==Menu de Opções==")
    print("Somar 2 números")
    n1 = float(input("1º número: "))
    n2 = float(input("2º número: "))
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma:.1f}")


#2 potencia
elif(option == "2"):
    print("Potência Y de um número X (xy)")
    potencia = int(input("Digite a potência do número: "))
    numero_potencia = int(input("Digite o número desejado: "))  
    resultado = math.pow(numero_potencia, potencia)
    print(f"{numero_potencia} elevado a {potencia} = {resultado}")


#3 raiz
elif(option == "3"):
    x = int(input("Digite um número inteiro para ser calculada sua raiz quadrada: "))
    if(x > 0):
        raix = math.sqrt(x)
        print(f"Raiz de {x} = {raix:.1f}")
    else:
        print("Não é possível calcular a raiz de um número negativo")


#4 gerar
elif(option == "4"):
    inicio = int(input("Digite o número inicial: "))
    final = int(input("Digite o número final: "))
    num_rand = random.randint(inicio, final)
    print(f"Entre {inicio} e {final} foi gerado o número {num_rand}")


else:
    print("Essa opção não existe\nTente novamente!")
