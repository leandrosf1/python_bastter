#Melhore o programa "chamada_escolar.py".
# Agora se a entrada de presença for diferente de "presente" ou "ausente", faça o programa perguntar
# a resposta certa até o usuário digitar uma resposta certa. Enquanto isso não acontecer, imprima na tela 
# uma mensagem de erro e peça novamente a entrada correta.

lista_chamada = ["Leandro", "Denise", "Giovana", "Sophia", "Matheus"]

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
        

faz_chamada()