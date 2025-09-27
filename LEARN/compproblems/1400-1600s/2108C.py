# Problem: C. Neo's Escape
# Contest: Codeforces - Codeforces Round 1022 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2108/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-05 11:04:05
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
	n = int(input())
	a = [0] + [int(x) for x in input().split()] + [0]
	delta = []
	for i in range(n+1):
		if a[i] > a[i+1]: delta.append(-1)
		elif a[i] < a[i+1]: delta.append(1)
		else: delta.append(delta[-1])
	
	c = 0
	for i in range(n+1):
		if delta[i] == 1 and delta[i+1] == -1:
			c += 1
	
	print(c)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()