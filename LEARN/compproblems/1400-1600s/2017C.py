# Problem: C. Maximum Subarray Sum
# Contest: Codeforces - Codeforces Round 1023 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2107/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-05 11:12:42
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
	n, k = map(int, input().split())
	s = [int(x) for x in input().strip()]
	a = [int(x) for x in input().split()]
	adiff = a.copy()
	
	INF = int(-1 * 1e13)
	first = -1
	for i in range(n):
		if s[i] == 0:
			adiff[i] = INF
			first = i
	
	mx = INF
	run = 0
	for i in adiff:
		run = max(run + i, i)
		mx = max(mx, run)
		
	if mx > k:
		print("NO"); return
		
	if first == -1: # no 0s in array, already works
		if mx == k:
			print("YES"); print(*a); return
		print("NO"); return
	
	print("YES")
	pref = [0]
	suf = [0]
	
	p = 0
	s = 0
	for i in range(first-1, -1, -1):
		p += adiff[i]
		pref.append(p)
	
	for i in range(first+1, n):
		s += adiff[i]
		suf.append(s)
	
	adiff[first] = k - (max(pref) + max(suf))
	print(*adiff)
	

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()