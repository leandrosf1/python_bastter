#Crie um programa que vai receber dois números do usuário. 
#O programa deve ter uma função que vai receber os dois números.
#Faça essa função retornar o menor desses números.
#Se os dois forem iguais, retorne uma mensagem informando isso.
def numero_menor():
    num1 = float(input('Digite o primeiro número: ').replace(",","."))
    num2 = float(input('Digite o segundo número: ').replace(",","."))
    
    if num1 < num2:
        print(str(num1).replace(".",","))
    elif num1 > num2:
        print(str(num2).replace(".",","))
    else:
        print('Ambos os números são iguais.')

numero_menor()