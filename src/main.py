import sys
import pygame
import random
from pygame.math import Vector2
sys.path.insert(0, '.')
from classes import Passageiro, Trem, Partida, Menu, Recorde
import time
import operator


pygame.init()

cn = 25 # Quantidade de células no mapa
cs = 32 # Tamanho das células

screen = pygame.display.set_mode((cn * cs,cn * cs)) # Tamanho da tela do jogo
pygame.display.set_caption("Metrô") # Adiciona um nome à janela
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 30)
fonte_1 = pygame.font.Font(None, 120)
fonte_2 = pygame.font.Font(None, 30)
fontes = [fonte_1, fonte_2]

menu = Menu(cn, cs, screen, fontes)
partida = Partida(cn, cs, screen, fonte)
SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE, 150)
# Criamos um evento que ocorre a cada 150 milissegundos e que vai acionar o movimento do trem

while True:
    if menu.jogo == "Menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Identifica quando o usuário clica no x na janela, fechando o programa
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.nome_rect.collidepoint(event.pos):
                    menu.selecionado = True
                else:
                    menu.selecionado = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    menu.comecar_fase()
                    partida.ativo = True
                    menu.musica.stop()
                    partida.musica.stop()
                    partida.musica.play()
                elif event.key == pygame.K_BACKSPACE and menu.selecionado == True:
                    menu.nome = menu.nome[:-1]
                elif len(menu.nome) < 20 and menu.selecionado == True:
                    menu.nome += event.unicode
                    
        menu.desenhar_elementos()
        pygame.display.flip() # Renderiza
        clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
        
    elif menu.jogo == "Meio":
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
                    menu.jogo = "Fim"
                    menu.registrar_recorde()
                    menu.recorde.escrever(partida.pontuacao)
                    partida.__del__()
        
        partida.desenhar_elementos()
        menu.desenhar_elementos()
        pygame.display.flip() # Renderiza
        clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
        
    elif menu.jogo == "Fim":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu.recorde.arquivo.close()
                pygame.quit()
                sys.exit()
                # Identifica quando o usuário clica no x na janela, fechando o programa
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

        screen.fill((100,100,200)) # Preenche a tela com cor
        partida.desenhar_elementos()
        menu.desenhar_elementos()
        pygame.display.flip() # Renderiza
        clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
            
