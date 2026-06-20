from typing import List, Tuple


class Solution:
    def isSafe(
        self,
        node: int,
        color: List[int],
        graph: List[List[int]],
        n: int,
        col: int,
    ) -> bool:
        for neighbour in range(n):
            if graph[node][neighbour] and color[neighbour] == col:
                return False
        return True

    def solve(
        self,
        node: int,
        color: List[int],
        graph: List[List[int]],
        m: int,
        n: int,
    ) -> bool:
        if node == n:
            return True

        for col in range(1, m + 1):
            if self.isSafe(node, color, graph, n, col):
                color[node] = col

                if self.solve(node + 1, color, graph, m, n):
                    return True

                color[node] = 0

        return False

    def graphColoring(self, edges: List[Tuple[int, int]], m: int, n: int) -> bool:
        graph = [[0] * n for _ in range(n)]

        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1

        color = [0] * n
        return self.solve(0, color, graph, m, n)


if __name__ == "__main__":
    solution = Solution()

    n1, m1 = 4, 3
    edges1 = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    print(f"N = {n1}, M = {m1}, Edges = {edges1}")
    print(f"Output: {solution.graphColoring(edges1, m1, n1)}")
    print("Expected: True\n")

    n2, m2 = 3, 2
    edges2 = [(0, 1), (1, 2), (0, 2)]
    print(f"N = {n2}, M = {m2}, Edges = {edges2}")
    print(f"Output: {solution.graphColoring(edges2, m2, n2)}")
    print("Expected: False\n")

    n3, m3 = 5, 3
    edges3 = [(0, 1), (1, 2), (0, 2), (2, 3), (2, 4), (3, 4)]
    print(f"N = {n3}, M = {m3}, Edges = {edges3}")
    print(f"Output: {solution.graphColoring(edges3, m3, n3)}")
    print("Expected: True")
