# Problem: C. Serval and The Formula
# Contest: Codeforces - Codeforces Round 1011 (Div. 2)
# URL: https://codeforces.com/contest/2085/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-06 10:02:20
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
	x, y = map(int, input().split())	
	if x == y:
		print(-1); return
	
	m = max(x, y)
	r = 0
	while m:
		m = m >> 1
		r += 1
	print(2**r - max(x,y))

		

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()