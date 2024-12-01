from typing import List

class Solution:
    def dfs(self, node: int, parent: int, dist: int, root: int, threshold: int, goodness: List[int], adjList: List[List[int]]) -> None:
        if dist >= threshold:
            return
        goodness[root] += 1
        for neighbor in adjList[node]:
            if neighbor != parent:
                self.dfs(neighbor, node, dist + 1, root, threshold, goodness, adjList)

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        adjList1 = [[] for _ in range(n)]
        adjList2 = [[] for _ in range(m)]
        
        for edge in edges1:
            u, v = edge
            adjList1[u].append(v)
            adjList1[v].append(u)
        
        for edge in edges2:
            u, v = edge
            adjList2[u].append(v)
            adjList2[v].append(u)
        
        goodness1 = [0] * n
        goodness2 = [0] * m
        
        for node in range(n):
            self.dfs(node, -1, 0, node, k + 1, goodness1, adjList1)
        
        for node in range(m):
            self.dfs(node, -1, 0, node, k, goodness2, adjList2)
        
        maxGoodness = max(goodness2)
        
        result = [goodness1[node] + maxGoodness for node in range(n)]
        
        return result