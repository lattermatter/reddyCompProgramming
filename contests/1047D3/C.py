# Problem: C. Maximum Even Sum
# Contest: Codeforces - Codeforces Round 1047 (Div. 3)
# URL: https://codeforces.com/contest/2137/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-07 07:50:33
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
	a, b = map(int, input().split())
	
	if a % 2 == 0 and b % 2:
		print(-1); return
	
	if a % 2 and b % 2:
		print(a * b + 1); return
	
	if b % 2 == 0 and (a % 2 == 0 or b % 4 == 0):
		print(a * b // 2 + 2); return
	
	print(-1)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()