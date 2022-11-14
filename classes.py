import pygame
import random
from pygame.math import Vector2

class Passageiro:
    def __init__(self, cn, cs, screen):
        self.x = random.randint(0, cn-1)
        self.y = random.randint(0, cn-1)
        self.pos = Vector2(self.x, self.y)
        # A posição é randomizada dentro dos limites da tela e guardada num vetor.
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado

    def desenhar_passageiro(self):
        passageiro_rect = pygame.Rect(int(self.x*self.cs), int(self.y*self.cs), self.cs, self.cs)
        pygame.draw.rect(self.screen, (111, 222, 142), passageiro_rect)
        # O passageiro é renderizado como um bloco colorido
        
class Trem:
    def __init__(self, cn, cs, screen):
        self.corpo = [Vector2(5,2), Vector2(4,2), Vector2(3,2)]
        self.sentido = Vector2(1,0)
        # O trem começa com três blocos numa posição definida, que compõem seu corpo, e com um sentido de movimanto também já definido
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
    
    def desenhar_trem(self):
        for vagao in self.corpo:
            vagao_rect = pygame.Rect(int(vagao.x*self.cs), int(vagao.y*self.cs), self.cs, self.cs)
            pygame.draw.rect(self.screen, (111, 222, 142), vagao_rect)
        # Cada vagão do trem é um bloco
    
    def mover_trem(self):
        corpo_copia = self.corpo[:-1]
        corpo_copia.insert(0,corpo_copia[0]+self.sentido)
        self.corpo = corpo_copia[:]
        # QUando o trem se move, o último vagão é eliminado e adiciona-se um vagão à frente dos outros(no começo da lista), que é uma cópia do primeiro vagão 
        # mais uma vez o sentido no qual o trem se move
