# Problem: B. Add 0 or K
# Contest: Codeforces - Codeforces Round 1045 (Div. 2)
# URL: https://codeforces.com/contest/2134/problem/B
# Memory Limit: 256 MB
# Time Limit: 1500 ms
# START: 2025-08-26 07:59:13
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, k = map(int, input().split())
	target = k + 1
	arr = [int(x) for x in input().split()]
	final = []
	for i in arr:
		diff = i % target
		final.append(i + k * diff)
	
	print(" ".join([str(x) for x in final]))

for i in range(int(input())):
	print(i) if debug else 0
	solve()