#Melhore o "jogo.py". Pergunte ao final de cada jogada se o jogador quer continuar jogando.
# Se sim, rode o jogo novamente até o jogador desistir de jogar. Se não, finalize o jogo.

import random
import time

def delay(tempo):
    time.sleep(tempo)

def apresenta_escolhas():
    print("####################################")
    print("####        Joguinho legal      ####")
    print("####################################")
    print("Vamos jogar, você tem três opções.")
    print(f"[1] - {descricao_opcao_escolhida(1)}")
    print(f"[2] - {descricao_opcao_escolhida(2)}")
    print(f"[3] - {descricao_opcao_escolhida(3)}")  
    print("")  
    
def descricao_opcao_escolhida(opcao):
    if (opcao == 1):
        return "Pedra"
    elif (opcao == 2):
        return "Papel"
    else:
        return "Tesoura"

def escolha_computador():
    return random.randrange(1,3)

def escolha_jogador():
    opcao_jogador = int(input("Escolha sua jogada: ")) 
    while opcao_jogador not in (1, 2, 3):
        opcao_jogador = int(input("Algo deu errado. Opção inválida, informe outra opção: "))
    return opcao_jogador 

def valida_jogada(jogador, computador):
    print (f"Você escolheu {descricao_opcao_escolhida(jogador)} e o computador escolheu {descricao_opcao_escolhida(computador)}.")
    if (jogador == computador): 
        print("Vocês empataram!")
    elif (jogador == 1 and computador == 2):
        print("Vocês perdeu!")
    elif (jogador == 1 and computador == 3):
        print("Vocês ganhou!")
    elif (jogador == 2 and computador == 1):
        print("Vocês ganhou!")
    elif (jogador == 2 and computador == 3):
        print("Vocês perdeu!")
    elif (jogador == 3 and computador == 1):
        print("Vocês perdeu!")
    else:
        print("Vocês ganhou!")    
    print("")

def jogar_novamente():
    opcao = input("Deseja jogar novamente? (s/n)")
    delay(1)
    while opcao not in ("s", "n"):
        opcao = input("Opção inválida! Deseja jogar novamente? (s/n)")
    
    if (opcao == "s"):
        print("")
        jogar()
    else:
        print("Até a próxima!!!") 
        print("") 

def jogar():
    apresenta_escolhas()
    jogador = escolha_jogador()
    computador = escolha_computador()
    delay(1.5)
    valida_jogada(jogador, computador)
    jogar_novamente()

jogar()