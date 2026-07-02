from collections import deque
import heapq

# Busca em Largura (BFS)
def bfs(grafo, inicio):
    fila = deque([inicio])
    visitados = [inicio]
    pai = {inicio: None}

    while fila:
        atual = fila.popleft()
        for vizinho, _peso in grafo[atual]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                pai[vizinho] = atual
                fila.append(vizinho)

    return pai


def reconstruir_caminho(pai, origem, destino):
    if destino not in pai:
        return []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]

    return list(reversed(caminho))


# Busca em Profundidade (DFS)
def dfs(grafo, inicio=None):
    visitados = set()
    desc = {}
    fim = {}
    pais = {}
    retorno = []
    tempo = 0

    def visitar(u, p=None):
        nonlocal tempo
        visitados.add(u)
        pais[u] = p
        tempo += 1
        desc[u] = tempo

        for v, _peso in grafo[u]:
            if v not in visitados:
                visitar(v, u)
            else:
                # Se 'v' já foi visitado, ainda não finalizado, e não é o pai
                # direto, então (u, v) é uma aresta de retorno -> há ciclo
                if v != p and v not in fim and desc[v] < desc[u]:
                    retorno.append((u, v))

        tempo += 1
        fim[u] = tempo

    if inicio is not None and inicio in grafo:
        visitar(inicio)

    for vertice in grafo:
        if vertice not in visitados:
            visitar(vertice)

    return desc, fim, pais, retorno


# Dijkstra (menor caminho com pesos)
def dijkstra(grafo, inicio):
  
    dist = {v: float("inf") for v in grafo}
    pai = {v: None for v in grafo}
    dist[inicio] = 0

    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        d_atual, u = heapq.heappop(fila_prioridade)

        if d_atual != dist[u]:
            continue  # entrada desatualizada na heap, ignora

        for v, peso in grafo[u]:
            nova_dist = d_atual + peso
            if nova_dist < dist[v]:
                dist[v] = nova_dist
                pai[v] = u
                heapq.heappush(fila_prioridade, (nova_dist, v))

    return pai, dist
    
# Componentes conexas

def contar_componentes(grafo):
    """
    Identifica as componentes conexas do grafo usando busca em largura.
    Retorna a lista de componentes (cada componente é uma lista de cidades).
    A quantidade de componentes é simplesmente len(retorno).
    """
    visitados = []
    componentes = []

    for vertice in grafo:
        if vertice not in visitados:
            componente = []
            fila = deque([vertice])
            visitados.append(vertice)

            while fila:
                u = fila.popleft()
                componente.append(u)
                for v, _peso in grafo[u]:
                    if v not in visitados:
                        visitados.append(v)
                        fila.append(v)

            componentes.append(componente)

    return componentes
    
# Funções de apoio para o relatório
def maior_grau(grafo):
    """Retorna a cidade com maior grau e o respectivo valor do grau."""
    cidade = max(grafo, key=lambda x: len(grafo[x]))
    return cidade, len(grafo[cidade])


def possui_ciclo(grafo):
    """Retorna True se o grafo possuir ao menos uma aresta de retorno (ciclo)."""
    _desc, _fim, _pais, arestas_retorno = dfs(grafo)
    return len(arestas_retorno) > 0
