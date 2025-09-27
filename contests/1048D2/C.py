# Problem: C. Cake Assignment
# URL: https://codeforces.com/contest/2139/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 08:49:52

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
	k, x = MI()
	
	a = x 
	b = 2 ** (k+1) - x
	
	ops = []
	
	while a != b:
		if a < b:
			b = b - a
			a = a * 2
			ops.append(1)
		else:
			a = a - b
			b = b * 2
			ops.append(2)
	
	print(len(ops)); print(*ops[::-1])
				
		