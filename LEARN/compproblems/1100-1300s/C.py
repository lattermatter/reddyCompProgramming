# Problem: C. Equal Values
# Contest: Codeforces - Educational Codeforces Round 179 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/2111/C
# Memory Limit: 512 MB
# Time Limit: 2000 ms
# START: 2025-09-05 19:34:58
# END: 19:53 (19 min)
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
flush = sys.stdout.flush

debug = False
def solve():
	l = 0
	r = 0
	mn = float("inf")
	n = int(input())
	a = [int(x) for x in input().split()]
	while r < n:
		while r < n and a[l] == a[r]:
			r += 1

		val = a[l] * (l) + a[r-1] * (n-r)
		mn = min(val, mn)
		l = r

	print(mn)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()