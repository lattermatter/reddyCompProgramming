# Problem: C. Asuna and the Mosquitoes
# Contest: Codeforces - Codeforces Round 1014 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2092/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-05 19:55:59-20:28, 30 mins
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
	a = [int(x) for x in input().split()]
	mx = max(a)
	a.remove(mx)
	
	e = []
	o = []
	
	for i in a:
		if i % 2: o.append(i); continue
		e.append(i)
	
	if mx % 2 and not e: print(mx); return
	if not mx % 2 and not o: print(mx); return
	
	both = (bool(e) and bool(o))
	se = sum(e) % 2
	so = sum(o) % 2
	
	if mx % 2:
		if both: print(mx + sum(e) - 1 + sum(o) - len(o) + 1)
		else: print(mx + sum(e))
	else:
		if both: print(mx + o[0] + sum(e) - 1 + sum(o[1:]) - (len(o)-1) + 1)
		else: print(mx + sum(o) - len(o) + 1)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()