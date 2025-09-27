# Problem: A. Sublime Sequence
# URL: https://codeforces.com/contest/2148/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 07:35:21

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
	a, b = MI()
	if b % 2:
		print(a)
	else:
		print(0)