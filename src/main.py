import pygame, sys
from classes import Botao, Partida, SubMenu


# Inicia o módulo PyGame.
pygame.init()


# Quantidade de células no mapa.
cn = 25
# Tamanho das células.
cs = 32

# Define as dimensões da tela do jogo.
screen = pygame.display.set_mode((cn * cs,cn * cs)) 
pygame.display.set_caption("Metrô")


# Imagem de fundo do menu principal.
estacao_com_metro = pygame.image.load("src/imagens/estação_menu.jpg")
# Imagem de fundo do menu Jogar, Opção e Créditos.
estacao_sem_metro = pygame.image.load("src/imagens/estação_sem_metro.jpeg")
retang_fundo = pygame.image.load("src/imagens/retang_fundo.png")

class Menu:
    def __init__(self, screen, estacao_com_metro, estacao_sem_metro, retang_fundo,cn, cs):
        self.screen = screen
        self.imagem_menu_principal = estacao_com_metro
        self.imagem_submenus = estacao_sem_metro
        self.retang_fundo = retang_fundo
        self.cn = cn
        self.cs = cs
        # Cria os objetos da classe SubMenu
        self.fontes = [pygame.font.Font(None, 120), pygame.font.Font(None, 30)]
        self.submenu = SubMenu(cn, cs, screen, self.fontes, "Jogador")

    def fonte(self, tamanho): 
        """ Reponsável por carregar a fonte "caverson".

        :return pygame.font.Font("src/imagens/caverson.otf", tamanho): fonte de letra com tamanho definido.

        Args:
            tamanho (int): tamanho da escrita.
        """ 
        return pygame.font.Font("src/imagens/caverson.otf", tamanho)


    def jogar(self):
        """ É um sub menu para as fases do jogo.
        """
        while True:
            # Cria a superfície da imagem de fundo.
            fundo_rect = pygame.Rect(0, 0, self.cs * self.cn, self.cs * self.cn)         # (Xo, Yo, X, Y)
            # Ajusta as dimensões da imagem de fundo.
            imagem_fundo = pygame.transform.scale(self.imagem_submenus, (self.cs * self.cn, self.cs * self.cn))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_fundo, fundo_rect)

            # Cria a superfície das instruções.
            intrucoes_rect = pygame.Rect(380, 330, 750, 650)     # (Xo, Yo, X, Y)
            # Ajusta as dimensões da imagem de fundo.
            imagem_intrucoes = pygame.transform.scale(pygame.image.load("src/imagens/instrucoes.png"), (370, 320))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_intrucoes, intrucoes_rect)

            # Cria a superfície do quadrado cinza.
            fundo_cinza_rect = pygame.Rect(100, 220, 700, 320)                           # (Xo, Yo, X, Y)
            # Ajusta as dimensões do retangulo_cinza.
            imagem_cinza = pygame.transform.scale(self.retang_fundo, (600, 100))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_cinza, fundo_cinza_rect)

            # Obtem a posição (x,y) do cursor do mouse.
            jogar_mouse_pos = pygame.mouse.get_pos()

            # Título da tela de jogar.
            jogar_titulo = self.fonte(80).render("Fases", True, "#e48b39")
            jogar_rect = jogar_titulo.get_rect(center = (400, 120))
            self.screen.blit(jogar_titulo, jogar_rect)

            # Texto da tela de jogar.
            texto_1 = self.fonte(25).render("Que bom te conhecer, maquinista                        ", True, "#d7fcd4")
            texto_2 = self.fonte(25).render("Escolha uma fase:", True, "#d7fcd4")
            y_coord = 250
            for texto in [texto_1, texto_2]:
                texto_rect = texto.get_rect(center = (400, y_coord))
                self.screen.blit(texto, texto_rect)
                y_coord += 40

            # BOTÕES
            # Cria o botão da fase 1.
            fase_1 = Botao(imagem = pygame.image.load("src/imagens/retang_fundo_fases.png"), pos = (200, 370), texto_cont = "FASE 1: Inglaterra", 
                           fonte = self.fonte(22), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Cria o botão da fase 2.
            fase_2 = Botao(imagem = pygame.image.load("src/imagens/retang_fundo_fases.png"), pos = (200, 430), texto_cont = "FASE 2: Brasil", 
                           fonte = self.fonte(22), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Cria o botão da fase 3.
            fase_3 = Botao(imagem = pygame.image.load("src/imagens/retang_fundo_fases.png"), pos = (200, 490), texto_cont = "FASE 3: Estados Unidos", 
                           fonte = self.fonte(22), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Cria o botão da fase 4.
            fase_4 = Botao(imagem = pygame.image.load("src/imagens/retang_fundo_fases.png"), pos = (200, 550), texto_cont = "FASE 4: China", 
                           fonte = self.fonte(22), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Cria o botão da fase 5.
            fase_5 = Botao(imagem = pygame.image.load("src/imagens/retang_fundo_fases.png"), pos = (200, 610), texto_cont = "FASE 5: França", 
                           fonte = self.fonte(22), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Cria o botão de voltar.
            jogar_voltar = Botao(imagem = None, pos = (400, 700), texto_cont = "Voltar", 
                                 fonte = self.fonte(50), cor_base = "Black", cor_com_mause = "#568e81")

            # Acionar as funções de atualização e mudança de cor para os botões criados.
            for botao in [fase_1, fase_2, fase_3, fase_4, fase_5, jogar_voltar]:
                botao.mudar_cor(jogar_mouse_pos)
                botao.atualizar(self.screen)

            # pygame.event.get() obtém os eventos que ocorrem.
            for evento in pygame.event.get():
                # Finaliza o programa se o botão X (canto superior direito) for clicado.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # É checado se o botão esquerdo do mouse clicou sobre algum botão, nesse caso, ele é redirecionado para a referida página.
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if fase_1.checar_clique(jogar_mouse_pos):
                        # Cria os objetos da classe Partida.
                        self.partida = Partida(cn, cs, screen, pygame.font.Font(None, 30), 1, self.submenu.nome)    # Fase = 1
                        self.submenu.musica.stop()
                        self.partida.inicia_partida()         

                    if fase_2.checar_clique(jogar_mouse_pos):
                        # Cria os objetos da classe Partida.
                        self.partida = Partida(cn, cs, screen, pygame.font.Font(None, 30), 2, self.submenu.nome)    # Fase = 2
                        self.submenu.musica.stop()
                        self.partida.inicia_partida()

                    if fase_3.checar_clique(jogar_mouse_pos):

                        # Cria os objetos da classe Partida.

                        self.partida = Partida(cn, cs, screen, pygame.font.Font(None, 30), 3, self.submenu.nome)    # Fase = 3
                        self.submenu.musica.stop()
                        self.partida.inicia_partida()
                        
                    if fase_4.checar_clique(jogar_mouse_pos):

                        # Cria os objetos da classe Partida.

                        self.partida = Partida(cn, cs, screen, pygame.font.Font(None, 30), 4, self.submenu.nome)    # Fase = 4
                        self.submenu.musica.stop()
                        self.partida.inicia_partida()

                    if fase_5.checar_clique(jogar_mouse_pos):

                       # Cria os objetos da classe Partida.

                        self.partida = Partida(cn, cs, screen, pygame.font.Font(None, 30), 5, self.submenu.nome)    # Fase = 5
                        self.submenu.musica.stop()
                        self.partida.inicia_partida()

                    if jogar_voltar.checar_clique(jogar_mouse_pos):
                        self.menu_principal()

                # Espaço para nome do jogador:
            # Se selecionar o retânculo do nome, começa a escrever o nome do jogador.
                    if self.submenu.cadastro_rect.collidepoint(evento.pos):
                        self.submenu.selecionado = True
                    else:
                        self.submenu.selecionado = False
                
                # Se uma tecla for clicada:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE and self.submenu.selecionado == True:
                        self.submenu.nome = self.submenu.nome[:-1]
                    elif len(self.submenu.nome) < 20 and self.submenu.selecionado == True:
                        self.submenu.nome += evento.unicode
            self.submenu.desenhar_elementos()  

            # Faz com que a superfície de exibição apareça no monitor do usuário.
            pygame.display.update()
        
    def opcoes(self):
        """ É um sub menu para as opções de jogo.
        """
        while True:

            # Cria a superfície da imagem de fundo.
            fundo_rect = pygame.Rect(0, 0, self.cs * self.cn, self.cs * self.cn)
            # Ajusta as dimensões da imagem de fundo.
            imagem_fundo = pygame.transform.scale(self.imagem_submenus, (self.cs * self.cn, self.cs * self.cn))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_fundo, fundo_rect)

            # Obtem a posição (x,y) do cursor do mouse.
            opcoes_menu_pos = pygame.mouse.get_pos()

            # Título da tela de opcoes.
            opcoes_titulo = self.fonte(80).render("Opções", True, "#e48b39")
            opcoes_rect = opcoes_titulo.get_rect(center = (400, 120))
            self.screen.blit(opcoes_titulo, opcoes_rect)


            # Texto da tela de opções.
            opcoes_texto = self.fonte(45).render("This is the OPTIONS screen.", True, "Black")
            # Superfície do texto.
            opcoes_rect = opcoes_texto.get_rect(center=(400, 260))
            # Adicionar à tela de opções.
            self.screen.blit(opcoes_texto, opcoes_rect)

            # Cria o botão de voltar.

            opcoes_voltar = Botao(imagem = None, pos = (400, 700), texto_cont = "Voltar", 
                                 fonte = self.fonte(50), cor_base = "Black", cor_com_mause = "#568e81")


            # Aciona changecolor para alterar a cor quando o mouse está sobre o botão.
            opcoes_voltar.mudar_cor(opcoes_menu_pos)
            # Adiciona o texto e a imagem à tela.
            opcoes_voltar.atualizar(self.screen)

            # pygame.event.get() obtém os eventos que ocorrem.
            for evento in pygame.event.get():
                # Finaliza o programa se o botão X (canto superior direito) for clicado.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Se o botão esquerdo do mouse for clicado sobre o botão "Voltar", é acionado a função "menu_principal" e voltamos ao menu.
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if opcoes_voltar.checar_clique(opcoes_menu_pos):
                        self.menu_principal()

            # Faz com que a superfície de exibição apareça no monitor do usuário.
            pygame.display.update()

    def creditos(self):
        """ É um sub menu para os créditos do jogo.
        """
        while True:

            # Cria a superfície da imagem de fundo.
            fundo_rect = pygame.Rect(0, 0, self.cs * self.cn, self.cs * self.cn)
            # Ajusta as dimensões da imagem de fundo.
            imagem_fundo = pygame.transform.scale(self.imagem_submenus, (self.cs * self.cn, self.cs * self.cn))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_fundo, fundo_rect)

            # Cria a superfície do quadrado cinza.
            fundo_rect2 = pygame.Rect(100, 200, 700, 650)   # (Xo, Yo, X, Y)
            # Ajusta as dimensões do retangulo_cinza.
            imagem_fundo2 = pygame.transform.scale(self.retang_fundo, (600, 450))
            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_fundo2, fundo_rect2)

            # Obtem a posição (x,y) do cursor do mouse.
            opcoes_menu_pos = pygame.mouse.get_pos()

            # Texto da tela de créditos.
            credito_titulo = self.fonte(80).render("Créditos", True, "#e48b39")
            # Superfície do texto.
            credito_rect = credito_titulo.get_rect(center=(400, 120))
            # Adicionar à tela de créditos.
            self.screen.blit(credito_titulo, credito_rect)

            # Título da tela de créditos.
            texto_1 = self.fonte(20).render("Metrô", True, "#e48b39")
            texto_rect = texto_1.get_rect(center = (285, 250))
            self.screen.blit(texto_1, texto_rect)
            # Texto da tela de créditos.
            texto_2 = self.fonte(20).render("             foi desenvolvido por:", True, "#d7fcd4")
            texto_3 = self.fonte(23).render("Rodrigo Kalil,", True, "Black")
            texto_4 = self.fonte(23).render("Rodrigo Dhery Silva Prieto,", True, "Black")
            texto_5 = self.fonte(23).render("Ricael Daniel Vieira da Silva e", True, "Black")
            texto_6 = self.fonte(23).render("Thiago Franke Melchiors,", True, "Black")
            texto_7 = self.fonte(20).render("Alunos do segundo semestre de Ciência de Dados da FGV EMAp.", True, "#d7fcd4")
            texto_8 = self.fonte(20).render("2022", True, "#d7fcd4")

            y_coord = 250
            for texto in [texto_2, texto_3, texto_4, texto_5, texto_6, texto_7, texto_8]:

                texto_rect = texto.get_rect(center = (400, y_coord))
                self.screen.blit(texto, texto_rect)
                y_coord += 60

            # Cria o botão de voltar.

            creditos_voltar = Botao(imagem = None, pos = (400, 700), texto_cont = "Voltar", 
                                 fonte = self.fonte(50), cor_base = "Black", cor_com_mause = "#568e81")
                                 
            # Aciona changecolor para alterar a cor quando o mouse está sobre o botão.
            creditos_voltar.mudar_cor(opcoes_menu_pos)
            # Adiciona o texto e a imagem à tela.
            creditos_voltar.atualizar(self.screen)


            # pygame.event.get() obtém os eventos que ocorrem.
            for evento in pygame.event.get():
                # Finaliza o programa se o botão X (canto superior direito) for clicado.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Se o botão esquerdo do mouse for clicado sobre o botão "Voltar", é acionado a função "menu_principal" e voltamos ao menu.
                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if creditos_voltar.checar_clique(opcoes_menu_pos):
                        self.menu_principal()

            # Faz com que a superfície de exibição apareça no monitor do usuário.
            pygame.display.update()


    def menu_principal(self):
        """ Responsável por gerar o menu principal do jogo, acionando as funções "jogar" e "opcoes" e a classe Botao para criar os botões. 
        """
        # O loop ocorre enquanto não for clicado no botão "SAIR".
        while True:
            # Cria a superfície da imagem de fundo.
            fundo_rect = pygame.Rect(0, 0, self.cs * self.cn, self.cs * self.cn)
            # Ajusta as dimensões da imagem de fundo.
            imagem_fundo = pygame.transform.scale(self.imagem_menu_principal, (self.cs * self.cn, self.cs * self.cn))

            # SCREEN.blit(nome_imagem, (x_pos, y_pos))
            self.screen.blit(imagem_fundo, fundo_rect)
            
            # Obtem a posição do cursor do mouse.
            menu_mouse_pos = pygame.mouse.get_pos()

            # Título principal do menu.
            menu_text = self.fonte(100).render("Metrô", True, "#e48b39")
            # Cria um objeto rect para colocar o texto.
            menu_rect = menu_text.get_rect(center = (400, 120))

            # Adicionar na tela o título.
            self.screen.blit(menu_text, menu_rect)

            # Criar os botões do menu acionando a classe Botao:
            # Botão de jogar.
            botao_jogar = Botao(imagem = pygame.image.load("src/imagens/retang_fundo.png"), pos = (400, 300), 
                                texto_cont = "JOGAR", fonte = self.fonte(75), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Botão de opções.
            botao_opcoes = Botao(imagem = pygame.image.load("src/imagens/retang_fundo.png"), pos=(400, 430), 
                                texto_cont = "OPÇÕES", fonte = self.fonte(75), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Botão de créditos.
            botao_creditos = Botao(imagem = pygame.image.load("src/imagens/retang_fundo.png"), pos=(400, 560), 
                                texto_cont = "CRÉDITOS", fonte = self.fonte(75), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")
            # Botão de sair.
            botao_sair = Botao(imagem = pygame.image.load("src/imagens/retang_fundo.png"), pos = (400, 690), 
                                texto_cont = "SAIR", fonte = self.fonte(75), cor_base = "#d7fcd4", cor_com_mause = "#5b9388")

            # Acionar as funções de atualização e mudança de cor para os botões criados.
            for botao in [botao_jogar, botao_opcoes, botao_creditos, botao_sair]:
                botao.mudar_cor(menu_mouse_pos)
                botao.atualizar(self.screen)
            
            # pygame.event.get() obtem os eventos que ocorrem.
            for evento in pygame.event.get():
                # Finaliza o programa se o botão X (canto superior direito) for clicado.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Se o botão esquerdo do mouse for clicado sobre o botão
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    # Jogar, é acionado a função "jogar".
                    if botao_jogar.checar_clique(menu_mouse_pos):
                        self.jogar()
                    # Opções, é acionado a função "opções".
                    if botao_opcoes.checar_clique(menu_mouse_pos):
                        self.opcoes()
                    if botao_creditos.checar_clique(menu_mouse_pos):
                        self.creditos()
                    # Sair, o programa é finalizado.
                    if botao_sair.checar_clique(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
            
            # Faz com que a superfície de exibição apareça no monitor do usuário.
            pygame.display.update()


menu = Menu(screen, estacao_com_metro, estacao_sem_metro, retang_fundo, cn, cs)
menu.menu_principal()
