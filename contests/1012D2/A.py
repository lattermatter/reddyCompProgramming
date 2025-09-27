# Problem: A. Serval and String Theory
# Contest: Codeforces - Codeforces Round 1011 (Div. 2)
# URL: https://codeforces.com/contest/2085/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-09-06 09:14:36
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
	s = input()	
	
	if k == 0:
		if s >= s[n:0:-1] + s[0]:
			print("NO"); return
		print("YES"); return
	
	if s[0]*n == s:
		print("NO"); return # all same
	
	print("YES")

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()