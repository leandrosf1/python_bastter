def somar():    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f"A soma de {num1} e {num2} é {num1 + num2}.")

def subtrair():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f"A subtração de {num1} menos {num2} é {num1 - num2}.")

def multiplicar():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digete o segundo número: '))
    print(f"A multiplicação entre {num1} e {num2} é {num1 * num2}.")

def dividir():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado = round(num1 / num2, 2)
    print(f"A divisão entre {num1} e {num2} é {resultado}.")