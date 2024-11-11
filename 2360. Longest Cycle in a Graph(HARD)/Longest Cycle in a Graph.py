from typing import List, Dict


class Solution:
    def longestCycle(self, arestas: List[int]) -> int:
        def encontrar_comprimento_ciclo(inicio: int) -> int:

            atual = inicio
            comprimento_caminho = 0
            distancias_nos: Dict[int, int] = {}

            # Explora o caminho até encontrar um ciclo ou um fim
            while atual != -1 and not visitado[atual]:
                visitado[atual] = True
                distancias_nos[atual] = comprimento_caminho

                proximo_no = arestas[atual]
                atual = proximo_no
                comprimento_caminho += 1

                if atual in distancias_nos:
                    return comprimento_caminho - distancias_nos[atual]

            return -1


        n = len(arestas)
        visitado = [False] * n
        ciclo_mais_longo = -1

        for no_inicial in range(n):
            if not visitado[no_inicial]:
                comprimento_ciclo = encontrar_comprimento_ciclo(no_inicial)
                ciclo_mais_longo = max(ciclo_mais_longo, comprimento_ciclo)

        return ciclo_mais_longo
