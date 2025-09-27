# Problem: A. Painting With Two Colors
# Contest: Codeforces - Codeforces Round 1045 (Div. 2)
# URL: https://codeforces.com/contest/2134/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-26 07:43:14
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, a, b = map(int, input().split())
	
	if b % 2 != n % 2:
		print("NO")
	elif a % 2 != n % 2 and a >= b:
		print("NO")
	else:
		print("YES")

for i in range(int(input())):
	print(i) if debug else 0
	solve()