# Problem: A. Redstone?
# Contest: Codeforces - Codeforces Round 1044 (Div. 2)
# URL: https://codeforces.com/contest/2133/problem/0
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-24 07:45:59
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	a = [int(x) for x in input().split()]
	
	for i in a:
		if a.count(i) > 1:
			print("YES")
			return
	print("NO")

for i in range(int(input())):
	print(i) if debug else 0
	solve()