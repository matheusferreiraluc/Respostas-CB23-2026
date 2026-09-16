# Atividade Prática 7 - Buscas em Grafos e Labirintos

**Questão 2**

Para resolver o problema, foi necessário implementar um algoritmo capaz de encontrar o caminho partindo da posição (1,1) até a localização do queijo. A solução escolhida para realizar essa navegação foi a **Busca em Largura (BFS - Breadth-First Search)**. 

A justificativa para essa escolha baseia-se nas seguintes características do problema:

* O script base utilizado na primeira etapa produz o que é chamado de labirinto "perfeito" (que possui exatamente um caminho ligando quaisquer dois pontos). Estruturalmente, esse labirinto atua como o equivalente a uma árvore geradora aleatória m x n.
* Visto que existe apenas um trajeto correto do início até o queijo, tanto a DFS quanto a BFS seriam capazes de encontrar a rota exata. Porém, a opção pela BFS foi feita porque, em problemas de travessia, ela processa a exploração em níveis. Dessa forma, caso as regras de geração mudassem no futuro e o labirinto passasse a ter múltiplos caminhos, a BFS continuaria assegurando que a rota encontrada seria o caminho mais curto possível, além de evitar estourar o limite de recursão (um risco associado a implementações recursivas clássicas de DFS em labirintos de grandes proporções).