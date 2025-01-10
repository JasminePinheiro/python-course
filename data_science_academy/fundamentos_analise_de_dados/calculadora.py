def input_value():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def start_calculator():
    print("\n -----------Calculadora em python--------------")
    print("Selecione o número da operação desejada:\n")
    print("1 - Soma \n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    operacao = int(input("Digite o número da operação desejada: "))

    if operacao == 1:
        num1, num2 = input_value()
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == 2:
        num1, num2 = input_value()
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif operacao == 3:
        num1, num2 = input_value()
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif operacao == 4:
        num1, num2 = input_value()
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
   
    print("Deseja encerra a operação?")
    sair = input("Digite 'S' para sair ou 'N' para continuar: ")

    if sair.upper() == 'S':
        print("Operação encerrada.")
        exit()
    elif sair.upper() == 'N':
        start_calculator()


start_calculator()

