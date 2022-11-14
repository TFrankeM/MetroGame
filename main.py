import sys
import pygame
import random
from pygame.math import Vector2
#sys.path.insert(0, '.')
#from classes import Fruit

class Passageiro: # Classe cujos objetos representam os passageiros
    def __init__(self):
        self.x = random.randint(0, cn-1)
        self.y = random.randint(0, cn-1)
        self.pos = Vector2(self.x, self.y) 
        # A posição é randomizada dentro dos limites da tela e guardada num vetor.

    def desenhar_passageiro(self):
        passageiro_rect = pygame.Rect(int(self.x*cs), int(self.y*cs), cs, cs)
        pygame.draw.rect(screen, (111, 222, 142), passageiro_rect)
        # O passageiro é renderizado como um bloco colorido
        
class Trem:
    def __init__(self):
        self.corpo = [Vector2(5,2), Vector2(4,2), Vector2(3,2)]
        self.sentido = Vector2(1,0)
        # O trem começa com três blocos numa posição definida, que compõem seu corpo, e com um sentido de movimanto também já definido
    
    def desenhar_trem(self):
        for vagao in self.corpo:
            vagao_rect = pygame.Rect(int(vagao.x*cs), int(vagao.y*cs), cs, cs)
            pygame.draw.rect(screen, (111, 222, 142), vagao_rect)
        # Cada vagão do trem é um bloco
    
    def mover_trem(self):
        corpo_copia = self.corpo[:-1]
        corpo_copia.insert(0,corpo_copia[0]+self.sentido)
        self.corpo = corpo_copia[:]
        # QUando o trem se move, o último vagão é eliminado e adiciona-se um vagão à frente dos outros(no começo da lista), que é uma cópia do primeiro vagão 
        # mais uma vez o sentido no qual o trem se move
        


pygame.init()
cs = 16 #cell_size
cn = 40 #cell_number
screen = pygame.display.set_mode((cn*cs,cn*cs))
clock = pygame.time.Clock()
passageiro = Passageiro() # Cria um objeto da classe Passageiro
trem = Trem() # Cria um objeto da classe Trem

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
