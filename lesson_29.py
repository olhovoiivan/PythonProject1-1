from collections import defaultdict

class SCC_Kosaraju:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.graph_t = defaultdict(list)
        self.stack = []
        self.visited = [False] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph_t[v].append(u)

    # DFS для формування порядку виходу
    def dfs_fill_stack(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs_fill_stack(v)
        self.stack.append(u)

    # DFS у транспонованому графі
    def dfs_find_scc(self, u, current_scc):
        self.visited[u] = True
        current_scc.append(u)
        for v in self.graph_t[u]:
            if not self.visited[v]:
                self.dfs_find_scc(v, current_scc)

    def find_scc(self):
        # 1. Заповнення стеку
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs_fill_stack(i)

        # 2. Пошук компонент у транспонованому графі
        self.visited = [False] * self.n
        scc_list = []

        while self.stack:
            u = self.stack.pop()
            if not self.visited[u]:
                component = []
                self.dfs_find_scc(u, component)
                scc_list.append(sorted(component))

        return scc_list
      
# Тест
g = SCC_Kosaraju(8)
edges = [
    (0, 1), (1, 2), (2, 0),
    (2, 3), (3, 4), (4, 5),
    (5, 6), (6, 4), (6, 7)
]

for a, b in edges:
    g.add_edge(a, b)

result = g.find_scc()
print("Компоненти сильної зв’язності (Kosaraju):")
for comp in result:
    print(comp)
