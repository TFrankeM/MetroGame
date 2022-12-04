import sys
sys.path.insert(0, ".\src")
import unittest as u
import main as m
from pygame.math import Vector2

def setUpModule():
    print("Iniciando rodada de testes")

def tearDownModule():
    print("Finalizando rodada de testes")
    
class TesteClasses(u.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Realizando testes do módulo main")
    @classmethod
    def tearDownClass(cls):
        print("Terminando testes do módulo main")
        
    def setUp(self):
        print("Executando SetUpMethod")
    
    def tearDown(self):
        print("Executando TearDownMethod")
    
    def test_case_menu_atualizar_idiomas_alemao(self):
        print("Executando Caso de Teste: Mudar nomes dos idiomas para o alemão")
        menu = m.Menu()
        menu.submenu.idioma = "en"
        menu.atualizar_idiomas()
        self.assertEqual(menu.idiomas, ["Portuguese", "English", "French", "Latin", "German", "Esperanto", "Javanes", "Spanish"])
    
    



if __name__ == "__main__":
    u.main(verbosity=2)
