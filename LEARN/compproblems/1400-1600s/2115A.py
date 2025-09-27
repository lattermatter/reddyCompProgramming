# Problem: A. Gellyfish and Flaming Peony
# Contest: Codeforces - Codeforces Round 1028 (Div. 1)
# URL: https://codeforces.com/problemset/problem/2115/A
# Memory Limit: 512 MB
# Time Limit: 2000 ms
# START: 2025-08-31 21:12:50
# 
# Powered by CP Editor (https://cpeditor.org)

from math import gcd

debug = False
def solve():
	n = int(input())
	a = list(reversed([int(x) for x in input().split()]))
	
	g = a[0]
	for i in range(n): g = gcd(g, a[i])
	
	if g in a: print(n - a.count(g)); return # ; works in python same line??
	
	dp = [5] * (max(a)+1)
	for ai in a:
		for c in range(1, max(a)+1):
			m = gcd(ai, c)
			dp[m] = min(dp[m], dp[c] + 1) # update the way to get to the gcd, 1 plus way to get to the og
		dp[ai] = 0

	print(n-1 + dp[g])

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()