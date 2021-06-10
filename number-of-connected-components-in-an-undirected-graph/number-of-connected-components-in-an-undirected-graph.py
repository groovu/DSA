class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0] * n
        adj = {}
        
        for i in range(n):
            adj[i] = []
        
        for e in edges:
            out = e[0]
            adj[out].append(e[1])
            adj[e[1]].append(out)
            
        print(adj)
        
        def dfs(node):
            if visited[node] == 0:
                visited[node] = 1
                for i in adj[node]:
                    dfs(i)
            return
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i)
        return count