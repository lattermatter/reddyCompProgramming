# Problem: B. Skibidus and Ohio
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/contest/2065/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-18 10:12:58
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	s = input()
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			print(1)
			return
	
	print(len(s))

for i in range(int(input())):
	print(i) if debug else 0
	solve()