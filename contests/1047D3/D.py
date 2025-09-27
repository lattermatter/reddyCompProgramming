# Problem: D. Replace with Occurrences
# Contest: Codeforces - Codeforces Round 1047 (Div. 3)
# URL: https://codeforces.com/contest/2137/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-07 08:04:28
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list), 
flush = sys.stdout.flush

debug = False
def solve():
	n = int(input())
	j = [i for i in range(n)]
	r = [int(x) for x in input().split()]
	b = [[r[i], j[i]] for i in range(n)]
	b.sort()
	
	m = {}
	for i in b:
		m[i[0]] = m.get(i[0], 0) + 1
	for k in m:
		v = m[k]
		if k > v: print(-1); return
		if v % k: print(-1); return

	c = 1
	ans = []
	ans.append([1, b[0][1]])
	cused = 1
	
	for i in range(1, n):
		if b[i][0] == b[i-1][0] and cused < b[i][0]:
			cused += 1
			ans.append([c, b[i][1]]); continue
		
		cused = 1
		c += 1
		ans.append([c, b[i][1]])
	
	ans.sort(key=lambda x: x[1])
	print(*[i[0] for i in ans])
		
	

	
	

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()