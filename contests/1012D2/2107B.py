# Problem: B. Apples in Boxes
# Contest: Codeforces - Codeforces Round 1023 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2107/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-09-06 20:00:16
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
	n, k = map(int, input().split())
	a = [int(x) for x in input().split()]
	
	mx = max(a)
	for i in range(n):
		if a[i] == mx:
			r = i; break
			
	a[r] -= 1
	
	if max(a) - min(a) > k:
		print("Jerry"); return
		
	a[r] += 1
	
	if sum(a) % 2:
		print("Tom")
	else:
		print("Jerry")

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()