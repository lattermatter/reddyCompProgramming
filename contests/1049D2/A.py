# Problem: A. Shift Sort
# URL: https://codeforces.com/contest/2140/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 07:36:14

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
	s = I()
	m = "".join(sorted(s))
	
	if s == m:
		print(0); continue
	
	c = s.count("0")
	d = s.count("1")
	# print(c,d,s)
	z = c
	o = d
	for i in range(c):
		if s[i] == "0":
			z -= 1
	
	for i in range(n-1, n-d-1, -1):
		if s[i] == "1":
			o -= 1

	print(min(z, o))
