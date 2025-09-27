import sys
 
debug = False
def solve():
	n = int(input())
	depth = {i: [] for i in range(1, n+1)}
	
	mxd = 0
	for i in range(1, n+1):
		print("?", i, n, " ".join([str(i) for i in range(1, n+1)]))
		sys.stdout.flush()
		d = int(input())
		depth[d].append(i)
		mxd = max(mxd, d)
	
	start = depth[mxd][0]
	path = [start]
	all = {i for i in range(1, n+1)}
	all = all.difference(set(depth[mxd]))
	all.add(start)
	currd = mxd - 1
	while currd > 0:
		level = all.difference(set(depth[currd]))
		k = len(level)
		for i in range(len(depth[currd])):
			level.add(depth[currd][i])
			print("?", start, k+1, " ".join(list(str(x) for x in level)))
			sys.stdout.flush()
			d = int(input())
			level.discard(depth[currd][i])
			if d == mxd:
				all.difference(set(depth[currd]))
				all.add(depth[currd][i])
				path.append(depth[currd][i])
				break
			
		currd -= 1
		
	print("!", mxd, " ".join([str(x) for x in path]))
 
for i in range(int(input())):
	print(i) if debug else 0
	solve()