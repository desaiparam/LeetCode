class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        # BFS with state: (node, last_color, distance)
        # 0 = red, 1 = blue
        queue = [(0, 0, 0), (0, 1, 0)]  # Start with both colors from node 0
        visited = set()
        result = [-1] * n
        result[0] = 0
        
        while queue:
            node, last_color, dist = queue.pop(0)
            
            if (node, last_color) in visited:
                continue
            visited.add((node, last_color))
            
            # Explore opposite color edges
            if last_color == 0:  # Last was red, now take blue
                for next_node in blue_graph[node]:
                    if result[next_node] == -1:
                        result[next_node] = dist + 1
                    queue.append((next_node, 1, dist + 1))
            else:  # Last was blue, now take red
                for next_node in red_graph[node]:
                    if result[next_node] == -1:
                        result[next_node] = dist + 1
                    queue.append((next_node, 0, dist + 1))
        
        return result