from collections import deque
import heapq


# =====================================================
# Busca em Largura (BFS)
# =====================================================
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


# =====================================================
# Busca em Profundidade (DFS)
# =====================================================
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
