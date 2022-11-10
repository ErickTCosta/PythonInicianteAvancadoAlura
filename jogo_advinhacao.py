
import random


def jogar_advinhacao ():
    print ('*'*33)
    print ("Bem vindo ao jogos mortais de advinhação")
    print ('*'*33)

    numero_secreto = random.randrange (1,101)
    #total_de_tentativas = 3
    rodada = 1
    pontos = 1000
    print ('Qual nivel de dificuldade? ')
    print('(1) Facil \n(2) Medio \n(3) Dificil')

    while (True):
        nivel = int (input ('digite o nivel escolhido: '))
        if nivel == 1:
            total_de_tentativas = 20
            break
        elif nivel == 2:
            total_de_tentativas = 10
            break
        elif nivel == 3:
            total_de_tentativas = 5
            break
        print ("Numero invalido, tente novamente")



    #print (numero_secreto)

    '''while(rodada < total_de_tentativas +1 ):    #usando WHHILE para fazer o laço
        print ('tentativas {} de {} '.format (rodada, total_de_tentativas))
        chute = int (input('Digite um numero entre 1 e 100: '))
        print ('voce digitou ', chute)'''


        
    for rodada in range (1, total_de_tentativas + 1):   #usando FOR para fazer o laço
        print ('tentativas {} de {} '.format (rodada, total_de_tentativas))


    
        chute = int (input('Digite um numero entre 1 e 100: '))    
        print ('voce digitou ', chute)
        pontos = pontos - chute
        if chute < 1 or chute > 100:
            print  ("Chute invalido, tentativa perdida")
            break
        if numero_secreto == chute:
            print ('voce acertou!!')
            rodada = 4
            break
                    
        else:
            print('voce errou!') 
              
            if numero_secreto < chute:
                print('Seu chute foi maior que o numero, seu pontos atuais são: ', pontos)
                  
            elif numero_secreto > chute:
                print ('Seu chute foi menor que o numero, seu pontos atuais são: ', pontos)
                
                print ('Seus pontos agoras são: {}'.format (pontos))
                #total_de_tentativas = total_de_tentativas -1
            rodada = rodada + 1

    print (' fim do jogo! ')

if (__name__ == "__main__"):
    jogar_advinhacao ()
    