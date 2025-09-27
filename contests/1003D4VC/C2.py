# Problem: C2. Skibidus and Fanum Tax (hard version)
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/C2
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-18 10:49:14
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect_left

debug = False
def solve():
	n, m = map(int, input().split())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	b = sorted(list(set(b)))
	
	start = a[0]
	for i in b:
		start = min(start, i - a[0])
	
	print(start, "start") if debug else 0
	print(b) if debug else 0
	for i in range(1, n):
		next = start + a[i]
		print(next, "next", i) if debug else 0
		index = bisect_left(b, next)
		print(index, "index") if debug else 0
		if index > len(b)-1:
			if a[i] < start:
				print("NO")
				return
		elif max(a[i], b[index] - a[i]) < start:
			print("NO")
			return
		next = a[i] if (index > len(b) - 1 or (a[i] <= b[index] - a[i] and a[i] >= start)) else b[index] - a[i]
		start = next
		print(start, "start") if debug else 0
	
	print("YES")

for i in range(int(input())):
	solve()