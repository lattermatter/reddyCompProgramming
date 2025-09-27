# Problem: B. Normal Problem
# URL: https://codeforces.com/contest/2044/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 18:45:53

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
	s = I()
	final = ""
	for i in s[::-1]:
		if i == "p":
			final += "q"
		if i == "q":
			final += "p"
		if i == "w":
			final += "w"
	print(final)