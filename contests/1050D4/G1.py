# Problem: G1. Medium Demon Problem (easy version)
# URL: https://codeforces.com/contest/2044/problem/G1
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 20:51:05

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
	k = A()
	a = [[0,0]] + [[k[i],0] for i in range(n)]
	seen = [False] * (n+1)
	mx = 0
	
	for i in range(1,n+1):
		if seen[i]:
			continue
			
		q = deque([a[i]])
		thisOne = set()
		thisOne.add(i)
		
		while q:
			c = q.pop()
			next = c[0]
			depth = c[1]
			
			if not seen[next]: 
				seen[next] = True
				a[next][1] = depth + 1
				thisOne.add(next)
				q.append(a[next])
			else:
				if next in thisOne:
					mx = max(mx, a[next][1])
				else:
					mx = max(mx, depth)
			
				
	print(mx+2)