n = 6
adj = [[] for _ in range(n)]
visited = [False] * n

adj[0] = [1, 2, 4]
adj[1] = [3, 4]
adj[2] = [5]

from collections import deque

depths = [float("inf")] * n

for i in range(n):
	if visited[i]: continue
	
	q = deque([i])
	depths[i] = 0
	
	while q:	
		node = q.pop()
		depth = depths[node]
		visited[node] = True
		
		print(node, depth)
		
		for next in adj[node]:
			if visited[next]: continue
			q.append(next)
			depths[next] = min(depths[next], depth+1)
			
print(depths)
		