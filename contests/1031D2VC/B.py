# Problem: B. Good Start
# Contest: Codeforces - Codeforces Round 1031 (Div. 2)
# URL: https://codeforces.com/contest/2113/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# START: 2025-08-27 18:32:53
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	# the width and height must contain 
	
	# if they touch its fine
	w, h, a, b = map(int, input().split())
	xa, ya, xb, yb = map(int, input().split())
	
	if (abs(xa - xb) % a == 0 or abs(ya - yb) % b == 0):
		if xa != xb and ya != yb:
			print("Yes")
		elif xa == xb and abs(ya - yb) % b == 0:
			print("Yes")
		elif ya == yb and abs(xa - xb) % a == 0:
			print("Yes")
		else:
			print("No")
	else:
		print("No")
	
	

for i in range(int(input())):
	print(i) if debug else 0
	solve()