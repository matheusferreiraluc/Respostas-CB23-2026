import unittest
from P06_3548_pilha_encadeada import *
from P06_3548_fila_encadeada import *

class TestPilhaEncadeada(unittest.TestCase):
    def test_ordem_lifo(self):
        # --- Ordem LIFO em sequência de push/pop na pilha ---
        pilha = PilhaEncadeada()
        pilha.push(1)
        pilha.push(2)
        pilha.push(3)
        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 2)
        self.assertEqual(pilha.pop(), 1)

    def test_excecao_pilha_vazia(self):
        # --- pop e topo em pilha vazia ---
        pilha = PilhaEncadeada()
        with self.assertRaises(IndexError):
            pilha.pop()
        with self.assertRaises(IndexError):
            pilha.topo()

    def test_coerencia_len(self):
        # --- Coerência de len após inserções e remoções na pilha ---
        pilha = PilhaEncadeada()
        self.assertEqual(len(pilha), 0)
        pilha.push(10)
        self.assertEqual(len(pilha), 1)
        pilha.push(20)
        self.assertEqual(len(pilha), 2)
        pilha.pop()
        self.assertEqual(len(pilha), 1)

    def test_alternancia_operacoes(self):
        # --- Alternância de operações na pilha ---
        pilha = PilhaEncadeada()
        pilha.push(5)
        self.assertEqual(pilha.pop(), 5)
        pilha.push(10)
        pilha.push(15)
        self.assertEqual(pilha.topo(), 15)
        self.assertEqual(pilha.pop(), 15)

    def test_tipos_diferentes_e_none(self):
        # --- Armazenamento de itens de tipos diferentes, valores repetidos e None na pilha ---
        pilha = PilhaEncadeada()
        pilha.push("texto")
        pilha.push(None)
        pilha.push([1, 2])
        pilha.push("texto")
        
        self.assertEqual(pilha.pop(), "texto")
        self.assertEqual(pilha.pop(), [1, 2])
        self.assertIsNone(pilha.pop())
        self.assertEqual(pilha.pop(), "texto")


class TestFilaEncadeada(unittest.TestCase):
    def test_ordem_fifo(self):
        # --- Ordem FIFO na fila ---
        fila = FilaEncadeada()
        fila.enfileirar("A")
        fila.enfileirar("B")
        fila.enfileirar("C")
        self.assertEqual(fila.desenfileirar(), "A")
        self.assertEqual(fila.desenfileirar(), "B")
        self.assertEqual(fila.desenfileirar(), "C")

    def test_intercalacao(self):
        # --- Intercalação de enfileirar e desenfileirar na fila ---
        fila = FilaEncadeada()
        fila.enfileirar(1)
        fila.enfileirar(2)
        self.assertEqual(fila.desenfileirar(), 1)
        fila.enfileirar(3)
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)

    def test_esvaziar_e_voltar_usar(self):
        # --- Esvaziar e voltar a usar a mesma instância na fila ---
        fila = FilaEncadeada()
        fila.enfileirar(10)
        fila.desenfileirar()
        self.assertTrue(fila.esta_vazia())
        fila.enfileirar(20)
        self.assertEqual(fila.frente(), 20)
        self.assertEqual(len(fila), 1)

    def test_excecao_fila_vazia(self):
        # --- Desenfileirar e frente em fila vazia ---
        fila = FilaEncadeada()
        with self.assertRaises(IndexError):
            fila.desenfileirar()
        with self.assertRaises(IndexError):
            fila.frente()

    def test_coerencia_len(self):
        # --- Coerência de len na fila ---
        fila = FilaEncadeada()
        self.assertEqual(len(fila), 0)
        fila.enfileirar("X")
        self.assertEqual(len(fila), 1)
        fila.enfileirar("Y")
        self.assertEqual(len(fila), 2)
        fila.desenfileirar()
        self.assertEqual(len(fila), 1)

if __name__ == "__main__":
    unittest.main()


