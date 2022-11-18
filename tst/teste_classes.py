import sys
sys.path.insert(0, "..\src")
import unittest as u
import classes as c
from pygame.math import Vector2

def setUpModule():
    print("Iniciando rodada de testes")

def tearDownModule():
    print("Finalizando rodada de testes")
    
class TesteClasses(u.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Realizando testes do módulo classes")
    @classmethod
    def tearDownClass(cls):
        print("Terminando testes do módulo classes")
        
    def setUp(self):
        print("Executando SetUpMethod")
    
    def tearDown(self):
        print("Executando TearDownMethod")
    
    def test_case_mover_trem(self):
        print("Executando Caso de Teste: Mover trem")
        trem = c.Trem()
        trem.mover_trem()
        self.assertEqual(trem.corpo, [Vector2(6,2), Vector2(5,2), Vector2(4,2)])



if __name__ == "__main__":
    u.main(verbosity=2)