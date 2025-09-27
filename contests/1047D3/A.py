# Problem: A. Collatz Conjecture
# Contest: Codeforces - Codeforces Round 1047 (Div. 3)
# URL: https://codeforces.com/contest/2137/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-09-07 07:36:16
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
	n, x = map(int, input().split())
	print(x * 2 ** n)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()