# Problem: B. Fun Permutation
# Contest: Codeforces - Codeforces Round 1047 (Div. 3)
# URL: https://codeforces.com/contest/2137/problem/B
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-07 07:39:46
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
	n = int(input())
	a = [int(x) for x in input().split()]
	ans = []
	for i in a:
		ans.append(n-i+1)
	
	print(*ans)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()