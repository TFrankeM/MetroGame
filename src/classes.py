import pygame
import random
from pygame.math import Vector2
import time

class Passageiro:
    """ Os objetos dessa classe são carregados na tela e interagem com objetos da classe Trem quando ambos ocupam as mesmas coordenadas.
    """
    def __init__(self, cn=1, cs=1, screen=None):
        """ Construtor da classe

        Args:
            cn (int): Número de células da janela do programa. Defaults to 1.
            cs (int): Tamanho das células. Defaults to 1.
            screen (pygame.Surface): Janela do programa. Defaults to None.
        """
        self.sortear(cn, cs, screen)
        # A posição é randomizada dentro dos limites da tela e guardada num vetor.
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        
    def definir_imagens_passageiro(self):
        """ Carrega a imagem correspondente aos objetos da classe
        """
        self.pessoa = pygame.image.load('src/metro_imagens/passageiro.png').convert_alpha()
        # Carrega a imagem que representa o objeto passageiro 

    def desenhar_passageiro(self):
        """ Gera um retângulo para conter a imagem do objeto da classe e garrega essa imagem na tela
        """
        passageiro_rect = pygame.Rect(int(self.x*self.cs), int(self.y*self.cs), self.cs, self.cs)
        self.pessoa = pygame.transform.scale(self.pessoa, (self.cs, self.cs))
        self.screen.blit(self.pessoa, passageiro_rect)
        # O passageiro é renderizado como um bloco colorido

    def sortear(self, cn, cs, screen):
        """ Define a posição do objeto na tela do jogo

        Args:
            cn (int): Número de células da janela do programa
            cs (int): Tamanho das células
            screen (pygame.Surface): Janela do programa
        """
        self.x = random.randint(2, cn-3)
        self.y = random.randint(2, cn-3)
        self.pos = Vector2(self.x, self.y)
        
class Trem:
    """ Os objetos dessa classe se movem pela janela
    """
    def __init__(self, cn=1, cs=1, screen=None):
        """ Construtor da classe

        Args:
            cn (int, optional): Número de células da janela do programa. Defaults to 1.
            cs (int, optional): Tamanho das células. Defaults to 1.
            screen (pygame.Surface, optional): Janela do programa. Defaults to None.
        """
        self.corpo = [Vector2(5,2), Vector2(4,2), Vector2(3,2)]
        self.sentido = Vector2(1,0)
        self.sentido_antes = Vector2(1,0)
        # O trem começa com três blocos numa posição definida, que compõem seu corpo, e com um sentido de movimanto também já definido
        # A variável sentido_antes mantém o sentido anterior e serve para comparação na hora de desenhar os vagões
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.novo_vagao = False
        # O objeto recebe o tamanho da tela emk relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        
    
    def definir_imagens_trem(self):
        """Carrega as imagens correspondentes aos objetos da classe
        """
        self.metro_frente_d = pygame.image.load('src/metro_imagens/metro_direita.png').convert_alpha()
        self.metro_frente_d = pygame.transform.scale(self.metro_frente_d, (self.cs,self.cs))
        self.metro_tras_d = pygame.image.load('src/metro_imagens/metro_esquerda.png').convert_alpha()
        self.metro_tras_d = pygame.transform.scale(self.metro_tras_d, (self.cs,self.cs))
        self.metro_meio_d = pygame.image.load('src/metro_imagens/metro_meio.png').convert_alpha()
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
        """ Gera um retângulo para conter as imagens do objeto da classe e garrega essas imagens na tela, de acordo com a posição das células que o objeto ocupa
        """
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
                self.relacao_meio(index, bloco)
                self.screen.blit(self.meio, vagao_rect)
                
        # Cada vagão do trem é um bloco
    
    
    def mover_trem(self):
        """ Modifica as células que compõem a imagem do objeto na tela
        """
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
        """ Torna True o valor da variável do objeto que descreve a necessidade de se adicionar células à sua imagem
        """
        self.novo_vagao = True

    def relacao_frente(self):
        """ Define que imagem deve ser carregada na primeira célula ocupada pelo objeto na tela, com base na próxima célula ocupada
        """
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
        """ Define que imagem deve ser carregada na última célula ocupada pelo objeto na tela, com base na célula anterior ocupada
        """
        relacao = self.corpo[-1] - self.corpo[-2]
        if relacao == Vector2(0,1):
            self.tras = self.metro_tras_c
        elif relacao == Vector2(0,-1):
            self.tras = self.metro_tras_b
        elif relacao == Vector2(1, 0):
            self.tras = self.metro_tras_e
        elif relacao == Vector2(-1, 0):
            self.tras = self.metro_tras_d

    def relacao_meio(self, index, bloco):
        """_summary_

        Args:
            index (_type_): _description_
            bloco (_type_): _description_
        """
        bloco_anterior = self.corpo[index+1]-bloco
        bloco_proximo = self.corpo[index-1]-bloco
        if bloco_anterior.x==bloco_proximo.x and bloco_anterior.y>bloco_proximo.y:
            self.meio = self.metro_meio_c
        elif bloco_anterior.x==bloco_proximo.x and bloco_anterior.y<bloco_proximo.y:
            self.meio = self.metro_meio_b
        elif bloco_anterior.y==bloco_proximo.y:
            self.meio = self.metro_meio_d
        else:
            if bloco_anterior.x == -1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == -1:
                self.meio = self.conexao_ec
            elif bloco_anterior.x == -1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == -1:
                self.meio = self.conexao_be
            elif bloco_anterior.x == 1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == 1:
                self.meio = self.conexao_cd
            elif bloco_anterior.x == 1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == 1:
                self.meio = self.conexao_db

class Partida:
    def __init__(self, cn, cs, screen, fonte):
        self.trem = Trem(cn, cs, screen) # Cria um objeto da classe Trem
        self.trem.definir_imagens_trem()
        self.passageiro = Passageiro(cn, cs, screen) # Cria um objeto da classe Passageiro
        self.passageiro.definir_imagens_passageiro()
        self.parede = Parede(cn, cs, screen, 1)
        self.parede.definir_imagens_parede()
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        self.ativo = False
        self.pausa = False
        self.fonte = fonte
        self.musica = pygame.mixer.Sound('src/metro_sons/musica_fundo.mpeg')
        self.batida = pygame.mixer.Sound('src/metro_sons/196734__paulmorek__crash-01.wav')
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
        self.parede.desenhar_parede()
        self.trem.desenhar_trem() # Desenha o trem
        self.desenhar_pontuacao()

    def checar_colisao(self):
        if self.passageiro.pos == self.trem.corpo[0]:
            while self.passageiro.pos in self.trem.corpo or self.passageiro.pos in self.parede.corpo:
                self.passageiro.sortear(self.cn, self.cs, self.screen)
                #
            self.trem.adicionar_vagao()
            
    
    def checar_falha(self):
        if not 1 < self.trem.corpo[0].x < self.cn-2 or not 1 < self.trem.corpo[0].y < self.cn-2:
            self.game_over()
        for bloco in self.trem.corpo[1:]:
            if bloco == self.trem.corpo[0]:
                self.game_over()
        if self.trem.corpo[0] in self.parede.corpo:
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
            
class Menu:
    def __init__(self, cn, cs, screen, fontes):
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.fontes = fontes
        self.comecar = False
        self.pausa = False
        self.abertura()
        
        
    def abertura(self):
        self.musica = pygame.mixer.Sound('src/metro_sons/chegada.mp3')
        self.musica.play()
    
    def desenhar_elementos(self):
        if self.comecar == False:
            self.desenhar_tela_inicial()
        elif self.comecar == True and self.pausa == True:
            self.pausar_jogo()
            
    
    
    def desenhar_tela_inicial(self):
        
        fundo = pygame.image.load('src/metro_imagens/estação-de-metro-vazia-dos-desenhos-animados-ilustração-do-vetor-144632670.jpg').convert_alpha()
        fundo_rect = pygame.Rect(0, 0, self.cs*self.cn, self.cs*self.cn)
        fundo = pygame.transform.scale(fundo, (self.cs*self.cn, self.cs*self.cn))
        self.screen.blit(fundo, fundo_rect)
    
    
        titulo = "Metrô"
        titulo_superficie = self.fontes[0].render(titulo, True, (250,100,0))
        titulo_rect = titulo_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 5*self.cs))
        self.screen.blit(titulo_superficie, titulo_rect)
    
        instrucao = "Pressione a barra de espaço"
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0,80,200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 12*self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
    def comecar_fase(self):
        self.comecar = True
        
    def pausar_jogo(self):
        menu_pausa_rect = pygame.Rect(self.cs*5, self.cs*4, self.cs*15, self.cs*17)
        pygame.draw.rect(self.screen, (200,200,50), menu_pausa_rect)
        
        pausa_1 = "O trem fez uma parada"
        pausa_2 = "Aguarde"
        pausa_superficie = self.fontes[1].render(pausa_1, True, (250,100,0))
        pausa_rect = pausa_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 5*self.cs))
        self.screen.blit(pausa_superficie, pausa_rect)
        pausa_superficie = self.fontes[1].render(pausa_2, True, (250,100,0))
        pausa_rect = pausa_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 6*self.cs))
        self.screen.blit(pausa_superficie, pausa_rect)
        


class Parede:
    def __init__(self, cn, cs, screen, fase):
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.corpo = []
        self.fase = fase
        self.adicionar_parede()
        
    def definir_imagens_parede(self):
        self.parede = pygame.image.load('src/metro_imagens/images.jfif').convert_alpha()
    
    def desenhar_parede(self):
        for bloco in self.corpo:
            parede_rect = pygame.Rect(int(bloco.x*self.cs), int(bloco.y*self.cs), self.cs, self.cs)
            self.parede = pygame.transform.scale(self.parede, (self.cs, self.cs))
            self.screen.blit(self.parede, parede_rect)
    
    def adicionar_parede(self):
        if self.fase == 0:
            pass
        elif self.fase == 1:
            self.corpo += [Vector2(5,5), Vector2(5,6), Vector2(4,5)]
            self.corpo += [Vector2(19,5), Vector2(19,6), Vector2(20,5)]
            self.corpo += [Vector2(5,19), Vector2(5,18), Vector2(4,19)]
            self.corpo += [Vector2(19,19), Vector2(19,18), Vector2(20,19)]
            self.corpo += [Vector2(7,8), Vector2(17,8), Vector2(7,16), Vector2(17,16)]
            self.corpo += [Vector2(9,10), Vector2(15,10), Vector2(9,14), Vector2(15,14)]
            self.corpo += [Vector2(11,3), Vector2(13,3), Vector2(11,21), Vector2(13,21)]
            self.corpo += [Vector2(3,11), Vector2(3,13), Vector2(21,11), Vector2(21,13)]

