
#  Rota Inteligente: Otimização de Entregas - Sabor Express

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-GPLv3-lightgrey)

## 1. Descrição do Problema

A "Sabor Express" enfrenta ineficiência logística em horários de pico. As rotas manuais geram atrasos e alto custo de combustível. O objetivo deste projeto é desenvolver uma solução baseada em IA para:

1.  **Agrupar entregas próximas (Clustering):** Dividir geograficamente as áreas entre os entregadores.
2.  **Calcular a rota mais rápida (Pathfinding):** Encontrar o menor caminho entre os pontos em sequência.

## 2. Abordagem e Algoritmos Adotados

Consideramos a cidade como um grafo $G(V, E)$, onde $V$ são locais e $E$ são as ruas. A solução é híbrida:

- **Etapa 1 (Estratégica):** Uso de **Aprendizado de Máquina (K-Means)** para dividir os pedidos entre os entregadores disponíveis, garantindo que cada um atue em uma zona geográfica específica, minimizando a variância.
- **Etapa 2 (Tática):** Uso de **Algoritmo de Busca (A\*)** para encontrar o menor caminho físico (ruas) entre a sequência de entregas. Utiliza a heurística de Distância Euclidiana, sendo mais eficiente que o Dijkstra por ser "guiado" ao alvo.

---

## 3. Atendimento aos Requisitos do Projeto

###  3.1. Organização e Estrutura do Código (`/src`, `/data`, `/docs`)
O projeto adota a seguinte estrutura de pastas recomendada para ambientes de produção:
* `/src`: Contém o script `main.py` com a lógica central.
* `/capturas`: Contém os artefatos visuais do algoritmo.
```

###  3.3. Outputs Relevantes
A aplicação da Inteligência Artificial resultou na redução de percurso e em um balanceamento de carga (entregas justas para cada motorista baseadas em sua zona geográfica).

**Output de Console (Logs de Execução):**
```text
Iniciando Sistema Sabor Express AI...
 Locais de Entrega: [43 38 52 49 33 13 42 16 35 15 54  2]

 Agrupamento (Clusters):
  Motorista 1: 3 entregas -> Nós [...]
  Motorista 2: 6 entregas -> Nós [...]
  Motorista 3: 3 entregas -> Nós [...]

Otimização Concluída. Mapa gerado.
```

**Output Gráfico (Rotas):** *(Imagem de exemplo gerada pela execução contida na pasta `/docs`)*

###  3.4. Instruções Claras para Execução

Para testar e rodar a simulação na sua máquina, siga o passo a passo:

**1. Dependências Necessárias:** Certifique-se de ter o Python 3.8+ instalado e instale as bibliotecas abaixo via terminal:

```bash
pip install networkx matplotlib scikit-learn numpy scipy

```

**2. Executando o Projeto:** No seu terminal, clone o projeto (ou extraia os arquivos) e execute o script:

```bash
# Navegue até a pasta do projeto
cd src

# Execute o arquivo principal
python main.py

```

**3. Visualização:** O script irá imprimir o agrupamento no terminal e, logo em seguida, abrirá uma janela do `matplotlib` renderizando o grafo visualmente com as rotas dos 3 entregadores marcadas por cores diferentes.

---

```

