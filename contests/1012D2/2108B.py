# Problem: B. SUMdamental Decomposition
# Contest: Codeforces - Codeforces Round 1022 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2108/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-09-06 19:18:41-19:52 (34 mins, fail)
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list), 
flush = sys.stdout.flush

debug = False
def solve():
	n, x = map(int, input().split())
	r = x
	if x == 0:
		if n == 1:
			print(-1)
		elif n % 2:
			print(n-1 + 4)
		else: 
			print(n)
		return
	
	if x == 1:
		if n % 2:
			print(n)
		else:
			print(n-1 + 4)
		return
	
	
	odd = x % 2
	ones = odd
	while x:
		x = x >> 1
		ones += x % 2
	
	# equal
	if n <= ones:
		print(r); return
	
	extra = n - ones
	# not equal
	if extra % 2 == 0:
		print(r + extra); return # just add extra 1s
	
	# just add an extra one in the number to compensate
	print(r + extra + 1)
	

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()