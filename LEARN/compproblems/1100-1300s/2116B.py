# Problem: B. Gellyfish and Baby's Breath
# Contest: Codeforces - Codeforces Round 1028 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2116/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-23 15:36:29
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
mod = 998244353

def solve():
	n = int(input())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	
	am = 0
	bm = 0
	ai = 0
	bi = 0
	ans = []
	for i in range(n):
		if a[i] > am:
			am = a[i]
			ai = i
			
		if b[i] > bm:
			bm = b[i]
			bi = i

		x = pow(2, am, mod) + pow(2, b[i+1 - ai - 1], mod)
		y = pow(2, bm, mod) + pow(2, a[i+1 - bi - 1], mod)
		k = max(x, y)
		# print(x, y)

		ans.append(k)
	
	print(" ".join([str(x) for x in ans]))

for i in range(int(input())):
	print(i) if debug else 0
	solve()