import random

print ('********************************')
print ('Bem vindo ao jogo de adivinhação')
print ('********************************')

numero_secreto = random.randrange (1,101)
print (numero_secreto)
total_tentativas = 3
rodada = 1
pontos = 1000

while (True):
    print ("Escolha o nivel do jogo:")
    print ("(1) Fácil (2) Médio (3) Difícil")

    nivel = int (input ("Digite o nivel: "))

    if nivel == 1:
        total_tentativas = 20
        break
    elif nivel == 2:
        total_tentativas = 10
        break
    elif nivel == 3:
        total_tentativas = 5
        break
    else:
        print ("numero invalido")

while (total_tentativas >= rodada ): 
    print (f"total de tentativas: {rodada} de {total_tentativas}") #ou ("Tentativas {} de {} ".format (rodada,total_tentativas))
    chute_str = input ("Digite um numero entre 1 e 100: ")
    print ("Seu chute ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if chute < 1 or chute > 100:
        print ("Digite um numero entre 1 e 100!")
        continue

    if (acertou):
        print ("voce acertou! e fez {} pontos".format (pontos))
        break
    else:
        if(maior):
            print("você errou, seu chute foi maior que o numero secreto.")
            if rodada == total_tentativas :
                print ("E o total de pontos feito foram {}".format(pontos))
        elif (menor):
            print("você errou, seu chute foi menor que o numero secreto.")
            if rodada == total_tentativas :
                print ("E o total de pontos feito foram {}".format(pontos))

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    rodada = rodada + 1
print ("fim de jogo!!")