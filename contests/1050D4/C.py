# Problem: C. Pacer
# URL: https://codeforces.com/contest/2148/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 07:42:13

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list)
flush = sys.stdout.flush
I = lambda: input()
II = lambda: int(input())
MI = lambda: map(int, input().split())
A = lambda: [int(x) for x in input().split()]

debug = False

for i in range(II()):
	n, m = MI()
	a = [[0, 0]] + [A() for _ in range(n)]
	
	t = 0
	for i in range(n):
		d = a[i+1][0] - a[i][0]
		s = a[i+1][1] - a[i][1]
		
		if d % 2 and s:
			t += d
		elif not d % 2 and not s:
			t += d
		else:
			t += d-1
	
	t += m - a[-1][0]
	
	print(t)