def somar(a, b):
    somar = a + b
    return print("\nA soma de {} + {} é igual a: {}" .format(a, b, somar))
 

def subtrair(a, b):    
    subtrair = a - b
    return print("\nA subtração de {} - {} é igual a: {}" .format(a, b, subtrair))
    

def multiplicar(a, b):
        multiplicar = a * b
        print("\nA multiplicação de {} * {} é igual a: {}".format(a, b, multiplicar))


def divisao(a, b):
    try:
        divisao = a / b
        return print("\nA divisão de {} / {} é igual a: {:.2f}".format(a, b, divisao))
    # Trata erro caso divisão seja por zero
    except ZeroDivisionError:
        return print("\nO divisor não pode ser 0")    

# Cria um boolean True para a condição do loop
op = True
while(op):
    print("\n -------- Calculadora em Python ---------\n")
    print("Digite a opção desejada:\n1 - Somar\t 2 - Subtrair\n3 - Multiplicar\t 4 - Dividir\n5 - Sair\n")

    # Faz a leitura da opção e armazena na variável op
    op = input()

    # Chama a função de soma e trata possível erro de entrada de dados
    if(op == "1"):
        try:
            x = int(input("Digite o primeiro número número: "))
            y = int(input("Digite o segundo número número: "))
            somar(x,y)
        except ValueError:
            print("\nDigite apenas números!")

    # Chama a função de subtração e trata possível erro de entrada de dados
    elif(op == "2"):
        try:
            x = int(input("Digite o primeiro número número: "))
            y = int(input("Digite o segundo número número: "))
            subtrair(x,y)
        except ValueError:
            print("\nDigite apenas números!")

    # Chama a função de multiplicação e trata possível erro de entrada de dados
    elif(op == "3"):
        try:
            x = int(input("Digite o primeiro número número: "))
            y = int(input("Digite o segundo número número: "))
            multiplicar(x,y)
        except ValueError:
            print("\nDigite apenas números!")
    
    # Chama a função de divisão e trata possível erro de entrada de dados
    elif(op == "4"):
        try:
            x = int(input("Digite o primeiro número número: "))
            y = int(input("Digite o segundo número número: "))
            divisao(x,y)
        except ValueError:
            print("\nDigite apenas números!")

    # Caso o número da opção digitado seja 5 ou maior que 5, a variável op recebe um valor boolean False e para o loop
    elif(op == "5" or op > "5"):
        op = False