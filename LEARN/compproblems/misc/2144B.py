# Problem: B. Maximum Cost Permutation
# URL: https://codeforces.com/contest/2144/problem/B
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 11:04:38

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
	
	cost = 0
	first0 = -1
	last0 = -1
	s = -1
	f = -1
	c = a.count(0)
	if c == 1:
		b = list({i for i in range(1, n+1)} - set(a) - {0})[0]

	
	for i in range(n):
		if a[i] == 0 and c == 1:
			a[i] = b
		if a[i] != i+1:
			if s == -1: s = i
			f = max(f, i)
		
	if s == f: print(0); continue
	print(f-s+1)