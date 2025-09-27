# Problem: D. Sum of LDS
# Contest: Codeforces - Codeforces Round 1039 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2128/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-31 19:40:02
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	a = [int(x) for x in input().split()] + [0]
	
	# editiorial sol
	dp = [1] * n
	
	for i in range(n-2, -1, -1):
		dp[i] = dp[i+1] + (n-i) if a[i] > a[i+1] else dp[i+1] + 1
	
	# my sol
	dp = 1
	s = 1
	for i in range(1, n):
		dp += (i+1) if a[i] < a[i-1] else 1
		s += dp
	
	print(s)

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()