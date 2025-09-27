# Problem: F. Skibidus and Slay
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/F
# Memory Limit: 512 MB
# Time Limit: 4000 ms
# START: 2025-08-18 13:25:45
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	color = [int(x)-1 for x in input().split()]	
	edge = [list(map(int, input().split())) for i in range(n-1)]
	adj = [list() for _ in range(n)]
	works = ["0" for _ in range(n)]

	for i in edge:
		adj[i[0]-1].append(i[1]-1)
		adj[i[1]-1].append(i[0]-1)
	
	def check(curr):
		curr_color = color[curr]
		adj_colors = {i: 0 for i in range(n)}
		for next in adj[curr]:
			next_color = color[next]
			adj_colors[next_color] += 1
			
		if adj_colors[curr_color] >= 1:
			works[curr_color] = "1"
			
		for adj_color in adj_colors:
			if adj_colors[adj_color] >= 2:
				works[adj_color] = "1"
		
	for i in range(n):
		check(i)
	
	print("".join(works))
	
	

for i in range(int(input())):
	print(i) if debug else 0
	solve()