# Problem: E. Mexification
# Contest: Codeforces - Codeforces Round 1047 (Div. 3)
# URL: https://codeforces.com/contest/2137/problem/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-07 08:54:09
# 
# Powered by CP Editor (https://cpeditor.org)

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque, Counter
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list), 
flush = sys.stdout.flush

debug = False
def solve():
	n, k = map(int, input().split())
	a = [int(x) for x in input().split()]
	
	d = [0] * (n+2)
	for i in a:
		d[i] += 1
	
	umex = -1
	umexFlag = False
	mexFlag = False
	mex = -1
	for i in range(n):
		if umexFlag and mexFlag:
			break
		p = d[i]
		if p == 0:
			umexFlag = True; mexFlag = True; continue
		if p != 1:
			mex += 1
			umexFlag = True
		if p == 1:
			if not umexFlag: umex += 1
			mex += 1
	
	umex += 1
	mex += 1
		
	# final state
	fstate = [0] * (n+2)
	for i in range(umex):
		fstate[i] = 1
	if n - umex: fstate[umex] = n - umex
	
	# simulation
	c = 0
	while d != fstate:
		for i in range(n):
			if a[i] > mex or (a[i] <= mex and d[a[i]] > 1):
				a[i] = mex; continue
				
		k -= 1
		if k == 0: print(sum(a)); return
		
		d = [0] * (n+2)
		for i in a:
			d[i] += 1
		
		mexFlag = False
		mex = -1
		for i in range(n):
			if mexFlag: break
			r = d[i]
			if not r: mexFlag = True; continue
			mex += 1
		mex += 1
		# print(d, mex)
	
	mex = 0
	for i in range(n+2):
		if d[i]: mex = max(mex, i)
	
	s = 0
	smex = 0
	fval = -1

	for i in range(n+2):
		if d[i]: s += i

		if d[i] == 0 and fval == -1 and d[i-1] != 0: fval = d[i-1]
		
		smex += i * d[i]
		if i == mex and k % 2: smex += d[i]
	
	if fval == 1: print(s)
	if fval != 1: print(smex)
	
		

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()