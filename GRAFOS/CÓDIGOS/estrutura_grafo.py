import csv


def carregar_grafo(arquivo_nos, arquivo_arestas):
    grafo = {}

    # Primeiro cria um vértice para cada cidade do arquivo de nós
    with open(arquivo_nos, "r", encoding="utf-8") as arq:
        leitor_nos = csv.DictReader(arq)
        for linha in leitor_nos:
            cidade = linha["Id"]
            grafo[cidade] = []

    # Em seguida, adiciona as arestas (grafo não-direcionado e ponderado)
    with open(arquivo_arestas, "r", encoding="utf-8") as arq:
        leitor_arestas = csv.DictReader(arq)
        for linha in leitor_arestas:
            origem = linha["Source"]
            destino = linha["Target"]
            peso = float(linha["Distance_km"])

            grafo[origem].append((destino, peso))
            grafo[destino].append((origem, peso))

    return grafo


def estatisticas_grafo(grafo):
    """Exibe o número de vértices, número de arestas e o grau médio do grafo."""
    num_vertices = len(grafo)
    soma_graus = sum(len(grafo[cidade]) for cidade in grafo)
    num_arestas = soma_graus // 2  # cada aresta foi contada duas vezes

    print("\n===== ESTATÍSTICAS =====")
    print("Número de vértices:", num_vertices)
    print("Número de arestas:", num_arestas)
    print("Grau médio: {:.2f}".format(soma_graus / num_vertices))
