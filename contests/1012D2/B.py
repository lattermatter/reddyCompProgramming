# Problem: B. Serval and Final MEX
# Contest: Codeforces - Codeforces Round 1011 (Div. 2)
# URL: https://codeforces.com/contest/2085/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-09-06 09:24:44
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
	
	first = -1
	for i in range(n):
		if a[i] == 0:	
			first = i; break
	
	if first == -1:
		print(1)
		print(1, n); return
	
	if first != 0 and first != n-1:
		print(2)
		print(first+1, n)
		print(1, n-(n-(first+1)))
		return
	
	if a[n-2] == 0 or a[n-1] == 0:
		if first == n-1:
			print(2)
			print(n-1, n)
			print(1, n-1)
			return
		print(3)	
		print(1, n-2)
		print(2, 3)
		print(1, 2)
		return
	
	print(2)
	print(1, n-2)
	print(1, 3)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()