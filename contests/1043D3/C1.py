# Problem: C1. The Cunning Seller (easy version)
# Contest: Codeforces - Codeforces Round 1043 (Div. 3)
# URL: https://codeforces.com/contest/2132/problem/C1
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-21 07:59:04
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	b3 = []
	sub = 1
	mod = 3
	cnt = 0
	while n > 0:
		cnt = 0
		while n % mod != 0:
			cnt += 1
			n -= sub
		b3.append(cnt)
		sub *= 3
		mod *= 3
	
	total = 0
	for i in range(len(b3)):
		total += int(b3[i] * (3 ** (i+1) + (i) * (3 ** (i-1))))
	print(total)

for i in range(int(input())):
	print(i) if debug else 0
	solve()