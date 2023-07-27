x = "n"

#Variavel para manter o programa aberto

while x != "y":

    #Variavel "y" para fechar o programa

    op = [1, 2 , 3, 4]

    #Variavel das opções


    print("Bem vindo")
    op1 = int(input("Menu \n 1-Numero primo \n 2-Numero decrescente \n 3-Mediana de 3 numeros \n 4-Sair \n Digite o numero equivalente a opcão que deseja: "))

    #Variavel do menu e as opções da lista

    if op1 == op[0]:

    #Opção 1
   
        primov = "q"

        #Variavel para manter o programa aberto

        while primov != "v":

        #Variavel para quebrar o loop
                
            primo = [1, 2, 3]

            #Opções para a lista do menu do numero primo

            primo1 = int(input("Bem vindo ao menu de verificação de numeros primos. \n 1-Lógica \n 2-Refazer \n 3-Voltar ao menu \n Digite o numero correspondente a opção que deseja: "))
            
            #Input para dar valor a variavel "primo1"

            if primo1 == primo [1]:

            #Opção Refazer

                print("Você ainda não usou a lógica.")

                #Print para caso o usuario escolha a opção refazer sem ter feito a lógica
            
            elif primo1 == primo [0]:

            #Opção 1

                nump = int(input("Digite o numero que deseja consultar: "))

                #input para atribur valor a variavel "nump"

                if nump % nump == 0 and nump % 2 != 0 and nump % 3 != 0 and nump % 5 != 0:

                    #Lógica para ver se o numero da variavel nump é primo ou não

                    print(f"O numero {nump} é primo.")

                    #print para caso o numero primo

                else:
                    print(f"O numero {nump} é primo.")

                    #print para caso o numero não for primo

                primo3 = [1, 2, 3]

                primom2 = int(input(" 1-Lógica \n 2-Refazer \n 3-Voltar ao menu \n Digite o numero correspondente a opção que deseja: "))

                if primom2 == primo3 [0]:
                    print("Você ja usou a logica")
                            
                elif primom2 == primo3 [1]:

                    if nump % nump == 0 and nump % 2 != 0 and nump % 3 != 0 and nump % 5 != 0:
                        print("mamaco")
                    else:
                        print("Não é primo")
                            
                    if primom2 == primo3 [2]:
                        primov = "v"

            elif primo1 == primo[1]:
                print("Você ainda não usou a lógica")

            elif primo1 == primo[2]:
                primov = "v"

            else:
                print("Essa opção não consta na lista.")

    elif op1 == op[1]:
        
        decrev = "d"

        while decrev != "v":

            decre = [1, 2, 3, 4]

            decre1 = int(input("Bem vindo ao menu de numeros drecrecentes. \n 1-Lógica \n 2-Refazer \n 3-Voltar \n 4-Sair \n Digite o numero conrrespondente a opção que deseja:"))
    
            if decre1 == decre [1]:
                print("Você ainda não executou a lógica")

            elif decre1 == decre [0]:
                numd = int(input("Digite um número inteiro: "))

                while numd >= 0:
                    print(numd)
                    numd -= 1

                decre2 = [1, 2, 3, 4]

                decre3 = int(input(" 1-Lógica \n 2-Refazer \n 3-Voltar \n 4-Sair \n Digite o numero conrrespondente a opção que deseja: "))

                if decre3 == decre2 [0]:
                    print("Você ja executou a lógica.")
                
                elif decre3 == decre2 [1]:

                    while numd >= 0:
                        print(numd)
                        numd -= 1

                        decre4 = [1, 2, 3, 4]

                        decre5 = int(input(" 1-Lógica \n 2-Refazer \n 3-Voltar \n 4-Sair \n Digite o numero conrrespondente a opção que deseja: "))

                        if decre5 == decre4 [2]:
                            decrev = "v"

                        elif decre5 == decre4 [3]:
                            x = "y"

                elif decre3 == decre2 [2]:
                    decrev = "v"

                elif decre3 == decre2 [3]:
                    x = "y"
            elif decre1 == decre [2]:
                decrev = "v"      
            elif decre1 == decre [3]:
                x = "y"

    elif op1 == op [2]:
        
        medv = "m"
        
        while medv != "v":

            medop = [1, 2, 3]

            med1 = int(input("Bem vindo ao menu de analise de mediana. \n 1-Lógica \n 2-Refazer \n 3-Voltar \n Digite o numero conrrespondente a opção que deseja: "))

            if med1 == medop [1]:
                print("Você ainda não executou a lógica")

            elif med1 == medop [2]:
                medv = "v"

            elif med1 == medop [0]:
                    
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                num3 = float(input("Digite o terceiro número: "))

                if num1 > num2:
                    if num2 > num3:
                        mediana = num2
                    elif num1 > num3:
                        mediana = num3
                    else:
                        mediana = num1
                else:
                    if num2 < num3:
                        mediana = num2
                    elif num1 < num3:
                        mediana = num3
                    else:
                        mediana = num1

                print("A mediana é:", mediana)
                
                medv2 = [1, 2, 3]

                med3 = int(input(" 1-Lógica \n 2-Refazer \n 3-Voltar \n Digite o numero conrrespondente a opção que deseja: "))

                if med3 == medv2 [0]:
                    print("Você ja realizou a lógica")

                elif med3 == medv2 [1]:
                    print("A mediana é:", mediana)

                elif med3 == medv2 [2]:
                    medv = "v"

    elif op1 == op [3]:
        x = "y"

    else:
        print("Essa opção não consta na lista")
