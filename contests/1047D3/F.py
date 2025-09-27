# Problem: F. Prefix Maximum Invariance
# URL: https://codeforces.com/contest/2137/problem/F
# Memory Limit: 256 MB
# Time Limit: 3000 ms
# START: 14:15:57

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

for i in range(II())):
	