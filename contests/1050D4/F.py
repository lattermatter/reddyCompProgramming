# Problem: F. Easy Demon Problem
# URL: https://codeforces.com/contest/2044/problem/F
# Memory Limit: 256 MB
# Time Limit: 4000 ms
# START: 20:09:31

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

n, m, q = A()
a = A()
b = A()

pa = [0]
pb = [0]
for i in a: pa.append(pa[-1] + i)
for i in b: pb.append(pb[-1] + i)

sx = pa[-1]
sy = pb[-1]
total = sx * sy


for _ in range(q):
	t = II()
	f = False
	for x in a:
		for y in b:
			# print(x, y, -1 * (- (sx * y) - (sy * x) + x * y))
			if total - (sx * y) - (sy * x) + x * y == t: f = True; break
		
	if f: print("YES")
	else: print("NO")
			
			
	
