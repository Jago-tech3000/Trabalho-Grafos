import os

from estrutura_grafo import carregar_grafo, estatisticas_grafo

# Nomes dos arquivos do dataset D8
ARQUIVO_NOS = "D8_cidades_pe_nodes.csv"
ARQUIVO_ARESTAS = "D8_cidades_pe.csv"

# Cidades usadas como exemplo nas buscas (ajuste conforme o relatório)
CIDADE_ORIGEM = "Recife"
CIDADE_DESTINO = "Caruaru"

def main():
    # ---------------------------------------------------
    # 1. Carregamento do grafo
    # ---------------------------------------------------
    grafo = carregar_grafo(ARQUIVO_NOS, ARQUIVO_ARESTAS)

    print("===== LISTA DE ADJACÊNCIA =====")
    for cidade in grafo:
        print(cidade, "->", grafo[cidade])

    estatisticas_grafo(grafo)

        
if __name__ == "__main__":
    main()