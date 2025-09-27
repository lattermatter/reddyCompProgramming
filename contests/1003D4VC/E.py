# Problem: E. Skibidus and Rizz
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/E
# Memory Limit: 256 MB
# Time Limit: 1500 ms
# START: 2025-08-18 11:27:34
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, m, k = map(int, input().split())
	if k < abs(n-m) or k > max(n, m):
		print(-1)
		return
	
	def fill(s, c1, o, c2):
		print(s * k + (o+s) * (c1-k) + o * (c2-(c1-k)))
	
	if n > m:
		fill("0", n, "1", m)
	else:
		fill("1", m, "0", n)

for i in range(int(input())):
	print(i) if debug else 0
	solve()
	
	