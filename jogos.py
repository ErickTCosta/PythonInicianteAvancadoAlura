import jogo_advinhacao
import jogo_forca


print ('*'*33)
print ("Bem vindo aos Jogos Mortais!!!")
print ('*'*33)

print ("escolha um jogo:\n(1) Advinhação \n(2) Forca" )
jogo = int (input ("Qual jogo?: "))

if jogo == 1:
    print ('*'*5,"Carregando o jogo Advinhação", '*'*5)
    jogo_advinhacao.jogar_advinhacao ()
elif jogo == 2:
    print ('*'*5,"Carregando o jogo Forca",'*'*5)
    jogo_forca.jogar_forca ()
