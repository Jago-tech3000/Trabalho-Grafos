# Projeto de Exploração de Grafos: Rede Rodoviária de Pernambuco (D8)

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Estruturas de Dados II** (UFPE - NICEN/CAA). O objetivo é aplicar algoritmos clássicos de teoria dos grafos em uma rede real: o dataset **D8**, que representa municípios de Pernambuco conectados por rodovias.

##Descrição da Rede
A rede analisada é um grafo **não dirigido e pesado**, onde:
*   **Vértices:** Representam 26 cidades de Pernambuco.
*   **Arestas:** Representam conexões rodoviárias entre as cidades.
*   **Pesos:** Distâncias aproximadas em quilômetros (km) entre os municípios.
*   **Hub Principal:** Recife, com grau 10.

##Estrutura do Projeto
O código foi organizado de forma modular para facilitar a compreensão:

```text
Trabalho-Grafos/
├── DADOS/
│   ├── D8_cidades_pe.csv        # Arquivo de arestas e pesos
│   └── D8_cidades_pe_nodes.csv  # Legenda dos nós (cidades)
└── CÓDIGOS/
    ├── trabalho_grafos.py                  # Ponto de entrada e análises principais
    ├── estrutura_grafo.py       # Funções de carregamento e estatísticas
    ├── buscas_grafo.py          # Implementação manual dos algoritmos
    ├── D8_cidades_pe.csv        # Arquivo de arestas e pesos
    └── D8_cidades_pe_nodes.csv  # Legenda dos nós (cidades)
```

### Detalhes dos Arquivos
*   **`estrutura_grafo.py`**: Contém a lógica para construir a **lista de adjacência** a partir dos arquivos CSV e funções para exibir estatísticas básicas (vértices, arestas e grau médio).
*   **`buscas_grafo.py`**: Centraliza os algoritmos obrigatórios, implementados manualmente sem o uso de bibliotecas externas (como NetworkX):
    *   **BFS (Busca em Largura):** Com reconstrução de caminho.
    *   **DFS (Busca em Profundidade):** Com registro de tempos de descoberta/finalização e identificação de arestas de retorno.
    *   **Dijkstra:** Para cálculo de menor caminho considerando pesos em km.
    *   **Detecção de Componentes:** Identifica a conectividade do grafo.
    *   **Análises Adicionais:** Identificação de nó de maior grau e verificação de ciclos.
*   **`trabalho_grafos.py`**: Integra as funcionalidades para responder às perguntas obrigatórias do relatório.

## Como Executar
1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório para sua máquina local.
3. Navegue até a pasta `CÓDIGOS/`.
4. Execute o script principal:
   ```bash
   python trabalho_grafos.py
   ```

## Algoritmos Implementados
De acordo com os requisitos do projeto, todos os algoritmos foram escritos do zero utilizando apenas bibliotecas padrão do Python (`csv`, `collections.deque`, `heapq`).

| Algoritmo | Complexidade (Tempo) | Aplicação no Projeto |
| :--- | :--- | :--- |
| **BFS** | $O(\|V\| + \|A\|)$ | Caminhos mínimos em número de saltos. |
| **DFS** | $O(\|V\| + \|A\|)$ | Identificação de ciclos e tempos de visitação. |
| **Dijkstra** | $O(\|A\| \log \|V\|)$ | Menor rota rodoviária em km (Petrolina ↔ Recife). |
| **Estatísticas**| $O(\|V\| + \|A\|)$ | Cálculo de grau médio e maior grau. |

## Relatório e Defesa
As respostas detalhadas para as 6 perguntas obrigatórias (componentes conexas, menor caminho, maior grau, árvore DFS, presença de ciclos e pergunta adicional) estão documentadas no relatório em PDF presente na raiz do projeto.

---
**Autores:** IAGO FERREIRA SILVA & PEDRO LUCAS ALVES SILVA
**Instituição:** UFPE — NICEN / CAA
