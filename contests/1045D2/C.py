# Problem: C. Even Larger
# Contest: Codeforces - Codeforces Round 1045 (Div. 2)
# URL: https://codeforces.com/contest/2134/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-26 08:05:42
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n = int(input())
	a = [int(x) for x in input().split()]
	
	if n == 2:
		print(max(a[0] - a[1], 0))
		return
	
	f = 0
	if n % 2:
		f = n-3
	else:
		f = n-2
	# ends
	o = 0
	if a[1] < a[0]:
		o += a[0] - a[1]
		a[0] -= a[0] - a[1]
	if a[n-2] < a[n-1] and n % 2:
		o += a[n-1] - a[n-2]
		a[n-1] -= a[n-1] - a[n-2]
		
	for i in range(2, f+1, 2):
		c = a[i]
		b = a[i-1]
		d = a[i+1]

		if c <= min(b, d):
			continue

		o += c - min(b,d)
		a[i] -= c - min(b,d)
	
	left = []
	f -= 2 if n % 2 == 0 else 0

	for i in range(0, f+1, 2):
		left.append(min(a[i+1] - (a[i] + a[i+2]), 0))
	
	m = len(left)
	
	if m % 2:
		a1 = abs(left[-1])
		for i in range(0, len(left)-1, 2):
			a1 += abs(min(left[i], left[i+1]))
		
		a2 = abs(left[0])
		for i in range(1, len(left), 2):
			a2 += abs(min(left[i], left[i+1]))
			
		o += min(a1, a2)
	
	else:
		a1 = abs(left[-1]) + abs(left[0])
		for i in range(1, len(left)-2, 2):
			a1 += abs(min(left[i], left[i+1]))
		
		a2 = 0
		for i in range(0, len(left), 2):
			a2 += abs(min(left[i], left[i+1]))
			
		o += min(a1, a2)
		

	print(o)



for i in range(int(input())):
	print(i) if debug else 0
	solve()