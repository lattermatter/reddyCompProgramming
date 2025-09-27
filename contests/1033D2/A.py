# Problem: A. Square of Rectangles
# Contest: Codeforces - Codeforces Round 1033 (Div. 2) and CodeNite 2025
# URL: https://codeforces.com/contest/2120/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-22 13:41:03
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	l1, w1, l2, w2, l3, w3 = map(int, input().split())
	if l1 > w1: 
		if (l1 == l2 + l3 and (
			w1 + w2 == l1
			and w2 == w3
		)) or (l1 == l2 and l2 == l3 and w1 + w2 + w3 == l1):
			print("YES")
			return
	else:
		if (w1 == w2 + w3 and (
			l1 + l2 == w1 and
			l2 == l3
		)) or (w1 == w2 and w2 == w3 and l1 + l2 + l3 == w1):
			print("YES")
			return
	print("NO")

for i in range(int(input())):
	print(i) if debug else 0
	solve()