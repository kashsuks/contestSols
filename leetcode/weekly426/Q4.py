from collections import deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        n1 = max(max(edge[0], edge[1]) for edge in edges1) + 1
        n2 = max(max(edge[0], edge[1]) for edge in edges2) + 1
        
        adj1 = [[] for _ in range(n1)]
        adj2 = [[] for _ in range(n2)]
        
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        def bfs(n, adj):
            parity = [-1] * n
            queue = deque([0])
            parity[0] = 0
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if parity[neighbor] == -1:
                        parity[neighbor] = parity[node] ^ 1
                        queue.append(neighbor)
            return parity
        
        p1 = bfs(n1, adj1)
        p2 = bfs(n2, adj2)
        
        even1 = p1.count(0)
        odd1 = p1.count(1)
        
        even2 = p2.count(0)
        odd2 = p2.count(1)
        
        max2 = max(even2, odd2)
        
        return [max2 + (even1 if p1[i] == 0 else odd1) for i in range(n1)]