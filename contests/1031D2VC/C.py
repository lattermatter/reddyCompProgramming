# Problem: C. Smilo and Minecraft
# Contest: Codeforces - Codeforces Round 1031 (Div. 2)
# URL: https://codeforces.com/contest/2113/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-27 18:58:49
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	# 20 - give each empty cell a score delta, (gold gained - gold destroyed). pick the best one to start.
	# if do at every iteration and simulate, o(nm ^ (k + 1)) k is power complexity of finding delta.
	# 30 - if k = 1 all gol dcan be collected 
	# 32 - after picking a point to destroy and gold is lost, no further gold needs to be lsot
	# problem reduces to (sum all gold) - (gold lost on first explosion)
	# 34 - gold lost on first explosion can be calculated with prefix sum, number of gold pieces from location ij to kl in pref sum
	n, m, k = map(int, input().split())
	pref = [[0] * (m + 2 * k) for _ in range(n + 2 * k)] # padding for the pref queries
	inp = [[str(x) for x in input().strip()] for _ in range(n)]
	
	for r in range(n):
		for c in range(m):
			pref[r+k][c+k] = 1 if inp[r][c] == "g" else 0

	for r in range(1, n + 2 * k):
		for c in range(1, m + 2 * k):
			pref[r][c] += pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1]

	mn = float("inf") # minimize the amt of gold lost on the first explosion

	for r in range(n):
		for c in range(m):
			if inp[r][c] == ".":
				lost = pref[r+2*k-1][c+2*k-1] - pref[r][c+2*k-1] - pref[r+2*k-1][c] + pref[r][c]
				mn = min(mn, lost)
			
	
	print(pref[-1][-1] - mn)

for i in range(int(input())):
	print(i) if debug else 0
	solve()