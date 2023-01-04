#Crie um programa que receba uma palavra do usuário e diga se a palavra é um palíndromo.
# Se não for, diga que a palavra não é um palíndromo.

def faz_split_texto_original(texto_original):
    texto_split = ""
    for letra in texto_original:
        texto_split = texto_split + letra.strip()
    return texto_split

def verifica_se_eh_palindromo(texto):
    texto_split = faz_split_texto_original(texto)
    texto_alterado = texto_split[::-1]
    if texto_split.lower() ==  texto_alterado.lower():
        print(f"Texto {texto} é um palíndromo.")
    else:
        print(f"Texto {texto} não é um palíndromo.")

def inicializa_programa():
    texto = input("Digite um texto para verificar se é palíndromo: ")
    verifica_se_eh_palindromo(texto)

inicializa_programa()