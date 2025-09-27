# Problem: C2. The Cunning Seller (hard version)
# Contest: Codeforces - Codeforces Round 1043 (Div. 3)
# URL: https://codeforces.com/contest/2132/problem/C2
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# START: 2025-08-21 08:26:51
# 
# Powered by CP Editor (https://cpeditor.org)

debug = False
def solve():
	n, k = map(int, input().split())
	b3 = []
	sub = 1
	mod = 3
	cnt = 0
	while n > 0:
		cnt = 0
		while n % mod != 0:
			cnt += 1
			n -= sub
		b3.append(cnt)
		sub *= 3
		mod *= 3
		
	b3.reverse()
	
	print(b3) if debug else 0
	
	if sum(b3) > k:
		print(-1)
		return
	
	total = 0
	for i in range(len(b3)):
		total += int(b3[i] * (3 ** (len(b3)-i-1+1) + (len(b3)-i-1) * (3 ** (len(b3)-i-1-1))))
		
	print(total, "total") if debug else 0
	
	deals = []
	pref = [0]
	cost = []
	delta = []
	acc = 0
	collect = 0
	
	for i in range(len(b3)-1, -1, -1):
		pref.append(pref[-1] + b3[i])
	
	pref.reverse()
	
	first = True
	
	for i in range(len(b3)):
		acc = acc or b3[i]
		if not acc:
			deals.append(0)
			delta.append(0)
			cost.append(0)
			continue
		elif i == 0:
			deals.append(b3[i])
			delta.append(sum(b3))
			cost.append(0)
			continue
		
		
		collect = deals[i-1] * 3 + b3[i]
		deals.append(collect)
		delta.append(collect + pref[i+1])
		cost.append(deals[i-1] * 3 ** (len(b3)-i-1))
	print(deals, cost) if debug else 0
	print(delta) if debug else 0
	
	d = 0
	for i in range(len(delta)):
		if delta[i] > k:
			break
		d = i
	print(d, "deals", k) if debug else 0
	
	save = 0
	for i in range(d+1):
		save += cost[i]
	
	m = delta[d]
	print(m, 'start deal') if debug else 0

	# while m <= k and d != len(deals) - 1:
		# if m+2 <= k:
			# save += 3 ** (len(b3)-d-1-1)
			# m += 2
		# else:
			# break
		
	if m <= k and d != len(deals) - 1:
		save += (k-m)//2 * 3 ** (len(b3)-d-1-1)
	
	print(save, "S") if debug else 0
	print(total-save)

for i in range(int(input())):
	print(i) if debug else 0
	solve()