import pygame
from pygame.locals import *
from sys import exit
from random import randint



pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
# barulho_colisao.set_volume(0)

# definindo as dimensões da tela
largura = 640
altura = 480  
x = int(largura/2)
y = int(altura/2)       

x_azul = randint(40,600)
y_azul = randint(50,430)
#                         (fonte,tamanho, negrito, italico)
fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo legal")
relogio = pygame.time.Clock()

# loop principal do jogo
while True:
    #quantos frames
    relogio.tick(30)
    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}' 
    #                              (string, texto menos pixelado, cor)
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    #detectar se algum evento ocorreu
    for event in pygame.event.get():

        # captura o evento de fechar a janela
        if event.type == QUIT:
            try:
                pygame.quit()
                exit()
            except Exception as error:
                print(error)
        if pygame.key.get_pressed()[K_a] :
            x = x - 20
        if pygame.key.get_pressed()[K_d] :
            x = x + 20
        if pygame.key.get_pressed()[K_w] :
            y = y - 20
        if pygame.key.get_pressed()[K_s] :
            y = y + 20
    #desenha retangulo                 x   y   w  h
    ret_vermelho = pygame.draw.rect(tela,(255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela,(0,0,255), (x_azul,y_azul,40,50))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
        
    #atualiza a tela   
    tela.blit(texto_formatado, (450,40))         
    pygame.display.update()