# Problem: D. Skibidus and Sigma
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-18 10:35:46
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, m = map(int, input().split())
	a = []
	for _ in range(n):
		a.append([int(x) for x in input().split()])
		
	a.sort(key=lambda a: sum(a), reverse=True)
	
	score = 0
	sub = 0
	for i in range(n):
		for j in range(m):
			score += a[i][j] * (n * m + sub)
			sub -= 1
	
	print(score)

for i in range(int(input())):
	print(i) if debug else 0
	solve()