# Problem: C1. Skibidus and Fanum Tax (easy version)
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/C1
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-18 10:14:10
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, m = map(int, input().split())
	a = [int(x) for x in input().split()]
	b = int(input())
	c = [b-i for i in a]
	
	s = min(a[0], c[0])
	for i in range(1, n):
		if a[i] < s and c[i] < s:
			print("NO")
			return
		l = [min(a[i], c[i]), max(a[i], c[i])]
		for i in l:
			if s <= i:
				 s = i
				 break
	
	print("YES")

for i in range(int(input())):
	print(i) if debug else 0
	solve()