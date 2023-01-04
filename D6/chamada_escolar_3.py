#O programa "chamada_escolar_2" tem uma saída de dados bem brusca. Torne essa saída mais palatável
# para quem lê. Adicione um timer a cada output do programa.

import time

lista_chamada = ["Leandro", "Denise", "Giovana", "Sophia", "Matheus"]

def delay():
    time.sleep(2)

def valida_chamada(aluno, resposta):
    while resposta not in ("presente", "ausente"):
        resposta = input("Opção inválida, informe se o(a) aluno(a) está presente ou ausente: ")
    print(f"{aluno} está {resposta}.")
 

def faz_chamada():
    for aluno in lista_chamada:
        print(f"{aluno}!")
        resposta = input("Aluno está presente ou ausente? ")
        valida_chamada(aluno, resposta)
        print("")
        delay()
        

faz_chamada()