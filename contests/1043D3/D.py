# Problem: D. From 1 to Infinity
# Contest: Codeforces - Codeforces Round 1043 (Div. 3)
# URL: https://codeforces.com/contest/2132/problem/D
# Memory Limit: 256 MB
# Time Limit: 1500 ms
# START: 2025-08-21 19:36:46
# 
# Powered by CP Editor (https://cpeditor.org)

from math import log10, floor
from bisect import bisect_left

debug = False

# precomp


	
def digitN(x, n):
	return int(x % (10 ** (n+1)) // 10 ** n)
	
def x999(k):
	n = floor(log10(k)) + 1
	x = k // 10 ** (n-1)
	return int((x+1) * 45 * (n-1) * 10 ** (n-2) + x * (x+1) // 2 * 10 ** (n-1))
	
by10 = [0]
for i in range(0, 18):
	by10.append(by10[-1] + (10 ** (i+1) - 10 ** i) * (i+1))

def solve():
	# what number is at the kth digit?
	# get close with binary search
	k = int(input())
	upToIndex = bisect_left(by10, k) # also digits per number
	start = 10 ** (upToIndex - 1) - 1
	x = start + (k - by10[upToIndex - 1]) // upToIndex # starting index counts 
	leftover = (k - by10[upToIndex - 1]) % upToIndex
	extra = sum([int(x) for x in str(x+1)[:leftover]]) # extra of x+1, just find digits 1-x inclusive
	
	s = 0
	
	for d in range(floor(log10(x)) + 1):
		m = digitN(x, d)
		print(m) if debug else 0
		
		if d == 0:
			s += m * (m+1) // 2
			continue
		
		s += m * (x % 10 ** d + 1) + x999(m * 10 ** (d) - 1) if m != 0 else 0 # place + 9-series of place
	
	print(s + extra)
	

for i in range(int(input())):
	print(i) if debug else 0
	solve()