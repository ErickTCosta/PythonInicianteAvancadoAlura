import random



def jogar_forca ():

    abertura_jogo()
    palavra_secreta = carregando_palavra()
    letras_acertadas = linhas_letras (palavra_secreta)
   
    
    print (letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    

   
    while (not enforcou and not acertou):
        
        chute = chute_jogador ()
        
        if chute in palavra_secreta:
           letra_acerto (chute, letras_acertadas, palavra_secreta)
                
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros  == 7
        
        acertou = "_" not in letras_acertadas
        print (letras_acertadas)

    if acertou:
        mensagem_sobrevivente ()
        
    else:
        mensagem_enforcado (palavra_secreta)
        

        







def abertura_jogo ():
    print ('*'*33)
    print ("Bem vindo ao jogos mortais da Forca")
    print ('*'*33)

def carregando_palavra ():
    arquivo = open ('palavra_secreta.txt', 'r')

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close ()

    numero = random.randrange (0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def linhas_letras (palavra):
    return ["_" for letra in palavra]

def chute_jogador (): 
    chute = input ("Qual a sua letra? ").upper()
    chute = chute.strip ()
    return chute

def letra_acerto (chute, letras_acertadas, palavra_secreta):
    index = 0   
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[index] = letra
                    
        index += 1   

def mensagem_sobrevivente ():
    print("Parabéns, você sobreviveu ao Jogo da Forca!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mensagem_enforcado (palavra_secreta):
    print("Puxa, você foi enforcado!")
    print ("A palavra era: ", palavra_secreta)
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")        


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar_forca()
