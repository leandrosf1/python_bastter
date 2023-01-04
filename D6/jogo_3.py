#Melhore o "jogo_3.py". Adicione um placar ao jogo. Mostre o resultado global ao final de cada jogada.

#Melhore o "jogo.py". Pergunte ao final de cada jogada se o jogador quer continuar jogando.
# Se sim, rode o jogo novamente até o jogador desistir de jogar. Se não, finalize o jogo.

import random
import time

pontos_computador = 0
pontos_jogador = 0

def delay(tempo):
    time.sleep(tempo)

def apresenta_escolhas():
    print("####################################")
    print("####       Joguinho legal       ####")
    print("####################################")
    print("Regra: Quem fizer 3 pontos primeiro vence o jogo!")
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
    delay(1)
    if (jogador == computador): 
        print("Vocês empataram!")
        calcula_placar("")
    elif (jogador == 1 and computador == 2 ) \
         or (jogador == 2 and computador == 3) \
            or (jogador == 3 and computador == 1):
        print("Você perdeu!")
        calcula_placar("computador")
    else:
        print("Vocês ganhou!")
        calcula_placar("jogador") 
    delay(1)
    print("")

def calcula_placar(ganhador):
    global pontos_computador
    global pontos_jogador
    if (ganhador == "computador"):
        pontos_computador += 1
    elif (ganhador == "jogador"):
        pontos_jogador += 1
    print("")
    delay(1)
    print(f"Placar: Jogador {pontos_jogador} x {pontos_computador} Computador.")   

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

def verifica_fim_jogo():
    global pontos_jogador
    global pontos_computador
    if (pontos_jogador == 3):
        print("Você fez 3 pontos e ganhou o jogo. Parabéns!")
        print("")
    elif(pontos_computador == 3):
        print("O computador fez 3 pontos e ganhou o jogo. Você perdeu!")
        print("")
    else:
        jogar_novamente()    

def jogar():
    apresenta_escolhas()
    jogador = escolha_jogador()
    computador = escolha_computador()
    delay(1.5)
    valida_jogada(jogador, computador)
    verifica_fim_jogo()

jogar()