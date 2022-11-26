import pygame
import random
from pygame.math import Vector2
import time

class Passageiro:
    def __init__(self, cn, cs, screen):
        self.sortear(cn, cs, screen)
        # A posição é randomizada dentro dos limites da tela e guardada num vetor.
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        
    def definir_imagens_passageiro(self):
        self.pessoa = pygame.image.load('src/metro_imagens/passageiro.png').convert_alpha()

    def desenhar_passageiro(self):
        passageiro_rect = pygame.Rect(int(self.x*self.cs), int(self.y*self.cs), self.cs, self.cs)
        self.pessoa = pygame.transform.scale(self.pessoa, (self.cs, self.cs))
        self.screen.blit(self.pessoa, passageiro_rect)
        # O passageiro é renderizado como um bloco colorido

    def sortear(self, cn, cs, screen):
        self.x = random.randint(2, cn-3)
        self.y = random.randint(2, cn-3)
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
        
    
    def definir_imagens_trem(self):
        self.metro_frente_d = pygame.image.load('src/metro_imagens/metro_direita.png').convert_alpha()
        self.metro_frente_d = pygame.transform.scale(self.metro_frente_d, (self.cs,self.cs))
        self.metro_tras_d = pygame.image.load('src/metro_imagens/metro_esquerda.png').convert_alpha()
        self.metro_tras_d = pygame.transform.scale(self.metro_tras_d, (self.cs,self.cs))
        self.metro_meio_d = pygame.image.load('src/metro_imagens/metro_meio_direita_esquerda.png').convert_alpha()
        self.metro_meio_d = pygame.transform.scale(self.metro_meio_d, (self.cs,self.cs))
        
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
        
        self.conexao_db = pygame.image.load('src/metro_imagens/curva.png').convert_alpha()
        self.conexao_db = pygame.transform.scale(self.conexao_db, (self.cs,self.cs))
        self.conexao_cd = pygame.transform.rotate(self.conexao_db, 90)
        self.conexao_ec = pygame.transform.rotate(self.conexao_db, 180)
        self.conexao_be = pygame.transform.rotate(self.conexao_db, 270)
    
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
                else:
                    if bloco_anterior.x == -1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == -1:
                        self.screen.blit(self.conexao_ec, vagao_rect)
                    elif bloco_anterior.x == -1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == -1:
                        self.screen.blit(self.conexao_be, vagao_rect)
                    elif bloco_anterior.x == 1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == 1:
                        self.screen.blit(self.conexao_cd, vagao_rect)
                    elif bloco_anterior.x == 1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == 1:
                        self.screen.blit(self.conexao_db, vagao_rect)
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
    def __init__(self, cn, cs, screen, fonte):
        self.trem = Trem(cn, cs, screen) # Cria um objeto da classe Trem
        self.trem.definir_imagens_trem()
        self.passageiro = Passageiro(cn, cs, screen) # Cria um objeto da classe Passageiro
        self.passageiro.definir_imagens_passageiro()
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        self.ativo = True
        self.pausa = False
        self.fonte = fonte
        self.musica = pygame.mixer.Sound('src/sons/musica_fundo.mpeg')
        self.musica.play()
        self.batida = pygame.mixer.Sound('src/sons/196734__paulmorek__crash-01.wav')
        self.borda = pygame.image.load('src/metro_imagens/linha_amarela_vao.png').convert_alpha()
        self.borda = pygame.transform.scale(self.borda, (cs,cs))


    def atualizar(self):
        if self.ativo == True and self.pausa == False:
            self.trem.mover_trem()
            self.checar_colisao()
            self.checar_falha()

    def desenhar_elementos(self):
        self.desenhar_borda()
        self.passageiro.desenhar_passageiro() # Desenha o passageiro
        self.trem.desenhar_trem() # Desenha o trem
        self.desenhar_pontuacao()

    def checar_colisao(self):
        if self.passageiro.pos == self.trem.corpo[0]:
            while self.passageiro.pos in self.trem.corpo:
                self.passageiro.sortear(self.cn, self.cs, self.screen)
                #
            self.trem.adicionar_vagao()
            
    
    def checar_falha(self):
        if not 1 < self.trem.corpo[0].x < self.cn-2 or not 1 < self.trem.corpo[0].y < self.cn-2:
            self.game_over()
        for bloco in self.trem.corpo[1:]:
            if bloco == self.trem.corpo[0]:
                self.game_over()
    
    def game_over(self):
        self.batida.play()
        self.ativo = False
        self.musica.stop()
        time.sleep(1)
        self.batida.stop()
        

    def desenhar_pontuacao(self):
        pontuacao = str(len(self.trem.corpo)-3)
        pontuacao_superficie = self.fonte.render(pontuacao, True, (0,0,0))
        pontuacao_rect = pontuacao_superficie.get_rect(center = (int(self.cs*self.cn - 60), int(20)))
        self.screen.blit(pontuacao_superficie, pontuacao_rect)

    def desenhar_borda(self):
        inicio = 1
        while inicio < self.cn-1:
            borda_rect = pygame.Rect(int(inicio*self.cs), int(1*self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            borda_rect = pygame.Rect(int(inicio*self.cs), int((self.cn-2)*self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            borda_rect = pygame.Rect(int(1*self.cs), int(inicio*self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            borda_rect = pygame.Rect(int((self.cn-2)*self.cs), int(inicio*self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            inicio+=1
            
