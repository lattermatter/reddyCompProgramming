# Problem: A. Maple and Multiplication
# URL: https://codeforces.com/contest/2139/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 07:37:09

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
	if a == b:
		print(0)
	elif a % b == 0 or b % a == 0:
		print(1)
	else:
		print(2)
		