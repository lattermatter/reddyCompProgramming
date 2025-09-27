# Problem: D. Destruction of the Dandelion Fields
# URL: https://codeforces.com/contest/2148/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 07:51:25

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
	n = II()
	a = A()
	
	o = 0
	e = 0
	oa = []
	ea = []
	for i in a:
		if i % 2:
			o += 1
			oa.append(i)
		else:
			e += 1
			ea.append(i)
	
	if o == 0:
		print(0); continue
	
	oa.sort()
	ea.sort()

	ans = oa.pop()
	while ea:
		ans += ea.pop()
	
	for i in range(len(oa)-1, (len(oa)+1)//2 - 1, -1):
		ans += oa[i]
	
	print(ans)