# 🛵 Rota Inteligente: Otimização de Entregas - Sabor Express

## 1. Descrição do Problema

A "Sabor Express" enfrenta ineficiência logística em horários de pico. As rotas manuais geram atrasos e alto custo de combustível. O objetivo deste projeto é desenvolver uma solução baseada em IA para:

1.  Agrupar entregas próximas (Clustering).
2.  Calcular a rota mais rápida entre os pontos (Pathfinding).

## 2. Abordagem Adotada

Consideramos a cidade como um grafo $G(V, E)$, onde $V$ são locais e $E$ são as ruas. A solução é híbrida:

- **Etapa 1 (Estratégica):** Uso de **Aprendizado de Máquina (K-Means)** para dividir os pedidos entre os entregadores disponíveis, garantindo que cada um atue em uma zona geográfica específica.
- **Etapa 2 (Tática):** Uso de **Algoritmo de Busca (A\*)** para encontrar o menor caminho físico (ruas) entre a sequência de entregas.

## 3. Algoritmos Utilizados

- **K-Means (Clustering):** Algoritmo não supervisionado que agrupa coordenadas geográficas das entregas em $K$ clusters (onde $K$ é o número de entregadores). Minimiza a variância dentro de cada cluster.
- **A\* (A-Star Search):** Algoritmo de busca informada. Utiliza a função de custo $f(n) = g(n) + h(n)$, onde $g(n)$ é o custo real do início até o nó $n$, e $h(n)$ é a heurística (Distância Euclidiana) estimada até o destino. É mais eficiente que o Dijkstra por ser "guiado" ao alvo.

## 4. Estrutura do Projeto

- `/src`: Contém o código fonte `main.py`.
- **Grafo:** Gerado sinteticamente usando `NetworkX` para simular uma malha urbana com 60 nós e conectividade baseada em proximidade.

## 5. Resultados e Análise

A aplicação combinada de K-Means e A\* resultou em:

- **Balanceamento de Carga:** As entregas foram distribuídas equitativamente entre os motoristas.
- **Redução de Percurso:** O agrupamento prévio impede que dois motoristas cruzem a cidade para locais vizinhos.
- **Visualização:** O gráfico gerado (ver output) demonstra rotas claras e sem sobreposições desnecessárias.

**Limitações:** O modelo atual assume trânsito estático (pesos fixos).
**Melhoria Futura:** Integrar API de trânsito em tempo real (como Google Maps API) para pesos dinâmicos nas arestas.

## Como Executar

1. Instale as dependências: `pip install networkx matplotlib scikit-learn numpy`
2. Execute: `python main.py`
