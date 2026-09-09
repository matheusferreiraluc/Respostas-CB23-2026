class _No:
    def __init__(self, valor):
        """Método de instanciação."""
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    """
    Implementa uma pilha LIFO (Last In, First Out) cujo armazenamento interno é uma lista simplesmente encadeada.
    Tem uma referência ao nó do topo e um contador de elementos.
    Os nós são representados pela classe auxiliar _No, com os atributos 'valor' e 'próximo'.
    """

    def __init__(self):
        """Método de instanciação."""
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """Insere o item no topo da pilha. O(1)."""
        no = _No(item)
        no.proximo = self._topo
        self._topo = no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o item do topo; levanta IndexError se a pilha estiver vazia. O(1)."""
        if self.esta_vazia():
            raise IndexError(f"A pilha está vazia.")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor

    def topo(self):
        """Retorna o item do topo sem removê-lo; levanta IndexError se a pilha estiver vazia. O(1)."""
        if self._topo is None:
            raise IndexError("A pilha está vazia.")
        return self._topo.valor

    def esta_vazia(self):
        """Retorna True quando não há elementos armazenados. O(1)."""
        if self._topo is None:
            return True
        return False
            
    def __len__(self):
        """Retorna a quantidade de elementos; exige contador mantido incrementalmente. O(1)."""
        return self._tamanho

    def __repr__(self):
        """Representação textual legível, do topo para a base. O(N)."""
        retorno = ""
        atual = self._topo
        while atual is not None:
            retorno += f"{atual.valor} -> "
            atual = atual.proximo
        retorno += "Base"
        return retorno