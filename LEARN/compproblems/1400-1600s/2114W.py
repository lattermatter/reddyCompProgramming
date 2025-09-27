# Problem: E. Kirei Attacks the Estate
# Contest: Codeforces - Codeforces Round 1027 (Div. 3)
# URL: https://codeforces.com/problemset/problem/2114/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-01 13:48:34
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
flush = sys.stdout.flush

#340-853
debug = False
def solve():
	n = int(input())
	danger = [int(x) for x in input().split()]
	edges = []
	adj = [list() for _ in range(n)]
	seen = [False] * n 
	f = [0] * n
	g = [0] * n
	
	for _ in range(n-1):
		edges.append(list(map(int, input().split())))
	
	for edge in edges:
		adj[edge[0]-1].append(edge[1]-1)
		adj[edge[1]-1].append(edge[0]-1)
		
	# begin traversal
	q = deque([[i, 0] for i in adj[0]]) # store each nodes parent to access the best danger
	f[0] = danger[0]; g[0] = danger[0]
	seen[0] = True
	
	while q:
		if debug: print(q)
		curr, parent = q.pop() # use dfs
		f[curr] = danger[curr] - min(0, g[parent])
		g[curr] = danger[curr] - max(0, f[parent])
		seen[curr] = True
		
		for next in adj[curr]:
			if not seen[next]:
				q.append([next, curr]) # curr is the parent of next
	
	print(*f)
	
	
for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()