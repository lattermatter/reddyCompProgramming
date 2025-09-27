# Problem: A. Homework
# Contest: Codeforces - Codeforces Round 1043 (Div. 3)
# URL: https://codeforces.com/contest/2132/problem/0
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-21 07:35:20
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	a = input()
	m = int(input())
	b = input()
	c = input()
	
	for i in range(m):
		if c[i] == "D":
			a = a + b[i]
		else:
			a = b[i] + a
			
	print(a)

for i in range(int(input())):
	print(i) if debug else 0
	solve()