import os

from estrutura_grafo import carregar_grafo, estatisticas_grafo

# Nomes dos arquivos do dataset D8
ARQUIVO_NOS = "D8_cidades_pe_nodes.csv"
ARQUIVO_ARESTAS = "D8_cidades_pe.csv"

# Cidades usadas como exemplo nas buscas (ajuste conforme o relatório)
CIDADE_ORIGEM = "Recife"
CIDADE_DESTINO = "Caruaru"

def main():
    
    # 1. Carregamento do grafo
    
    grafo = carregar_grafo(ARQUIVO_NOS, ARQUIVO_ARESTAS)

    print("===== LISTA DE ADJACÊNCIA =====")
    for cidade in grafo:
        print(cidade, "->", grafo[cidade])

    estatisticas_grafo(grafo)

    # 2. BFS

    print("\n===== BFS =====")
    pai_bfs = bfs(grafo, CIDADE_ORIGEM)
    for cidade in pai_bfs:
        print(cidade, "<-", pai_bfs[cidade])

    # 3. DFS (Pergunta 6: árvore DFS e tempos)
    print("\n===== DFS =====")
    descoberta, finalizacao, pai_dfs, arestas_retorno = dfs(grafo, CIDADE_ORIGEM)
    print("Tempos de descoberta:", descoberta)
    print("Tempos de finalização:", finalizacao)
    print("Árvore DFS (pai):", pai_dfs)
    print("Arestas de retorno:", arestas_retorno)
        
# 4. Dijkstra (Pergunta 1: menor caminho)
    print("\n===== DIJKSTRA (menor caminho) =====")
    pai_dijkstra, distancias = dijkstra(grafo, CIDADE_ORIGEM)
    caminho_minimo = reconstruir_caminho(pai_dijkstra, CIDADE_ORIGEM, CIDADE_DESTINO)
    print("Caminho:", caminho_minimo)
    print("Distância total:", distancias[CIDADE_DESTINO], "km")

# 5. Componentes conexas (Pergunta 4)
    print("\n===== COMPONENTES CONEXAS =====")
    componentes = contar_componentes(grafo)
    print("Quantidade de componentes:", len(componentes))
    for indice, componente in enumerate(componentes, 1):
        print(indice, componente)

adição no buscas_grafos.py de 

 # 6. Maior grau (Pergunta 2) e ciclos (Pergunta 3)
    cidade_maior_grau, grau = maior_grau(grafo)
    print("\nCidade com maior grau:", cidade_maior_grau, "-> grau", grau)

    print("Possui ciclos:", "Sim" if possui_ciclo(grafo) else "Não")

if __name__ == "__main__":
    main()
