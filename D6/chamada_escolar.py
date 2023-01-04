#Crie uma lista de chamada de uma sala de aula de uma escola, com nome de 5 alunos.
#  Itere sobre essa lista e printe o nome de cada aluno na tela. Simule o comportamento de uma sala
# de aula. A cada aluno, o programa irá esperar duas possíveis entradas: "presente" ou "ausente".
# Se o aluno estiver presente, printe na tela o nome do aluno e ao lado a marcação que ele está presente.
# Se não, printe o nome do aluno e ao lado a palavra "ausente".

lista_chamada = ["Leandro", "Denise", "Giovana", "Sophia", "Matheus"]

def faz_chamada():
    for aluno in lista_chamada:
        print(f"{aluno}!")
        resposta = input("Aluno está presente ou ausente? ")
        print(f"{aluno} está {resposta}.")
        print("")

faz_chamada()