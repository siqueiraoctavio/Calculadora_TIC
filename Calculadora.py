def calculadora ():
    while True: #Loop infinito para sempre retornar ao menu inicial
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("Selecionar operação ou 's' para sair: ")

        #Definição de Saída

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a Calculadora Simples!")
            break #Sai do loop infinito e encerra a calculadora

        # Tratar entradas inválidas

        if operacao not in ['1','2','3','4']:
            print("Opção inválida! Tente novamente")
            continue #Retorna ao loop

        numero_1 = float(input("Primeiro Número: "))
        numero_2 = float(input("Segundo Número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da soma é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da subtração é: ", resultado)

        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da multiplicação é: ", resultado)

        else:
            if numero_2 == 0:
                print("Divisões por 0 não são permitidas!")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da divisão é: ", resultado)

calculadora()


