# Problem: G. Chimpanzini Bananini
# Contest: Codeforces - Codeforces Round 1017 (Div. 4)
# URL: https://codeforces.com/contest/2094/problem/G
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-19 10:03:48
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False

from collections import deque

def solve():
	q = int(input())
	m = 0
	s = 0
	arr = deque()
	summing = 0
	dir = 1
			
	for _ in range(q):
		query = list(map(int, input().split()))
		if query[0] == 1:
			if dir == 1:
				k = arr.pop()
				arr.appendleft(k)
			if dir == -1:
				k = arr.popleft()
				arr.append(k)
			s = s + summing - (m) * k
			
		elif query[0] == 2:
			dir *= -1
			s = summing * (m+1) - s
			
		elif query[0] == 3:
			summing += query[1]
			m += 1
			if dir == 1:
				arr.append(query[1])
			if dir == -1:
				arr.appendleft(query[1])
			s = s + query[1] * (m)
			
		print(s)
			

for i in range(int(input())):
	print(i) if debug else 0
	solve()