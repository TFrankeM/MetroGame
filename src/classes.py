import pygame
import random
from pygame.math import Vector2

class Passageiro:
    def __init__(self, cn, cs, screen):
        self.sortear(cn, cs, screen)
        # A posição é randomizada dentro dos limites da tela e guardada num vetor.
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.pessoa = pygame.image.load('metro_imagens/metro_direita.png').convert_alpha()
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado

    def desenhar_passageiro(self):
        passageiro_rect = pygame.Rect(int(self.x*self.cs), int(self.y*self.cs), self.cs, self.cs)
        self.pessoa = pygame.transform.scale(self.pessoa, (16,16))
        self.screen.blit(self.pessoa, passageiro_rect)
        # O passageiro é renderizado como um bloco colorido

    def sortear(self, cn, cs, screen):
        self.x = random.randint(0, cn-1)
        self.y = random.randint(0, cn-1)
        self.pos = Vector2(self.x, self.y)
        
class Trem:
    def __init__(self, cn=1, cs=1, screen=None):
        self.corpo = [Vector2(5,2), Vector2(4,2), Vector2(3,2)]
        self.sentido = Vector2(1,0)
        self.sentido_antes = Vector2(1,0)
        # O trem começa com três blocos numa posição definida, que compõem seu corpo, e com um sentido de movimanto também já definido
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.novo_vagao = False
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        self.metro_frente_d = pygame.image.load('metro_imagens/metro_direita.png').convert_alpha()
        self.metro_frente_d = pygame.transform.scale(self.metro_frente_d, (16,16))
        self.metro_tras_d = pygame.image.load('metro_imagens/metro_esquerda.png').convert_alpha()
        self.metro_tras_d = pygame.transform.scale(self.metro_tras_d, (16,16))
        self.metro_meio_d = pygame.image.load('metro_imagens/metro_meio_direita_esquerda.png').convert_alpha()
        self.metro_meio_d = pygame.transform.scale(self.metro_meio_d, (16,16))
        
        self.metro_frente_c = pygame.transform.rotate(self.metro_frente_d, 90)
        self.metro_tras_c = pygame.transform.rotate(self.metro_tras_d, 90)
        self.metro_meio_c = pygame.transform.rotate(self.metro_meio_d, 90)
        
        self.metro_frente_e = self.metro_tras_d
        self.metro_tras_e = self.metro_frente_d
        self.metro_meio_e = self.metro_meio_d
        
        self.metro_frente_b = pygame.transform.rotate(self.metro_frente_d, 270)
        self.metro_tras_b = pygame.transform.rotate(self.metro_tras_d, 270)
        self.metro_meio_b = pygame.transform.rotate(self.metro_meio_d, 270)

        self.frente = self.metro_frente_d
        self.tras = self.metro_tras_d
        self.meio = self.metro_meio_d
    
    def desenhar_trem(self):
        self.relacao_frente()
        self.relacao_tras()
        for index, bloco in enumerate(self.corpo):
            x_pos = int(bloco.x*self.cs)
            y_pos = int(bloco.y*self.cs)
            vagao_rect = pygame.Rect(int(bloco.x*self.cs), int(bloco.y*self.cs), self.cs, self.cs)
            if index == 0:
                self.screen.blit(self.frente, vagao_rect)
            elif index == len(self.corpo) -1:
                self.screen.blit(self.tras, vagao_rect)
            else:
                bloco_anterior = self.corpo[index+1]-bloco
                bloco_proximo = self.corpo[index-1]-bloco
                if bloco_anterior.x==bloco_proximo.x and bloco_anterior.y>bloco_proximo.y:
                    self.screen.blit(self.metro_meio_c, vagao_rect)
                elif bloco_anterior.x==bloco_proximo.x and bloco_anterior.y<bloco_proximo.y:
                    self.screen.blit(self.metro_meio_b, vagao_rect)
                elif bloco_anterior.y==bloco_proximo.y:
                     self.screen.blit(self.metro_meio_d, vagao_rect)
        # Cada vagão do trem é um bloco
    
    def mover_trem(self):
        if self.novo_vagao == True:
            corpo_copia = self.corpo[:]
            corpo_copia.insert(0,corpo_copia[0]+self.sentido)
            self.corpo = corpo_copia[:]
            self.novo_vagao = False
        else:
            corpo_copia = self.corpo[:-1]
            corpo_copia.insert(0,corpo_copia[0]+self.sentido)
            self.corpo = corpo_copia[:]
        # Quando o trem se move, o último vagão é eliminado e adiciona-se um vagão à frente dos outros(no começo da lista), que é uma cópia do primeiro vagão 
        # mais uma vez o sentido no qual o trem se move

    def adicionar_vagao(self):
        self.novo_vagao = True

    def relacao_frente(self):
        relacao = self.corpo[1] - self.corpo[0]
        if relacao == Vector2(0,1):
            self.frente = self.metro_frente_c
        elif relacao == Vector2(0,-1):
            self.frente = self.metro_frente_b
        elif relacao == Vector2(1, 0):
            self.frente = self.metro_frente_e
        elif relacao == Vector2(-1, 0):
            self.frente = self.metro_frente_d

    def relacao_tras(self):
        relacao = self.corpo[-1] - self.corpo[-2]
        if relacao == Vector2(0,1):
            self.tras = self.metro_tras_c
        elif relacao == Vector2(0,-1):
            self.tras = self.metro_tras_b
        elif relacao == Vector2(1, 0):
            self.tras = self.metro_tras_e
        elif relacao == Vector2(-1, 0):
            self.tras = self.metro_tras_d

    
        

class Partida:
    def __init__(self, cn, cs, screen):
        self.trem = Trem(cn, cs, screen) # Cria um objeto da classe Trem
        self.passageiro = Passageiro(cn, cs, screen) # Cria um objeto da classe Passageiro
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado


    def atualizar(self):
        self.trem.mover_trem()
        self.checar_colisao()

    def desenhar_elementos(self):
        self.passageiro.desenhar_passageiro() # Desenha o passageiro
        self.trem.desenhar_trem() # Desenha o trem

    def checar_colisao(self):
        if self.passageiro.pos == self.trem.corpo[0]:
            self.passageiro.sortear(self.cn, self.cs, self.screen)
            self.trem.adicionar_vagao()




