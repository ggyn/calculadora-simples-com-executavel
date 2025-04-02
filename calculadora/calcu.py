def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero não é permitida."

def exponenciacao(a, b):
    return a ** b

def raiz_quadrada(a):
    import math
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erro: número negativo não tem raiz quadrada real."

def menu():
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite o número da operação: ")

        if escolha == '7':
            print("Encerrando a calculadora. Até mais!")
            break
        elif escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print(f"Resultado: {soma(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {divisao(num1, num2)}")
            elif escolha == '5':
                print(f"Resultado: {exponenciacao(num1, num2)}")
        elif escolha == '6':
            num = float(input("Digite o número: "))
            print(f"Resultado: {raiz_quadrada(num)}")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()