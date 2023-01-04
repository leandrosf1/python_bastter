def calcula_imc():
    '''
    Função que recebe o Peso e a Altura e calcula o IMC, retornando o resultado e a faixa do IMC calculado.
    '''
    peso = float(input('Digite o seu peso em Kg: ').replace(",","."))
    altura = float(input('Digite sua altura em metros: ').replace(",","."))
    imc = round(peso / (altura ** 2), 2)
    imc_convertida = str(imc).replace(".",",")
    if imc < 18.5:
        print(f'Seu IMC é {imc_convertida} - Abaixo do peso.')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Seu IMC é {imc_convertida} - Peso normal.')
    elif imc > 24.9 and imc <= 29.9:
        print(f'Seu IMC é {imc_convertida} - Sobrepeso.')
    elif imc > 29.9 and imc <= 34.9:
        print(f'Seu IMC é {imc_convertida} - Obesidade Grau I')
    elif imc > 34.9 and imc <= 39.9:
        print(f'Seu IMC é {imc_convertida} - Obesidade Grau II')
    else:
        print(f'Seu IMC é {imc_convertida} - Obesidade Grau III')

calcula_imc()