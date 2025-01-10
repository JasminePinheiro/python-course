# Calculadora simples

print("Bem-vindo à Calculadora")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Selecione uma opeação (+, -, *, /):  ")

if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado} ")
elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado} ")
elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado} ")
elif operacao == "/":
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado} ")
