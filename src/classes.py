import pygame
import random
from pygame.math import Vector2
import time
from datetime import date
import re
import pandas as pd

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
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        
    def definir_imagens_passageiro(self):
        """ Carrega a imagem correspondente aos objetos da classe
        """
        # Carregando as imagens das pessoas/passageiros em uma lista
        self.pessoas = [pygame.image.load('src/imagens/passageiros/p1.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p2.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p3.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p4.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p5.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p6.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p7.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p8.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p9.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p10.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p11.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p12.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p13.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p14.png').convert_alpha(),
                        pygame.image.load('src/imagens/passageiros/p15.png').convert_alpha()]
        # Sorteia o primeiro passageiro
        self.pessoa = self.pessoas[random.randint(0,14)]


    def desenhar_passageiro(self):
        """ Gera um retângulo para conter a imagem do objeto da classe e garrega essa imagem na tela
        """
        passageiro_rect = pygame.Rect(int(self.x * self.cs), int(self.y * self.cs), self.cs, self.cs)
        self.pessoa = pygame.transform.scale(self.pessoa, (self.cs, self.cs))
        self.screen.blit(self.pessoa, passageiro_rect)
        # O passageiro é renderizado como um bloco colorido

    def sortear(self, cn):
        """ Define a posição do objeto na tela do jogo e a sua imagem

        Args:
            cn (int): Número de células da janela do programa
            cs (int): Tamanho das células
            screen (pygame.Surface): Janela do programa
        """
        # Sorteia a posição do passageiro
        self.x = random.randint(2, cn - 3)
        self.y = random.randint(2, cn - 3)
        self.pos = Vector2(self.x, self.y)
    
        # Sorteia a imagem do 2º passageiro em diante
        self.pessoa = self.pessoas[random.randint(0,14)]

    def __del__(self):
        pass
        
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
        # Carregando as imagens da frente do trem
        self.frente_direita = pygame.image.load('src/imagens/metro/horizontal_frente.png').convert_alpha()
        self.frente_direita = pygame.transform.scale(self.frente_direita, (self.cs,self.cs))
        self.frente_esquerda = pygame.transform.flip(self.frente_direita, True, False)
        self.frente_emcima = pygame.image.load('src/imagens/metro/vertical_emcima.png').convert_alpha()
        self.frente_emcima = pygame.transform.scale(self.frente_emcima, (self.cs,self.cs))
        self.frente_embaixo = pygame.image.load('src/imagens/metro/vertical_embaixo.png').convert_alpha()
        self.frente_embaixo = pygame.transform.scale(self.frente_embaixo, (self.cs,self.cs))

        # Carregando as imagens da traseira do trem
        self.traseira_esquerda = pygame.image.load('src/imagens/metro/horizontal_traseira.png').convert_alpha()
        self.traseira_esquerda = pygame.transform.scale(self.traseira_esquerda, (self.cs,self.cs))
        self.traseira_direita = pygame.transform.flip(self.traseira_esquerda, True, False)
        self.traseira_emcima = pygame.image.load('src/imagens/metro/vertical_emcima.png').convert_alpha()
        self.traseira_emcima = pygame.transform.scale(self.traseira_emcima, (self.cs,self.cs))
        self.traseira_embaixo = pygame.image.load('src/imagens/metro/vertical_embaixo.png').convert_alpha()
        self.traseira_embaixo = pygame.transform.scale(self.traseira_embaixo, (self.cs,self.cs))

        # Carregando vagão do meio do trem
        self.meio_horizontal = pygame.image.load('src/imagens/metro/horizontal_meio.png').convert_alpha()
        self.meio_horizontal = pygame.transform.scale(self.meio_horizontal, (self.cs,self.cs))
        self.meio_vertical = pygame.image.load('src/imagens/metro/vertical_meio.png').convert_alpha()
        self.meio_vertical = pygame.transform.scale(self.meio_vertical, (self.cs,self.cs))

        # Carregando curvas/quinas
        # dc = direita, em cima
        # db = direita, em baixo
        # ec = erquerda, em cima
        # eb = esquerda, em baixo
        self.conexao_dc = pygame.image.load('src/imagens/metro/curva.png').convert_alpha()
        self.conexao_dc = pygame.transform.scale(self.conexao_dc, (self.cs, self.cs))
        self.conexao_db = pygame.transform.rotate(self.conexao_dc, 270)
        self.conexao_ec = pygame.transform.rotate(self.conexao_dc, 90)
        self.conexao_eb = pygame.transform.rotate(self.conexao_dc, 180)
    
    def desenhar_trem(self):
        """ Gera um retângulo para conter as imagens do objeto da classe e garrega essas imagens na tela, de acordo com a posição das células que o objeto ocupa
        """
        self.relacao_frente()
        self.relacao_traseira()
        for index, bloco in enumerate(self.corpo):
            x_pos = int(bloco.x * self.cs)
            y_pos = int(bloco.y * self.cs)
            vagao_rect = pygame.Rect(x_pos, y_pos, self.cs, self.cs)
            if index == 0:
                self.screen.blit(self.frente, vagao_rect)
            elif index == len(self.corpo) -1:
                self.screen.blit(self.traseira, vagao_rect)
            else:
                self.relacao_meio(index, bloco)
                self.screen.blit(self.meio, vagao_rect)
                
        # Cada vagão do trem é um bloco
    
    
    def mover_trem(self):
        """ Modifica as células que compõem a imagem do objeto na tela
        """
        if self.novo_vagao == True:
            corpo_copia = self.corpo[:]
            corpo_copia.insert(0, corpo_copia[0] + self.sentido)
            self.corpo = corpo_copia[:]
            self.novo_vagao = False
        else:
            corpo_copia = self.corpo[:-1]
            corpo_copia.insert(0, corpo_copia[0] + self.sentido)
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
            self.frente = self.frente_emcima
        elif relacao == Vector2(0,-1):
            self.frente = self.frente_embaixo
        elif relacao == Vector2(1, 0):
            self.frente = self.frente_esquerda
        elif relacao == Vector2(-1, 0):
            self.frente = self.frente_direita

    def relacao_traseira(self):
        """ Define que imagem deve ser carregada na última célula ocupada pelo objeto na tela, com base na célula anterior ocupada
        """
        relacao = self.corpo[-2] - self.corpo[-1]
        if relacao == Vector2(0,1):
            self.traseira = self.traseira_emcima
        elif relacao == Vector2(0,-1):
            self.traseira = self.traseira_embaixo
        elif relacao == Vector2(1, 0):
            self.traseira = self.traseira_esquerda
        elif relacao == Vector2(-1, 0):
            self.traseira = self.traseira_direita

    def relacao_meio(self, index, bloco):
        """_summary_

        Args:
            index (_type_): _description_
            bloco (_type_): _description_
        """
        bloco_anterior = self.corpo[index+1] - bloco
        bloco_proximo = self.corpo[index-1] - bloco
        if bloco_anterior.x == bloco_proximo.x:
            self.meio = self.meio_vertical
        elif bloco_anterior.y == bloco_proximo.y:
            self.meio = self.meio_horizontal
        else:
            if bloco_anterior.x == -1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == -1:
                self.meio = self.conexao_ec
            elif bloco_anterior.x == -1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == -1:
                self.meio = self.conexao_eb
            elif bloco_anterior.x == 1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == 1:
                self.meio = self.conexao_dc
            elif bloco_anterior.x == 1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == 1:
                self.meio = self.conexao_db
                
    def __del__(self):
        pass

class Partida:
    def __init__(self, cn, cs, screen, fonte):
        self.trem = Trem(cn, cs, screen) # Cria um objeto da classe Trem
        self.trem.definir_imagens_trem()
        
        self.obstaculo = Obstaculo(cn, cs, screen, 1)
        self.obstaculo.definir_imagens_obstaculo()

        self.passageiro = Passageiro(cn, cs, screen) # Cria um objeto da classe Passageiro
        self.passageiro.definir_imagens_passageiro()
        self.passageiro.sortear(cn)

        # Checar se o passageiro está sobre o trem ou algum obstáculo
        while self.passageiro.pos in self.trem.corpo or self.passageiro.pos in self.obstaculo.posicoes_objetos:
            self.passageiro.sortear(cn)
        
        self.cn = cn
        self.cs = cs
        self.screen = screen
        # O objeto recebe o tamanho da tela em relação às células, o tamanho das células no jogo e a superfície onde ele será desenhado
        self.ativo = False
        self.pausa = False
        self.fonte = fonte
        self.musica = pygame.mixer.Sound('src/sons/musica_fundo.mpeg')
        self.batida = pygame.mixer.Sound('src/sons/batida.wav')
        self.borda = pygame.image.load('src/imagens/obstaculos/borda.jpg').convert_alpha()
        self.borda = pygame.transform.scale(self.borda, (cs,cs))
        self.pontuacao = 0


    def atualizar(self):
        if self.ativo == True and self.pausa == False:
            self.trem.mover_trem()
            self.checar_colisao()
            self.checar_falha()

    def desenhar_elementos(self):
        self.fundo()
        self.desenhar_borda()
        self.passageiro.desenhar_passageiro() # Desenha o passageiro
        self.obstaculo.desenhar_obstaculo()
        self.trem.desenhar_trem() # Desenha o trem
        self.desenhar_pontuacao()

    def checar_colisao(self):
        if self.passageiro.pos == self.trem.corpo[0]:
            while self.passageiro.pos in self.trem.corpo or self.passageiro.pos in self.obstaculo.posicoes_objetos:
                self.passageiro.sortear(self.cn)
                #
            self.trem.adicionar_vagao()
            
    
    def checar_falha(self):
        if not 1 < self.trem.corpo[0].x < self.cn-2 or not 1 < self.trem.corpo[0].y < self.cn-2:
            self.game_over()
        for bloco in self.trem.corpo[1:]:
            if bloco == self.trem.corpo[0]:
                self.game_over()
                
        if self.trem.corpo[0] in self.obstaculo.posicoes_objetos:
            self.game_over()
    
    def game_over(self):
        self.batida.play()
        self.ativo = False
        self.musica.stop()
        time.sleep(1)
        self.batida.stop()

    def desenhar_pontuacao(self):
        self.pontuacao = str(len(self.trem.corpo) - 3)
        pontuacao_superficie = self.fonte.render(self.pontuacao, True, (0,0,0))
        pontuacao_rect = pontuacao_superficie.get_rect(center = (int(self.cs * self.cn - 60), int(20)))
        self.screen.blit(pontuacao_superficie, pontuacao_rect)

    def desenhar_borda(self):
        inicio = 1
        while inicio < self.cn - 1:
            # Borda superior
            borda_rect = pygame.Rect(int(inicio * self.cs), int(1 * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda inferior
            borda_rect = pygame.Rect(int(inicio * self.cs), int((self.cn - 2) * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda esquerda
            borda_rect = pygame.Rect(int(1 * self.cs), int(inicio * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda direita
            borda_rect = pygame.Rect(int((self.cn - 2) * self.cs), int(inicio * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            inicio += 1
    
    # Gera o fundo quadriculado
    def fundo(self):
        
        self.screen.fill((175,205,70)) # Preenche a tela com cor
        cor_grama = (167, 209, 61)
        for linha in range(self.cn):
            if linha % 2 == 0:
                for col in range(self.cn):
                    if col % 2 == 0:
                        grama_rect = pygame.Rect(col * self.cs, linha * self.cs, self.cs, self.cs)
                        pygame.draw.rect(self.screen, cor_grama, grama_rect)
            else:
                for col in range(self.cn):
                    if col % 2 != 0:
                        grama_rect = pygame.Rect(col * self.cs, linha * self.cs, self.cs, self.cs)
                        pygame.draw.rect(self.screen, cor_grama, grama_rect )
            
    def __del__(self):
        self.passageiro.__del__()
        self.obstaculo.__del__()
        self.trem.__del__()
        #print(f"A partida acabou.")

class Menu:
    def __init__(self, cn, cs, screen, fontes):
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.fontes = fontes
        self.jogo = "Início"
        self.pausa = False
        self.abertura()
        self.nome = "Jogador"
        self.selecionado = True
        
    def abertura(self):
        self.musica = pygame.mixer.Sound('src/sons/chegada.mp3')
        self.musica.play()
    
    def desenhar_elementos(self):
        if self.jogo == "Início":
            self.desenhar_tela_inicial()
            self.cadastrar()
        elif self.jogo == "Meio" and self.pausa == True:
            self.pausar_jogo()
        elif self.jogo =="Fim":
            self.fim_jogo()
            
    def desenhar_tela_inicial(self):
        fundo = pygame.image.load('src/imagens/estação_menu.jpg').convert_alpha()
        fundo_rect = pygame.Rect(0, 0, self.cs*self.cn, self.cs*self.cn)
        fundo = pygame.transform.scale(fundo, (self.cs*self.cn, self.cs*self.cn))
        self.screen.blit(fundo, fundo_rect)
    
        titulo = "Metrô"
        titulo_superficie = self.fontes[0].render(titulo, True, (250,100,0))
        titulo_rect = titulo_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 5*self.cs))
        self.screen.blit(titulo_superficie, titulo_rect)

        instrucao = "Bem-vindo"
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0,80,200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs*(self.cn/2-6)), 13*self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
        instrucao = ", o Maquinista."
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0,80,200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs*(7+self.cn/2)), 13*self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
        instrucao = "Pressione a barra de espaço e tenha um bom dia"
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0,80,200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 16*self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
    def comecar_fase(self):
        self.jogo = "Meio"
        
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
    
    def fim_jogo(self):
        menu_fim_rect = pygame.Rect(self.cs*5, self.cs*4, self.cs*15, self.cs*17)
        pygame.draw.rect(self.screen, (200,200,50), menu_fim_rect)

        self.recorde.ler()
        listas = self.recorde.df.values.tolist()
        for i in range(min(5, len(listas))):
            nome = listas[i][0]
            nome_superficie = self.fontes[1].render(nome, True, "blue")
            nome_rect = nome_superficie.get_rect(center = (int(self.cs*(self.cn/2-3)), (10+i)*self.cn))
            self.screen.blit(nome_superficie, nome_rect)
            linha = " | "+listas[i][1]+" | "+str(listas[i][2])
            recordes_superficie = self.fontes[1].render(linha, True, (0,0,0))
            recordes_rect = recordes_superficie.get_rect(center = (int(self.cs*(3+self.cn/2)), (10+i)*self.cn))
            self.screen.blit(recordes_superficie, recordes_rect)
    
    def registrar_recorde(self):
        self.recorde = Recorde(self.nome)
    
    def cadastrar(self):
        nome_superficie = self.fontes[1].render(self.nome, True, "yellow")
        self.nome_rect = nome_superficie.get_rect(center = (int(self.cs*(self.cn/2)), 13*self.cs))
        self.screen.blit(nome_superficie, self.nome_rect)
        if self.selecionado == True:
            pygame.draw.rect(self.screen, (200,150,0), self.nome_rect, 2)

class Obstaculo:
    def __init__(self, cn, cs, screen, fase):
        self.cn = cn
        self.cs = cs
        self.screen = screen
        self.corpo = {}
        self.fase = fase
        self.adicionar_obstaculo()
        
    def definir_imagens_obstaculo(self):
        self.obstaculos = [pygame.image.load('src/imagens/obstaculos/b1.png').convert_alpha(),
                          pygame.image.load('src/imagens/obstaculos/b2.png').convert_alpha(),
                          pygame.image.load('src/imagens/obstaculos/b3.png').convert_alpha()]
    
    def desenhar_obstaculo(self):
        for index, self.imagem in enumerate(self.obstaculos):
            for bloco in self.corpo[int(index)]:
                obstaculo_rect = pygame.Rect(int(bloco.x * self.cs), int(bloco.y * self.cs), self.cs, self.cs)
                self.imagem = pygame.transform.scale(self.imagem, (self.cs, self.cs))
                self.screen.blit(self.imagem, obstaculo_rect)
    
    def adicionar_obstaculo(self):
        # Obstáculos fase 0
        if self.fase == 0:
            pass
        # Obstáculos fase 1
        elif self.fase == 1:
            self.corpo[0] = [Vector2(5, 5), Vector2(5, 6), Vector2(4, 5), 
                               Vector2(19, 5), Vector2(19, 6), Vector2(20, 5), 
                               Vector2(19, 5), Vector2(19, 6), Vector2(20, 5),
                               Vector2(5, 19), Vector2(5, 18), Vector2(4, 19),
                               Vector2(19, 19), Vector2(19, 18), Vector2(20, 19)]
            self.corpo[1] = [Vector2(7, 8), Vector2(17, 8), Vector2(7, 16), Vector2(17, 16),
                               Vector2(9, 10), Vector2(15, 10), Vector2(9, 14), Vector2(15, 14)]
            self.corpo[2] = [Vector2(11, 3), Vector2(13, 3), Vector2(11, 21), Vector2(13, 21),
                               Vector2(3, 11), Vector2(3, 13), Vector2(21, 11), Vector2(21, 13)]

        # Colocar a posição dos obtáculos em uma lista para futura checagem de colisão
        self.posicoes_objetos = []
        for posicoes in self.corpo.values():
            for vetor in posicoes:
                self.posicoes_objetos.append(vetor)

    def __del__(self):
        pass


class Recorde:
    def __init__(self, nome):
        self.arquivo = open("registros.txt", "a+")
        self.nome = nome
    
    def escrever(self, pontuacao):
        self.arquivo.write(f"{self.nome}|{date.today()}|{pontuacao}\n")
        
    def ler(self):
        nomes=[]
        datas=[]
        pontos=[]
        self.arquivo.seek(0,0)
        for linha in self.arquivo.readlines():
            nome, data, ponto = re.split("\|", linha)
            ponto = re.sub("\n", "", ponto)
            nomes.append(nome)
            datas.append(data)
            pontos.append(int(ponto))
        dic = {"Jogador":nomes, "Data":datas, "Pontuação":pontos}
        self.df = pd.DataFrame(dic)
        self.df.sort_values(by="Data", axis = 0, ascending=False, inplace=True)
        self.df.sort_values(by="Pontuação", axis = 0, ascending=False, inplace=True)
        self.df.drop_duplicates(subset="Jogador", inplace=True)
    
    def __del__(self):
        #print(f"O recorde cumpriu sua função.")
        #print(f"O recorde foi registrado.")
        pass
