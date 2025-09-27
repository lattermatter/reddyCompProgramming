# Problem: D. Serval and Kaitenzushi Buffet
# Contest: Codeforces - Codeforces Round 1011 (Div. 2)
# URL: https://codeforces.com/contest/2085/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-09-06 10:36:10
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
	# backward dp
	n, k = map(int, input().split())
	a = [int(x) for x in input().split()]
	
	dp = [0] * n
	
	pick = [0] * n
	change = {}
	
	for i in range(n-1, -1, -1):
		pick[i] = (n-1-i+1) // (k+1)
		if i+1 != n and pick[i] != pick[i+1]:
			change[pick[i+1]] = i+1
 
	
	for i in range(n-k-1, -1, -1):
		prev = pick[i] - 1
		premx = dp[change[prev]]
		
		dp[i] = max(dp[i+1], premx + a[i]) # fails because it only picks one max in a range when you can actually use 2
	
 
	print(dp[0])
 
for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()