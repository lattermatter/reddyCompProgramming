# Problem: B. Cake Collection
# URL: https://codeforces.com/contest/2139/problem/B
# Memory Limit: 512 MB
# Time Limit: 1000 ms
# START: 07:42:45

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
	a = A()
	
	a.sort(reverse=True)
	ans = 0
	for i in range(n):
		ans += max(a[i] * (m-i), 0)
	
	print(ans)