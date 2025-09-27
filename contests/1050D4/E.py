# Problem: E. Insane Problem
# URL: https://codeforces.com/contest/2044/problem/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 19:05:27

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list)
flush = sys.stdout.flush
input = sys.stdin.readline
I = lambda: input().strip()
II = lambda: int(input())
A = lambda: [int(x) for x in input().split()]

debug = False

for i in range(II()):
	k, l1, r1, l2, r2 = A()
	n = 0
	ans = 0
	
	while k ** n * l1 <= r2:
		lc = ceil(l2 / k ** n)
		rc = floor(r2 / k ** n)
		# print(lc, rc, k ** n * l1)
		
		ans += max(min(r1, rc) - max(l1, lc) + 1, 0)
		
	
		n += 1
	
	print(ans)