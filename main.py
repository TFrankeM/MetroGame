import sys
import pygame
import random
from pygame.math import Vector2
sys.path.insert(0, '.')
from classes import Passageiro, Trem


pygame.init()
cs = 16 #cell_size
cn = 40 #cell_number
screen = pygame.display.set_mode((cn*cs,cn*cs))
clock = pygame.time.Clock()

passageiro = Passageiro(cn, cs, screen) # Cria um objeto da classe Passageiro
trem = Trem(cn, cs, screen) # Cria um objeto da classe Trem

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
            trem.mover_trem()
            # Identifica quando o evento periódico que foi criado fora do loop ocorre, chamando então a função mover_trem()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                trem.sentido = (0,-1)
            if event.key == pygame.K_DOWN:
                trem.sentido = (0,1)
            if event.key == pygame.K_RIGHT:
                trem.sentido = (1,0)
            if event.key == pygame.K_LEFT:
                trem.sentido = (-1,0)
            # Identifica quando o usuário pressiona uma das setas do teclado e ajuta a direção do movimento do trem de acordo
    
    screen.fill((100,100,200)) # Preenche a tela com cor
    passageiro.desenhar_passageiro() # Desenha o passageiro
    trem.desenhar_trem() # Desenha o trem
    pygame.display.flip() # Renderiza
    clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
