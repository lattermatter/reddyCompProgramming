# Problem: E. Interesting Ratio
# Contest: Codeforces - Codeforces Round 1013 (Div. 3)
# URL: https://codeforces.com/problemset/problem/2091/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-06 20:23:25
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
	a = [False] * (n+1)
	
	for i in range(2, ceil(n ** (1/2)) + 1):
		for j in range(2*i, n+1, i):
			a[j] = True
	
	ans = 0	
	for i in range(2, n+1):
		if not a[i]:
			ans += n // i
	
	print(ans)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()