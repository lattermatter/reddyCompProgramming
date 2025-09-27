# Problem: C. Ultimate Value
# URL: https://codeforces.com/contest/2140/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 10:01:55

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
	
	
	# end on first turn
	t = 0
	for i in range(n):
		if i % 2: t -= a[i]
		else: t += a[i]
	ans = t
	
	if n == 1: print(ans); continue
	
	# do one turn then end
	base = ans
	
	# maximum same parity even and odd
	ans = base + max((n-1) - (n-1) % 2, (n-2) - (n-2) % 2)
	# different parities
	modd = meven = float("inf")
	for i in range(n):
		if i % 2:
			ans = max(base + i + 2 * a[i] - meven, ans)
			modd = min(i - 2 * a[i], modd)
		else:
			ans = max(base + i - 2 * a[i] - modd, ans)
			meven = min(i + 2 * a[i], meven)
	
	print(ans)
	