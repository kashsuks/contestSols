from typing import List

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        numNodes = len(edges) + 1
        
        adjList = [[] for _ in range(numNodes)]
        for edge in edges:
            u, v, w = edge
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        dp = [[0, 0] for _ in range(numNodes)]

        self.dfs(0, -1, k, adjList, dp)

        return dp[0][0]
    
    def dfs(self, node: int, parent: int, k: int, adjList: List[List[tuple]], dp: List[List[int]]):
        gains = []
        totalWithoutConnection = 0

        for neighbourNode, weight in adjList[node]:
            if neighbourNode == parent:
                continue

            self.dfs(neighbourNode, node, k, adjList, dp)

            totalWithoutConnection += dp[neighbourNode][0]

            gainIfConnected = weight + dp[neighbourNode][1] - dp[neighbourNode][0]
            gains.append(gainIfConnected)

        gains.sort(reverse=True)

        totalWithConnection = totalWithoutConnection
        maxConnWithoutConnection = k
        for i in range(min(len(gains), maxConnWithoutConnection)):
            if gains[i] > 0:
                totalWithConnection += gains[i]
        dp[node][0] = totalWithConnection

        if k >= 1:
            totalWithConnectionOneLess = totalWithoutConnection
            maxConnWithConnection = k - 1
            for i in range(min(len(gains), maxConnWithConnection)):
                if gains[i] > 0:
                    totalWithConnectionOneLess += gains[i]
            dp[node][1] = totalWithConnectionOneLess
        else:
            dp[node][1] = totalWithoutConnection
