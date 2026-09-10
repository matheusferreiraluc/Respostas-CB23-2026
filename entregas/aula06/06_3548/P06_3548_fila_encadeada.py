from P06_3548_pilha_encadeada import *

class FilaEncadeada:
    """Método de instanciação."""
    def __init__(self):
        self.entrada = PilhaEncadeada()
        self.saida = PilhaEncadeada()

    def enfileirar(self, item):
        """Insere o item no fim da fila. O(1)."""
        self.entrada.push(item)

    def desenfileirar(self):
        """Remove e retorna o item da frente; levanta IndexError se a fila estiver vazia. O(1) amortizada."""
        if self.saida.esta_vazia():
            while not self.entrada.esta_vazia():
                self.saida.push(self.entrada.pop())
        if self.saida.esta_vazia():
            raise IndexError("A fila está vazia.")
        return self.saida.pop()

    def frente(self):
        """Retorna o item da frente sem removê-lo; levanta IndexError se a fila estiver vazia. O(1) amortizada."""
        if self.saida.esta_vazia():
            while not self.entrada.esta_vazia():
                self.saida.push(self.entrada.pop())
        if self.saida.esta_vazia():
            raise IndexError("A fila está vazia.")
        return self.saida.topo()

    def esta_vazia(self):
        """Retorna True quando não há elementos armazenados. O(1)."""
        return self.entrada.esta_vazia() and self.saida.esta_vazia()

    def __len__(self):
        """Retorna a quantidade de elementos da fila. O(1)."""
        tamanho = len(self.entrada) + len(self.saida)
        return tamanho

    def __repr__(self):
        """Representação textual legível, da frente para o fim. O(N)."""
        retorno = ""
        temp_saida = PilhaEncadeada()

        while not self.saida.esta_vazia():
            val = self.saida.pop()
            retorno += f"{val} -> "
            temp_saida.push(val)

        while not temp_saida.esta_vazia():
            self.saida.push(temp_saida.pop())

        temp_entrada = PilhaEncadeada()

        while not self.entrada.esta_vazia():
            temp_entrada.push(self.entrada.pop())
            
        while not temp_entrada.esta_vazia():
            val = temp_entrada.pop()
            retorno += f"{val} -> "
            self.entrada.push(val)
            
        retorno += "Fim"
        return retorno
    