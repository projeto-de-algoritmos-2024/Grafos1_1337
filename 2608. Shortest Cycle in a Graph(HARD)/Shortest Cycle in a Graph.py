from collections import deque
from typing import List, Tuple


class Solution:
    def findShortestCycle(self, n: int, arestas: List[List[int]]) -> int:
        def bfs(inicio: int, grafo: List[List[int]]) -> int:
            distancias = [-1] * n
            pais = [-1] * n
            distancias[inicio] = 0

            fila = deque([inicio])

            ciclo_min_local = float('inf')

            while fila:
                atual = fila.popleft()

                for vizinho in grafo[atual]:
                    if distancias[vizinho] == -1:
                        # Nó não visitado
                        distancias[vizinho] = distancias[atual] + 1
                        pais[vizinho] = atual
                        fila.append(vizinho)
                    elif pais[atual] != vizinho:
                        # Ciclo encontrado
                        comprimento_ciclo = distancias[atual] + distancias[vizinho] + 1
                        ciclo_min_local = min(ciclo_min_local, comprimento_ciclo)

            return ciclo_min_local

        grafo = [[] for _ in range(n)]
        for u, v in arestas:
            grafo[u].append(v)
            grafo[v].append(u)

        ciclo_minimo = float('inf')
        for vertice_inicial in range(n):
            comprimento_ciclo = bfs(vertice_inicial, grafo)
            ciclo_minimo = min(ciclo_minimo, comprimento_ciclo)

        return ciclo_minimo if ciclo_minimo != float('inf') else -1
