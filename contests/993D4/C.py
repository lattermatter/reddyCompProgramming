# Problem: C. Hard Problem
# URL: https://codeforces.com/contest/2044/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 18:47:21

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
	m, a, b, c = A()
	before = min(a, m) + min(b, m)
	ans = before + min(2*m - before, c)
	print(ans)