# Por que desenfileirar pode custar O(N) no pior caso?

O método `desenfileirar` custa O(N) quando a pilha de saída está vazia. Neste caso, todos os N elementos armazenados na pilha de entrada precisam ser desempilhados (com custo O(1) cada) e empilhados na pilha de saída (também com custo O(1) cada). Como essa operação é repetida N vezes, o custo total dessa única chamada de desenfileirar se torna O(N).

## Por que a complexidade é O(1) amortizada?

A complexidade é considerada O(1) amortizada pois avaliamos o custo médio das operações ao longo do tempo. Considere o ciclo de vida de um elemento na `FilaEncadeada`:

1. Ele é empilhado na pilha de entrada no momento em que é enfileirado (custo O(1)).
2. Ele é desempilhado da pilha de entrada durante a transferência (custo O(1)).
3. Ele é empilhado na pilha de saída durante a transferência (custo O(1)).
4. Ele é desempilhado da pilha de saída quando for desenfileirado (custo O(1)).

Como cada elemento é movimentado um número constante e restrito de vezes (no máximo 4 operações elementares) durante todo o seu tempo de existência na estrutura, o custo total para enfileirar e desenfileirar N elementos é proporcional a N. Dividindo esse custo total de O(N) pelo número N de operações, o custo médio para cada chamada individual é diluído para O(1).