import random as r
import math as m


while(True):
    print("MENU PRINCIPAL:")
    print("1. Calculo Aritmetico")
    print("2. Contagem")
    print("3. Sortear Número")
    print("4. Sair do sistema")
    op = int(input("Digite a opção desejada do menu de opções: "))
#menu 1
    if(op == 1):
        while(True):
            print("\nVocê entrou na opção 1\n\nSubmenu Calculo: ")
            print("1. Tabuada de um número")
            print("2. Raiz quadrada")
            print("3. Potência")
            print("4. Voltar")
            op1 = int(input("Digite a opção desejada da opção 1: "))
    #op1 menu1
            if(op1 == 1):
                tabu = int(input("Digite o número para cacular sua tabuada: "))
                i = 0
                while(i <= 10):
                    rt = tabu * i
                    print(f"{i} X {tabu} = {rt}")
                    i += 1
    #op2 menu1              
            elif(op1 == 2):
                raiz = int(input("Digite um número para calcularmos sua raiz quadrada: "))
                rr = m.sqrt(raiz)
                print(f"A raiz quadrada de {raiz} = {rr}")
    #op3 menu1
            elif(op1 == 3):
                base = int(input("Digite um número para ser a base: "))
                expo = int(input("Digite um número para ser o expoente: "))
                rp = m.pow(base, expo)
                print(f"{base} elevado a {expo} = {rp}")
    #op4 menu1        
            elif(op1 == 4):
                print("\nVocê voltou a menu de opções\n")
                break
    #else menu1
            else:
                print("Erro: Essa opção não existe.\nTente novamente")
#menu2            
    elif(op == 2):
        while(True):
            print("\nVocê entrou na opção 2\n\nSubmenu Contagem: ")
            print("1. Contar de 1 a 20")
            print("2. Contar do inicio ao fim de n em n")
            print("3. Voltar")
            op2 = int(input("Digite a opção desejada da opção 2: "))
    #op1 menu2
            if(op2 == 1):
                i2 = 1
                for i in range(1, 21, 1):
                    print(i)
    #op2 menu2        
            elif(op2 == 2):
                ini2 = int(input("Digite o valor de inicio: "))
                fin2 = int(input("Digite o valor final: "))
                i3 = ini2
                for i3 in range(ini2, fin2, 1):
                    print(i3)
    #op3 menu2
            elif(op2 == 3):
                print("\nVocê voltou a menu de opções\n")
                break
    #else menu2
            else:
                print("Erro: Essa opção não existe.\nTente novamente")
#menu3
    elif(op == 3):
        while(True):
            print("\nVocê entrou na opção 3\n\nSubmenu Sortear Números: ")
            print("1. Sortear de 1 a 10")
            print("2. Sortear de n em n")
            print("3. Voltar")
            op3 = int(input("Digite a opção desejada da opção 3: "))
    #op1 menu3
            if(op3 == 1):
                ran1 = r.randint(1, 10)
                print("O número sorteado entre 1 a 10 foi: ",ran1)
    #op2 menu3
            elif(op3 == 2):
                ini3 = int(input("Digite o intervalo inicial: "))
                fin3 = int(input("Digite o intervalo final: "))
                ran2 = r.randint(ini3, fin3)
                print(f"O número sorteado entre {ini3} e {fin3} é: {ran2}")
    #op3 menu3
            elif(op3 == 3):
                print("\nVocê voltou a menu de opções\n")
                break
    #else menu3
            else:
                print("Erro: Essa opção não existe.\nTente novamente")
#menu4
    elif(op == 4):
        print("\nVocê saiu deste sistema!\n")
        break


#else menu de opções
    else:
        print("Essa opção não existe\nTente Novamente")
        print()
        break


print("FIM")
