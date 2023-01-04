#Procure se há nos métodos de string alguma função que possa te ajudar 
# a contar as letras de forma mais fácil, sem precisar "reinventar a roda".

def conta_letra(palavra):
    contador_de_letra = palavra.count('a')    
    if contador_de_letra == 0:
         print(f'Não exite a letra a na palavra {palavra}.')
    else:
        print(f'Exite(m) {contador_de_letra} letra(s) a na palavra {palavra}.')


def inicializa_programa():
    palavra = input("Informe uma palavra para contar a quantidade de letras a: ")
    conta_letra(palavra)

inicializa_programa()