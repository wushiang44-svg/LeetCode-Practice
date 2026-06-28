class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        return self.dfs(0, -1, graph, hasApple)
            
    
    def dfs(self, node, parent, graph, hasApple):
        total = 0

        for child in graph[node]:
            if child == parent:
                continue
            
            child_time = self.dfs(child, node, graph, hasApple)

            if child_time > 0 or hasApple[child]:
                total += child_time + 2

        
        return total