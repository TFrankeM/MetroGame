import sys
import pygame
import random
from pygame.math import Vector2
sys.path.insert(0, '.')
from classes import Passageiro, Trem, Partida, Menu
import time
import operator


pygame.init()
cn = 25 #cell_number
cs = 32 #cell_size
screen = pygame.display.set_mode((cn*cs,cn*cs)) # Tela do jogo
pygame.display.set_caption("Metrô") # Adiciona um nome à janela
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 30)
fonte_1 = pygame.font.Font(None, 120)
fonte_2 = pygame.font.Font(None, 30)
fontes = [fonte_1, fonte_2]

menu = Menu(cn, cs, screen, fontes)
partida = Partida(cn, cs, screen, fonte)


while menu.comecar == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Identifica quando o usuário clica no x na janela, fechando o programa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu.comecar_fase()
                partida.ativo = True
                menu.musica.stop()
                partida.musica.play()
    
    menu.desenhar_elementos()
    pygame.display.flip() # Renderiza
    clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo




SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE, 150)
# Criamos um evento que ocorre a cada 150 milissegundos e que vai acionar o movimento do trem

while menu.comecar == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Identifica quando o usuário clica no x na janela, fechando o programa
        if event.type == SCREEN_UPDATE:
            pygame.time.set_timer(SCREEN_UPDATE, 150)
            if partida.ativo == True:
                partida.atualizar()
            # Identifica quando o evento periódico que foi criado fora do loop ocorre, chamando então a função mover_trem()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and partida.ativo == True:
                partida.pausa = operator.not_(partida.pausa)
                menu.pausa = partida.pausa
            if event.key == pygame.K_UP and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,-1) or event.key == pygame.K_w and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,-1):
                partida.trem.sentido = Vector2(0,-1)
            if event.key == pygame.K_DOWN and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,1) or event.key == pygame.K_s and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,1):
                partida.trem.sentido = Vector2(0,1)
            if event.key == pygame.K_RIGHT and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(1,0) or event.key == pygame.K_d and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(1,0):
                partida.trem.sentido = Vector2(1,0)
            if event.key == pygame.K_LEFT and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(-1,0) or event.key == pygame.K_a and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(-1,0):
                partida.trem.sentido = Vector2(-1,0)
            # Identifica quando o usuário pressiona uma das setas do teclado e ajusta a direção do movimento do trem de acordo
            if partida.ativo == False:
                pygame.time.set_timer(SCREEN_UPDATE, 200)
                partida = Partida(cn, cs, screen, fonte)
                partida.ativo = True
                partida.musica.play()
        
    screen.fill((100,100,200)) # Preenche a tela com cor
    partida.desenhar_elementos()
    menu.desenhar_elementos()
    pygame.display.flip() # Renderiza
    clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
