# Problem: A. Shashliks
# Contest: Codeforces - Codeforces Round 1031 (Div. 2)
# URL: https://codeforces.com/contest/2113/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-27 18:11:53
# 
# Powered by CP Editor (https://cpeditor.org)
# min of both is best, go until you cant do the cheaper one then do the more expensive one

debug = False
def solve():
	k, a, b, x, y = map(int, input().split())
	if y <= x:
		t = max((k - b) // y + 1, 0) 
		k = min(k - ((k - b) // y + 1) * y, k)

		t = t + max(0, (k-a) // x + 1)  

	else:
		t = max((k - a) // x + 1, 0)
		
		k = min(k - ((k - a) // x + 1) * x, k)

		t = t + max(0, (k-b) // y + 1)  
	
	print(t)

for i in range(int(input())):
	print(i) if debug else 0
	solve()