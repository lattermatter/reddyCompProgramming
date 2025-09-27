# Problem: B. Fibonacci Cubes
# Contest: Codeforces - Educational Codeforces Round 179 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/2111/B
# Memory Limit: 512 MB
# Time Limit: 2000 ms
# START: 2025-08-29 14:44:38
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, m = map(int, input().split())
	boxes = [list(map(int, input().split())) for _ in range(m)]
	fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 79][:n]
	
	work = []
	
	for box in boxes:
		if max(box) >= fib[-1] + fib[-2] and min(box) >= fib[-1]:
			work.append(1)
		else:
			work.append(0)
	
	print("".join([str(x) for x in work]))

for i in range(int(input())):
	print("testcase", i+1) if debug else 0
	solve()