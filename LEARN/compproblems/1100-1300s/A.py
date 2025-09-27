# Problem: A. LRC and VIP
# Contest: Codeforces - Codeforces Round 1023 (Div. 2)
# URL: https://codeforces.com/contest/2107/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-30 20:04:30
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	a = [int(x) for x in input().split()]
	final = []
	mx = max(a)
	for i in range(n):
		if a[i] == mx:
			final.append("2")
		else:
			final.append("1")
			
	if "1" not in final:
		print("NO")
		return
	else:
		print("YES")
		print(" ".join(final))

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()