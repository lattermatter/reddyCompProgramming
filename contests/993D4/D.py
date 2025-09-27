# Problem: D. Harder Problem
# URL: https://codeforces.com/contest/2044/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 18:50:40

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
	n = II()
	a = A()
	f = []
	s = [False] * int(n + 5)
	for i in a:
		if s[i]:
			continue
		s[i] = True
		f.append(i)
	
	for i in range(1, len(s)):
		if len(f) < n and not s[i]:
			f.append(i)
			
	print(*f)