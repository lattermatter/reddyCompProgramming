# Problem: B. Square Pool
# Contest: Codeforces - Codeforces Round 1033 (Div. 2) and CodeNite 2025
# URL: https://codeforces.com/contest/2120/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-22 14:10:53
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, s = map(int, input().split())
	
	c = 0
	for i in range(n):
		dx, dy, x1, y1 = map(int, input().split())
		if (x1 == y1) and (dx == dy):
			c += 1
		if (y1 == -1 * x1 + s) and (dx != dy):
			c += 1
	
	print(c)

for i in range(int(input())):
	print(i) if debug else 0
	solve()