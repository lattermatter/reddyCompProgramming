# Problem: B. Another Divisibility Problem
# URL: https://codeforces.com/contest/2140/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 07:58:04

from bisect import bisect, bisect_left
from math import floor, log10, gcd, lcm, sqrt, ceil
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
	n = II()
	d = log10(n)
	
	if d == int(d):
		print(n * 2); continue
	
	ans = (n * 10 ** (ceil(d)+1) - n * (n+1)) // n
	ans = 10 ** (ceil(d) + 1) - (n+1)
	print(ans)
	

	