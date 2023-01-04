#Faça um programa que recebe uma palavra do usuário. 
# Conte quantas letras "a" há nessa palavra e mostre o resultado  na tela.
# Faça esse exercício usando um laço.

def conta_letra(palavra):
    contador_de_letra = 0
    for letra in palavra:
        if letra.lower() == 'a':
            contador_de_letra += 1
    
    if contador_de_letra == 0:
         print(f'Não exite a letra a na palavra {palavra}.')
    else:
        print(f'Exite(m) {contador_de_letra} letra(s) a na palavra {palavra}.')


def inicializa_programa():
    palavra = input("Informe uma palavra para contar a quantidade de letras a: ")
    conta_letra(palavra)

inicializa_programa()