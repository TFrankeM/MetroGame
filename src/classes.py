import pygame
import random
from pygame.math import Vector2
import time
from datetime import date
import re
import pandas as pd


class Passageiro:
    """ Os objetos dessa classe são carregados na tela e interagem com objetos da classe Trem quando 
        ambos ocupam as mesmas coordenadas.
    """
    def __init__(self, cn = 1, cs = 1, screen = None):
        """ Construtor da classe.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Passageiro.
            cn (int): Número de células da janela do programa. Defaults to 1.
            cs (int): Tamanho das células. Defaults to 1.
            screen (pygame.Surface): Janela do programa. Defaults to None.
        """
        # Objetos recebem a quantidade e o tamanho de cada célula e o tamanho da tela do jogo.
        self.cn = cn    
        self.cs = cs
        self.screen = screen    # screen = (cn * cs, cn * cs)
        
        
    def definir_imagens_passageiro(self):
        """ Carrega a imagem correspondente aos objetos da classe

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Passageiro.
        """
        # Carregando as imagens das pessoas/passageiros em uma lista.
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


    def desenhar_passageiro(self):
        """ Gera um objeto "Rect" para armazenar e manipular uma área retangular que contém a 
            imagem do passageiro e a carregar na tela.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Passageiro.
        """
        # Cria o objeto retangular:
        # nome_retangulo = pygame.Rect(coordenada x, coordenada y, largura, altura).
        passageiro_rect = pygame.Rect(int(self.x * self.cs), int(self.y * self.cs), self.cs, self.cs)
        # Define as proporções da imagem do passageiro.
        self.pessoa = pygame.transform.scale(self.pessoa, (self.cs, self.cs))
        # O passageiro é renderizado no objeto retangular.
        self.screen.blit(self.pessoa, passageiro_rect)
        

    def sortear(self, cn):
        """ Define a posição do objeto (passageiro) na tela do jogo e a sua imagem.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Passageiro.
            cn (int): Número de células da janela do programa.
        """
        # Sorteia a posição do passageiro.
        self.x = random.randint(2, cn - 3)  # Coordenada x
        self.y = random.randint(2, cn - 3)  # Coordenada y
        self.pos = Vector2(self.x, self.y)  # Atribui a posição a um vetor
    
        # Sorteia a imagem do passageiro.
        self.pessoa = self.pessoas[random.randint(0, 14)]

    def __del__(self):
        pass



class Trem:
    """ Os objetos dessa classe (as composições do metrô) tem a habilidade de se mover pela tela de jogo.
    """
    def __init__(self, cn = 1, cs = 1, screen = None):
        """ Construtor da classe.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
            cn (int, optional): Número de células da janela do programa. Defaults to 1.
            cs (int, optional): Tamanho das células. Defaults to 1.
            screen (pygame.Surface, optional): Janela do programa. Defaults to None.
        """
        # Posição e tamanho do "corpo" original do metrô.
        self.corpo = [Vector2(5, 2), Vector2(4, 2), Vector2(3, 2)]
        # Sentido de movimanto predefinido.
        self.sentido = Vector2(1, 0)
        # "sentido_antes" mantém o sentido anterior e compara na hora de desenhar os vagões.
        self.sentido_antes = Vector2(1, 0)
        
        # Objetos recebem a quantidade e o tamanho de cada célula e o tamanho da tela do jogo.
        self.cn = cn
        self.cs = cs
        self.screen = screen        # screen = (cn * cs, cn * cs)
        self.novo_vagao = False     # Status padrão FALSO para adição de novo vagão ao metrô
        
    
    def definir_imagens_trem(self):
        """Carrega as imagens correspondentes aos objetos da classe Trem (os vagões).

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        # Carrega as imagens da frente do metrô.
        self.frente_direita = pygame.image.load('src/imagens/metro/horizontal_frente.png').convert_alpha()
        self.frente_direita = pygame.transform.scale(self.frente_direita, (self.cs,self.cs))
        self.frente_esquerda = pygame.transform.flip(self.frente_direita, True, False)
        self.frente_emcima = pygame.image.load('src/imagens/metro/vertical_emcima.png').convert_alpha()
        self.frente_emcima = pygame.transform.scale(self.frente_emcima, (self.cs,self.cs))
        self.frente_embaixo = pygame.image.load('src/imagens/metro/vertical_embaixo.png').convert_alpha()
        self.frente_embaixo = pygame.transform.scale(self.frente_embaixo, (self.cs,self.cs))

        # Carrega as imagens da traseira do metrô.
        self.traseira_esquerda = pygame.image.load('src/imagens/metro/horizontal_traseira.png').convert_alpha()
        self.traseira_esquerda = pygame.transform.scale(self.traseira_esquerda, (self.cs,self.cs))
        self.traseira_direita = pygame.transform.flip(self.traseira_esquerda, True, False)
        self.traseira_emcima = pygame.image.load('src/imagens/metro/vertical_emcima.png').convert_alpha()
        self.traseira_emcima = pygame.transform.scale(self.traseira_emcima, (self.cs,self.cs))
        self.traseira_embaixo = pygame.image.load('src/imagens/metro/vertical_embaixo.png').convert_alpha()
        self.traseira_embaixo = pygame.transform.scale(self.traseira_embaixo, (self.cs,self.cs))

        # Carrega as imagens do vagão do meio do metrô.
        self.meio_horizontal = pygame.image.load('src/imagens/metro/horizontal_meio.png').convert_alpha()
        self.meio_horizontal = pygame.transform.scale(self.meio_horizontal, (self.cs,self.cs))
        self.meio_vertical = pygame.image.load('src/imagens/metro/vertical_meio.png').convert_alpha()
        self.meio_vertical = pygame.transform.scale(self.meio_vertical, (self.cs,self.cs))

        # Carrega curvas/quinas
        # dc = direita, em cima
        # db = direita, em baixo
        # ec = erquerda, em cima
        # eb = esquerda, em baixo
        self.conexao_dc = pygame.image.load('src/imagens/metro/curva.png').convert_alpha()
        self.conexao_dc = pygame.transform.scale(self.conexao_dc, (self.cs, self.cs))
        self.conexao_db = pygame.transform.rotate(self.conexao_dc, 270)
        self.conexao_ec = pygame.transform.rotate(self.conexao_dc, 90)
        self.conexao_eb = pygame.transform.rotate(self.conexao_dc, 180)
    

    def relacao_frente(self):
        """ Relaciona a imagem correta a ser atribuida à primeira célula do metrô com base na próxima 
            posição a ser ocupada pela frente do metrô.
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        # Vetor resultante da substração da antiga posição da frente do metrô com a nova.
        relacao = self.corpo[1] - self.corpo[0]
        if relacao == Vector2(0,1):
            self.frente = self.frente_emcima        # Frente para cima
        elif relacao == Vector2(0,-1):
            self.frente = self.frente_embaixo       # Frente para baixo
        elif relacao == Vector2(1, 0):
            self.frente = self.frente_esquerda      # Frente para esquerda
        elif relacao == Vector2(-1, 0):
            self.frente = self.frente_direita       # Frente para direita


    def relacao_traseira(self):
        """ Relaciona a imagem correta a ser atribuida à última célula do metrô com base na próxima 
            posição a ser ocupada pela traseira do metrô.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        # Vetor resultante da substração da nova posição da traseira do metrô com a antiga.
        relacao = self.corpo[-2] - self.corpo[-1]
        if relacao == Vector2(0,1):
            self.traseira = self.traseira_emcima    # Traseira para cima
        elif relacao == Vector2(0,-1):
            self.traseira = self.traseira_embaixo   # Traseira para baixo
        elif relacao == Vector2(1, 0):
            self.traseira = self.traseira_esquerda  # Traseira para esquerda
        elif relacao == Vector2(-1, 0):
            self.traseira = self.traseira_direita   # Traseira para direita


    def relacao_meio(self, index, bloco):
        """ Relaciona a imagem correta a ser atribuida a cada célula do meio do metrô com base na sentido
            da celula anterior e da posterior.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
            index (int): índice de determinada composição do metrô.
            bloco (obj): contém as propriedades de determinada composição do metrô.
        """
        bloco_anterior = self.corpo[index + 1] - bloco      # Vagão anterior ao atual bloco
        bloco_proximo = self.corpo[index - 1] - bloco       # Vagão seguinte ao atual bloco
        if bloco_anterior.x == bloco_proximo.x:
            self.meio = self.meio_vertical                  # Atribui a imagem do vagão vertical
        elif bloco_anterior.y == bloco_proximo.y:
            self.meio = self.meio_horizontal                # Atribui a imagem do vagão horizontal
        else:
            if bloco_anterior.x == -1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == -1:
                self.meio = self.conexao_ec                 # Atribui a imagem da curva erquerda - em cima
            elif bloco_anterior.x == -1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == -1:
                self.meio = self.conexao_eb                 # Atribui a imagem da curva erquerda - embaixo
            elif bloco_anterior.x == 1 and bloco_proximo.y == -1 or bloco_anterior.y == -1 and bloco_proximo.x == 1:
                self.meio = self.conexao_dc                 # Atribui a imagem da curva direita - em cima
            elif bloco_anterior.x == 1 and bloco_proximo.y == 1 or bloco_anterior.y == 1 and bloco_proximo.x == 1:
                self.meio = self.conexao_db                 # Atribui a imagem da curva direita-embaixo
    
    
    def desenhar_trem(self):
        """ Desenha o metrô na tela. Para o primeiro e último vagão da composição, basta chamar as 
        funções self.relacao_frente() e self.relacao_traseira(). Para os vagões do meio primeiro 
        diferencia-se as curvas das retas.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        # Acionar as funções que atribuem a imagem correta da frente e da traseira do metrô.
        self.relacao_frente()
        self.relacao_traseira()

        # Define a coodenada de cada vagão do metrô.
        for index, bloco in enumerate(self.corpo):
            x_pos = int(bloco.x * self.cs)
            y_pos = int(bloco.y * self.cs)
            # Cria o objeto retangular:
            # nome_retangulo = pygame.Rect(coordenada x, coordenada y, largura, altura).
            vagao_rect = pygame.Rect(x_pos, y_pos, self.cs, self.cs)
            # Para a frente do metrô é adicionado sua imagem no objeto "Rect" correspondente.
            if index == 0:
                self.screen.blit(self.frente, vagao_rect)
            # Para a traseira do metrô é adicionado sua imagem no objeto "Rect" correspondente.
            elif index == len(self.corpo) - 1:
                self.screen.blit(self.traseira, vagao_rect)
            # Para cada vagão do meio é adicionado a imagem correspondente a uma reta ou a uma curva.
            else:
                self.relacao_meio(index, bloco)    # Determina a imagem correta: curva ou reta e sentido
                self.screen.blit(self.meio, vagao_rect)
    

    def adicionar_vagao(self):
        """ Muda para True o status da variável que descreve a necessidade de se adicionar um novo objeto,
            ou seja, um novo vagão.
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        self.novo_vagao = True

    
    def mover_trem(self):
        """ Modifica as células que compõem a imagem do objeto na tela

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Trem.
        """
        # Adiciona um novo vagão se o status para um novo vagão é TRUE.
        if self.novo_vagao == True:
            corpo_copia = self.corpo[:]
            corpo_copia.insert(0, corpo_copia[0] + self.sentido) # Novo vagão na primeira posição do metrô
            self.corpo = corpo_copia[:]
            self.novo_vagao = False                              # O status para novo vagão volta para FALSE
        # Movimento sem a adição de novo vagão.
        else:
            corpo_copia = self.corpo[:-1]                        # Copia-se o metrô exceto o último vagão
            corpo_copia.insert(0, corpo_copia[0] + self.sentido) # Adiciona-se uma nova composição na 1ª posição
            self.corpo = corpo_copia[:]                          # com sentido igual ao do metrô

                
    def __del__(self):
        pass



class Obstaculo:
    """ Os objetos dessa classe representam o fim de jogo no caso de uma colisão do metrô com um obstáculo.
    """
    def __init__(self, cn, cs, screen, fase):
        """ Construtor da classe.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
            cn (int, optional): Número de células da janela do programa. Defaults to 1.
            cs (int, optional): Tamanho das células. Defaults to 1.
            screen (pygame.Surface, optional): Janela do programa. Defaults to None.
            fase (int): Número da fase do jogo.
        """
        # Objetos recebem a quantidade e o tamanho de cada célula e o tamanho da tela do jogo.
        self.cn = cn
        self.cs = cs
        self.screen = screen        # screen = (cn * cs, cn * cs)
        self.corpo = {}             # Dicionário de objetos: as chaves são o tipo de obstáculo e os
                                    # valores uma lista das posições onde aparecem
        self.fase = fase            # Fase do jogo
        self.adicionar_obstaculo()  # Aciona a função de adição de obstáculos
        

    def definir_imagens_obstaculo(self):
        """ Carrega as imagens correspondentes aos objetos da classe Obstaculo.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.obstaculos = [pygame.image.load('src/imagens/obstaculos/b1.png').convert_alpha(),
                          pygame.image.load('src/imagens/obstaculos/b2.png').convert_alpha(),
                          pygame.image.load('src/imagens/obstaculos/b3.png').convert_alpha()]
    

    def adicionar_obstaculo(self):
        """ Adiciona a "self.corpo" um vetor posição dos obstáculos de acordo com a imagem de cada um.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        # Obstáculos fase 0.
        if self.fase == 0:
            pass
        # Obstáculos fase 1.
        elif self.fase == 1:
            # Cada chave do dicionário representa um obstáculo diferente. O valor é uma lista com as 
            # posições onde o obstáculo aparece.
            self.corpo[0] = [Vector2(5, 5), Vector2(5, 6), Vector2(4, 5), 
                             Vector2(19, 5), Vector2(19, 6), Vector2(20, 5), 
                             Vector2(19, 5), Vector2(19, 6), Vector2(20, 5),
                             Vector2(5, 19), Vector2(5, 18), Vector2(4, 19),
                             Vector2(19, 19), Vector2(19, 18), Vector2(20, 19)]
            self.corpo[1] = [Vector2(7, 8), Vector2(17, 8), Vector2(7, 16), Vector2(17, 16),
                             Vector2(9, 10), Vector2(15, 10), Vector2(9, 14), Vector2(15, 14)]
            self.corpo[2] = [Vector2(11, 3), Vector2(13, 3), Vector2(11, 21), Vector2(13, 21),
                             Vector2(3, 11), Vector2(3, 13), Vector2(21, 11), Vector2(21, 13)]
        # Obstáculos fase 2.
        if self.fase == 2:
            pass
        # Obstáculos fase 3.
        if self.fase == 3:
            pass
        # Obstáculos fase 4.
        if self.fase == 4:
            pass
        # Obstáculos fase 5.
        if self.fase == 5:
            pass

        # Coloca o vetor posição dos obtáculos em uma lista para futura checagem de colisão.
        self.posicoes_objetos = []
        for posicoes in self.corpo.values():
            for vetor in posicoes:
                self.posicoes_objetos.append(vetor)


    def desenhar_obstaculo(self):
        """ Gera um objeto "Rect" para armazenar e manipular uma área retangular que contém a 
            imagem do obstáculo e a carrega na tela.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        # O índice de cada imagem da lista de imagens de obstáculos é usado como chave para acessar as
        # posições onde o referido obstáculo aparece no mapa do jogo.
        for index, self.imagem in enumerate(self.obstaculos):
            for bloco in self.corpo[int(index)]:
                # Cria o objeto retangular:
                # nome_retangulo = pygame.Rect(coordenada x, coordenada y, largura, altura).
                obstaculo_rect = pygame.Rect(int(bloco.x * self.cs), int(bloco.y * self.cs), self.cs, self.cs)
                # Ajuste das proporções da imagem.
                self.imagem = pygame.transform.scale(self.imagem, (self.cs, self.cs))
                # Coloca a imagem no objeto Rect correspondente.
                self.screen.blit(self.imagem, obstaculo_rect)


    def __del__(self):
        pass



class Partida:
    """ Os acontecimentos do jogo se desenvolvem nos objetos dessa classe, responsáveis por acionar as 
    classes Trem, Obstaculo e Passageiro.
    """
    def __init__(self, cn, cs, screen, fonte):
        """ Construtor da classe.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
            cn (int, optional): Número de células da janela do programa. Defaults to 1.
            cs (int, optional): Tamanho das células. Defaults to 1.
            screen (pygame.Surface, optional): Janela do programa. Defaults to None.
            fonte: estilo de letra.
        """
        # Cria os objetos da classe Trem
        self.trem = Trem(cn, cs, screen)
        # Aciona "definir_imagens_trem()" que carrega as imagens do metrô.
        self.trem.definir_imagens_trem()
        
        # Cria os objetos da classe Obstaculo
        self.obstaculo = Obstaculo(cn, cs, screen, 1)
        # Aciona "definir_imagens_obstaculo()" que carrega as imagens dos obstaculos.
        self.obstaculo.definir_imagens_obstaculo()

        # Cria os objetos da classe Passageiro.
        self.passageiro = Passageiro(cn, cs, screen)
        # Aciona "definir_imagens_passageiro()" que carrega as imagens dos passageiros.
        self.passageiro.definir_imagens_passageiro()
        # Aciona "sortear()" que sorteia a posição e a imagem do novo obstáculo.
        self.passageiro.sortear(cn)

        # Uma nova posição será sorteada para o passageiro enquanto ele estiver sobre o metrô ou algum obstáculo.
        while self.passageiro.pos in self.trem.corpo or self.passageiro.pos in self.obstaculo.posicoes_objetos:
            self.passageiro.sortear(cn)
        
        # Objetos recebem a quantidade e o tamanho de cada célula e o tamanho da tela do jogo.
        self.cn = cn
        self.cs = cs
        self.screen = screen        # screen = (cn * cs, cn * cs)
        
        # O status padrão de atividade para a partida é FALSE.
        self.ativo = False
        # O status padrão de pausa para a partida é FALSE.
        self.pausa = False
        # Fonte da letra.
        self.fonte = fonte
        # Carregamento da música de fundo.
        self.musica = pygame.mixer.Sound('src/sons/musica_fundo.mpeg')
        # Carregamento do sons de batida.
        self.batida = pygame.mixer.Sound('src/sons/batida.wav')
        # Carregamento da imagem da borda do mapa.
        self.borda = pygame.image.load('src/imagens/obstaculos/borda.jpg').convert_alpha()
        self.borda = pygame.transform.scale(self.borda, (cs,cs))
        # Pontuação inicial:
        self.pontuacao = 0


    def atualizar(self):
        """ É responsável por, a cada ciclo do código, acionar o movimento do metrô, checar se houve 
            colisão com a borda do mapa, com obstáculos ou com o próprio corpo do metrô.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        # Se o status da partida é TRUE para ativo e FALSE para pausa há atualização.
        if self.ativo == True and self.pausa == False:
            self.trem.mover_trem()
            self.checar_colisao()
            self.checar_falha()


    def desenhar_elementos(self):
        """ Aciona os objetos responsáveis por gerar imagens, cores da tela de fundo e efeitos gráficos, 
        da borda, dos passageiros, dos obstáculos, do metrô e da pontuação.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.fundo()                                # Preenche a tela de fundo
        self.desenhar_borda()                       # Desenha a borda
        self.passageiro.desenhar_passageiro()       # Desenha o passageiros
        self.obstaculo.desenhar_obstaculo()         # Desenha os obstáculos
        self.trem.desenhar_trem()                   # Desenha o metrô
        self.desenhar_pontuacao()                   # Desenha a pontuação


    def checar_colisao(self):
        """ Se houver "colisão" entre a frente do metrô e um passageiro, aciona self.passageiro.sortear()
            até que a posição do novo passageiro não seja nem sobre o metrô nem sobre um obstáculo. Em 
            seguida, um novo vagão é adicionado ao metrô.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Partida.
        """
        if self.passageiro.pos == self.trem.corpo[0]:
            while self.passageiro.pos in self.trem.corpo or self.passageiro.pos in self.obstaculo.posicoes_objetos:
                self.passageiro.sortear(self.cn)
            
            # Quando o metrô pegar um passageiro, seu comprimento será aumentado em um vagão.
            self.trem.adicionar_vagao()
            
    
    def checar_falha(self):
        """ Se a frente do metrô não estiver no limite do mapa
            (1 < coordenada x e coordenada y da frente do metrô < numero de quadrados - 2) ou se ela ocupar 
            a mesma posição de alguma parte do corpo do metrô é acionado self.game_over().
            Além disso, o fim da partida também ocorre se a frente do metrô colidir com um obstáculo.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Partida.
        """
        # Game over se a frente do metrô não estiver dentro dos limites do mapa.
        if not 1 < self.trem.corpo[0].x < self.cn - 2 or not 1 < self.trem.corpo[0].y < self.cn - 2:
            self.game_over()
        # Game over se a frente do metrô estiver sobre outra parte do metrô.
        for bloco in self.trem.corpo[1:]:
            if bloco == self.trem.corpo[0]:
                self.game_over()
        # Game over se a frente do metrô colidir com obstáculo.
        if self.trem.corpo[0] in self.obstaculo.posicoes_objetos:
            self.game_over()
    

    def game_over(self):
        """ Se acionado, determina o fim da partida, acionando o áudio de batida, o fim da música de 
        fundo e definindo o estado da partida com desativada (self.ativo = False).

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Partida.
        """
        self.batida.play()  # Inicia o áudio da batida
        self.ativo = False  # Altera o status de atividade da partida
        self.musica.stop()  # Para a música de fundo
        time.sleep(1)
        self.batida.stop()  # Para o áudio da batida


    def desenhar_pontuacao(self):
        """ Gera um objeto "Rect" para armazenar e manipular uma área retangular que contém o número de
            passageiros. Em seguida, carrega o placar na tela.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        # Comprimento do metrô, descontados os vagões iniciais.
        self.pontuacao = str(len(self.trem.corpo) - 3)
        # Conteúdo exibido no objeto Rect.
        pontuacao_superficie = self.fonte.render(f"{self.pontuacao} passageiros", True, (0,0,0))
        # Contrução do  objeto Rect.
        pontuacao_rect = pontuacao_superficie.get_rect(center = (int(self.cs * self.cn - 110), int(20)))
        self.screen.blit(pontuacao_superficie, pontuacao_rect)


    def desenhar_borda(self):
        """ Gera objetos "Rect" para armazenar e manipular áreas retangulares que contém a borda do jogo.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        inicio = 1
        while inicio < self.cn - 1:
            # Borda superior.
            borda_rect = pygame.Rect(int(inicio * self.cs), int(1 * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda inferior.
            borda_rect = pygame.Rect(int(inicio * self.cs), int((self.cn - 2) * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda esquerda.
            borda_rect = pygame.Rect(int(1 * self.cs), int(inicio * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            # Borda direita.
            borda_rect = pygame.Rect(int((self.cn - 2) * self.cs), int(inicio * self.cs), self.cs, self.cs)
            self.screen.blit(self.borda, borda_rect)
            inicio += 1
    

    # Gera o fundo quadriculado
    def fundo(self):
        """ Gera objetos "Rect" para armazenar e manipular a primeira camada de áreas retangulares que 
            que formam a superfície do jogo.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        # Cor padrão de fundo.
        self.screen.fill((175,205,70))
        # Cor alternativa de fundo.
        cor_grama = (167, 209, 61)
        for linha in range(self.cn):
            # Células de linhas e colunas pares recebem a "cor_grama".
            if linha % 2 == 0:
                for col in range(self.cn):
                    if col % 2 == 0:
                        grama_rect = pygame.Rect(col * self.cs, linha * self.cs, self.cs, self.cs)
                        pygame.draw.rect(self.screen, cor_grama, grama_rect)
            # Células de linhas e colunas ímpares recebem a "cor_grama".
            else:
                for col in range(self.cn):
                    if col % 2 != 0:
                        grama_rect = pygame.Rect(col * self.cs, linha * self.cs, self.cs, self.cs)
                        pygame.draw.rect(self.screen, cor_grama, grama_rect )
            

    def __del__(self):
        """ Responsável por apagar os registros de uma partida assim que ela acaba.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.passageiro.__del__()
        self.obstaculo.__del__()
        self.trem.__del__()
        #print(f"A partida acabou.")



class Menu:
    """ Gera um objeto "Rect" para armazenar e manipular a primeira camada de áreas retangulares que 
        que formam a superfície do jogo.
    """
    def __init__(self, cn, cs, screen, fontes):
        """ Construtor da classe.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
            cn (int, optional): Número de células da janela do programa. Defaults to 1.
            cs (int, optional): Tamanho das células. Defaults to 1.
            screen (pygame.Surface, optional): Janela do programa. Defaults to None.
            fontes: estilos de letra.
        """
        # Objetos recebem a quantidade e o tamanho de cada célula e o tamanho da tela do jogo.
        self.cn = cn
        self.cs = cs
        self.screen = screen        # screen = (cn * cs, cn * cs)
        self.fontes = fontes
        # "self.jogo" recebe início, ou seja, menu
        self.jogo = "Menu"
        self.pausa = False
        self.abertura()
        self.nome = "Jogador"
        self.selecionado = True


    def abertura(self):
        """ Inicia a música de fundo do menu.

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.musica = pygame.mixer.Sound('src/sons/chegada.mp3')
        self.musica.play()
    

    def desenhar_elementos(self):
        """ 

        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        if self.jogo == "Menu":
            self.desenhar_tela_inicial()
            self.cadastrar()
        elif self.jogo == "Meio" and self.pausa == True:
            self.pausar_jogo()
        elif self.jogo == "Fim":
            self.fim_jogo()
            

    def desenhar_tela_inicial(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        fundo = pygame.image.load('src/imagens/estação_menu.jpg').convert_alpha()
        fundo_rect = pygame.Rect(0, 0, self.cs * self.cn, self.cs * self.cn)
        fundo = pygame.transform.scale(fundo, (self.cs * self.cn, self.cs * self.cn))
        self.screen.blit(fundo, fundo_rect)
    
        titulo = "Metrô"
        titulo_superficie = self.fontes[0].render(titulo, True, (250, 100, 0))
        titulo_rect = titulo_superficie.get_rect(center = (int(self.cs * (self.cn / 2)), 5 * self.cs))
        self.screen.blit(titulo_superficie, titulo_rect)

        instrucao = "Bem-vindo"
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0, 80, 200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs * (self.cn / 2 - 6)), 13 * self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
        instrucao = ", o Maquinista."
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0, 80, 200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs * (7 + self.cn / 2)), 13 * self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        
        instrucao = "Pressione a barra de espaço e tenha um bom dia"
        instrucao_superficie = self.fontes[1].render(instrucao, True, (0, 80, 200))
        instrucao_rect = instrucao_superficie.get_rect(center = (int(self.cs * (self.cn / 2)), 16 * self.cs))
        self.screen.blit(instrucao_superficie, instrucao_rect)
        

    def comecar_fase(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.jogo = "Meio"
        

    def pausar_jogo(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        menu_pausa_rect = pygame.Rect(self.cs * 5, self.cs * 4, self.cs * 15, self.cs * 17)
        pygame.draw.rect(self.screen, (200, 200, 50), menu_pausa_rect)
        
        pausa_1 = "O trem fez uma parada"
        pausa_2 = "Aguarde"
        pausa_superficie = self.fontes[1].render(pausa_1, True, (250, 100, 0))
        pausa_rect = pausa_superficie.get_rect(center = (int(self.cs * (self.cn/2)), 5 * self.cs))
        self.screen.blit(pausa_superficie, pausa_rect)
        pausa_superficie = self.fontes[1].render(pausa_2, True, (250, 100, 0))
        pausa_rect = pausa_superficie.get_rect(center = (int(self.cs * (self.cn/2)), 6 * self.cs))
        self.screen.blit(pausa_superficie, pausa_rect)
    

    def fim_jogo(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        menu_fim_rect = pygame.Rect(self.cs * 5, self.cs * 4, self.cs * 15, self.cs * 17)
        pygame.draw.rect(self.screen, (200, 200, 50), menu_fim_rect)

        self.recorde.ler()
        listas = self.recorde.df.values.tolist()
        for i in range(min(5, len(listas))):
            nome = listas[i][0]
            nome_superficie = self.fontes[1].render(nome, True, "blue")
            nome_rect = nome_superficie.get_rect(center = (int(self.cs * (self.cn / 2 - 3)), (10 + i) * self.cn))
            self.screen.blit(nome_superficie, nome_rect)
            linha = " | " + listas[i][1] + " | " + str(listas[i][2])
            recordes_superficie = self.fontes[1].render(linha, True, (0, 0, 0))
            recordes_rect = recordes_superficie.get_rect(center = (int(self.cs * (3 + self.cn / 2)), (10 + i) * self.cn))
            self.screen.blit(recordes_superficie, recordes_rect)
    

    def registrar_recorde(self):
        self.recorde = Recorde(self.nome)
    

    def cadastrar(self):
        nome_superficie = self.fontes[1].render(self.nome, True, "yellow")
        self.nome_rect = nome_superficie.get_rect(center = (int(self.cs * (self.cn / 2)), 13 * self.cs))
        self.screen.blit(nome_superficie, self.nome_rect)
        if self.selecionado == True:
            pygame.draw.rect(self.screen, (200, 150, 0), self.nome_rect, 2)



class Recorde:
    def __init__(self, nome):
        """ Construtor da classe.
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
            nome: 
        """
        self.arquivo = open("registros.txt", "a+")
        self.nome = nome
    

    def escrever(self, pontuacao):
        """
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        self.arquivo.write(f"{self.nome}|{date.today()}|{pontuacao}\n")
        

    def ler(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        nomes = []
        datas = []
        pontos = []
        self.arquivo.seek(0, 0)
        for linha in self.arquivo.readlines():
            nome, data, ponto = re.split("\|", linha)
            ponto = re.sub("\n", "", ponto)
            nomes.append(nome)
            datas.append(data)
            pontos.append(int(ponto))
        dic = {"Jogador": nomes, "Data": datas, "Pontuação": pontos}
        self.df = pd.DataFrame(dic)
        self.df.sort_values(by = "Data", axis = 0, ascending = False, inplace = True)
        self.df.sort_values(by = "Pontuação", axis = 0, ascending = False, inplace = True)
        self.df.drop_duplicates(subset = "Jogador", inplace = True)
    

    def __del__(self):
        """ 
        
        Args:
            self: palavra-chave que acessa os atributos e métodos da classe Obstaculo.
        """
        #print(f"O recorde cumpriu sua função.")
        #print(f"O recorde foi registrado.")
        pass
