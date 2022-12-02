import sys
import pygame
from pygame.math import Vector2
sys.path.insert(0, '.')
from classes import Partida, Menu
import operator

class Jogo:
    def __init__(self):
        
        pygame.init()

        self.cn = 25 # Quantidade de células no mapa
        self.cs = 32 # Tamanho das células

        self.screen = pygame.display.set_mode((self.cn * self.cs,self.cn * self.cs)) # Tamanho da tela do jogo
        pygame.display.set_caption("Metrô") # Adiciona um nome à janela
        self.clock = pygame.time.Clock()
        self.fontes = [pygame.font.Font(None, 120), pygame.font.Font(None, 30)]
        self.menu = Menu(self.cn, self.cs, self.screen, self.fontes)
        self.partida = Partida(self.cn, self.cs, self.screen, self.fontes[1])
        self.SCREEN_UPDATE = pygame.USEREVENT 
        pygame.time.set_timer(self.SCREEN_UPDATE, 150)
        # Criamos um evento que ocorre a cada 150 milissegundos e que vai acionar o movimento do trem

    def loop(self):
            while True:
                if self.menu.jogo == "Menu":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            # Identifica quando o usuário clica no x na janela, fechando o programa
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.menu.nome_rect.collidepoint(event.pos):
                                self.menu.selecionado = True
                            else:
                                self.menu.selecionado = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                                self.menu.comecar_fase()
                                self.partida.ativo = True
                                self.menu.musica.stop()
                                self.partida.musica.stop()
                                self.partida.musica.play()
                            elif event.key == pygame.K_BACKSPACE and self.menu.selecionado == True:
                                self.menu.nome = self.menu.nome[:-1]
                            elif len(self.menu.nome) < 20 and self.menu.selecionado == True:
                                self.menu.nome += event.unicode

                    self.menu.desenhar_elementos()
                    pygame.display.flip() # Renderiza
                    self.clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo

                elif self.menu.jogo == "Meio":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            # Identifica quando o usuário clica no x na janela, fechando o programa
                        if event.type == self.SCREEN_UPDATE:
                            pygame.time.set_timer(self.SCREEN_UPDATE, 150)
                            if self.partida.ativo == True:
                                self.partida.atualizar()
                            # Identifica quando o evento periódico que foi criado fora do loop ocorre, chamando então a função mover_trem()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE and self.partida.ativo == True:
                                self.partida.pausa = operator.not_(self.partida.pausa)
                                self.menu.pausa = self.partida.pausa
                            if event.key == pygame.K_UP and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(0,-1) or event.key == pygame.K_w and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(0,-1):
                                self.partida.trem.sentido = Vector2(0,-1)
                            if event.key == pygame.K_DOWN and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(0,1) or event.key == pygame.K_s and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(0,1):
                                self.partida.trem.sentido = Vector2(0,1)
                            if event.key == pygame.K_RIGHT and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(1,0) or event.key == pygame.K_d and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(1,0):
                                self.partida.trem.sentido = Vector2(1,0)
                            if event.key == pygame.K_LEFT and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(-1,0) or event.key == pygame.K_a and self.partida.trem.corpo[1] != self.partida.trem.corpo[0]+Vector2(-1,0):
                                self.partida.trem.sentido = Vector2(-1,0)
                            # Identifica quando o usuário pressiona uma das setas do teclado e ajusta a direção do movimento do trem de acordo
                            if self.partida.ativo == False:
                                self.menu.jogo = "Fim"
                                self.menu.registrar_recorde()
                                self.menu.recorde.escrever(self.partida.pontuacao)
                                self.partida.__del__()

                    self.partida.desenhar_elementos()
                    self.menu.desenhar_elementos()
                    pygame.display.flip() # Renderiza
                    self.clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo

                elif self.menu.jogo == "Fim":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.menu.recorde.arquivo.close()
                            pygame.quit()
                            sys.exit()
                            # Identifica quando o usuário clica no x na janela, fechando o programa
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pass

                    self.screen.fill((100,100,200)) # Preenche a tela com cor
                    self.partida.desenhar_elementos()
                    self.menu.desenhar_elementos()
                    pygame.display.flip() # Renderiza
                    self.clock.tick(60) # Garante uma frequência de cerca de 60 frames por segundo
            
            
if __name__ == "__main__":
    jogo = Jogo()
    jogo.loop()
