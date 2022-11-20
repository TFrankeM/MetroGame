import sys
import pygame
import random
from pygame.math import Vector2
sys.path.insert(0, '.')
from classes import Passageiro, Trem, Partida
import time
import operator


#try:
pygame.init()
cn = 25 #cell_number
cs = 32 #cell_size
screen = pygame.display.set_mode((cn*cs,cn*cs)) # Tela do jogo
pygame.display.set_caption("Metrô") # Adiciona um nome à janela
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 30)


partida = Partida(cn, cs, screen, fonte)

SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE, 150)
# Criamos um evento que ocorre a cada 150 milissegundos e que vai acionar o movimento do trem

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Identifica quando o usuário clica no x na janela, fechando o programa
        if event.type == SCREEN_UPDATE:
            partida.atualizar()
            # Identifica quando o evento periódico que foi criado fora do loop ocorre, chamando então a função mover_trem()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                partida.pausa = operator.not_(partida.pausa)
            if event.key == pygame.K_UP and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,-1):
                partida.trem.sentido = Vector2(0,-1)
            if event.key == pygame.K_DOWN and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(0,1):
                partida.trem.sentido = Vector2(0,1)
            if event.key == pygame.K_RIGHT and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(1,0):
                partida.trem.sentido = Vector2(1,0)
            if event.key == pygame.K_LEFT and partida.trem.corpo[1] != partida.trem.corpo[0]+Vector2(-1,0):
                partida.trem.sentido = Vector2(-1,0)
            # Identifica quando o usuário pressiona uma das setas do teclado e ajusta a direção do movimento do trem de acordo
            if partida.ativo == False:
                partida = Partida(cn, cs, screen, fonte)
        
    screen.fill((100,100,200)) # Preenche a tela com cor
    #menor = pygame.draw.rect(screen, (100,50,50), pygame.Rect(int(32), int(32), cs*(cn-2), cs*(cn-2)))
    partida.desenhar_elementos()
    pygame.display.flip() # Renderiza
    clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
"""except:
    print("Deu ruim!")
    pygame.quit()
    sys.exit()"""
