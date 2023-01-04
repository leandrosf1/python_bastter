#Escreva um programa com duas funções. A primeira vai fazer o computador escolher um número entre 1 e 3.
# A segunda vai chamar a primeira e pedir ao usuário um número entre 1 e 3. Se o usuário digitar o mesmo
# número que o computador, imprime mensagem dizendo que o usuário adivinhou o número do computador. Se não, 
# imprime a mensagem dizendo o número escolhido pelo computador e afirmando que o usuário errou o palpite.
import random

def calcula_numero_randomico():
    return int(random.randint(1,3))

def adivinha_numero():
    numero_usuario = int(input('Digite um número entre 1 e 3: '))
    numero_ramdomico = calcula_numero_randomico()

    if numero_usuario == numero_ramdomico:
        print('Parabéns, você acertou.')
    else:
        print(f'Você errou, o número gerado foi {numero_ramdomico}.')

adivinha_numero();