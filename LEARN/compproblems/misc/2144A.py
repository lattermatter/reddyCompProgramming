# Problem: A. Cut the Array
# URL: https://codeforces.com/contest/2144/problem/A
# Memory Limit: 512 MB
# Time Limit: 2000 ms
# START: 23:15:13

from bisect import bisect, bisect_left
from math import floor, log, gcd, lcm, sqrt, ceil
from collections import deque
from sys import setrecursionlimit
import sys
import heapq as hq # for priority queue/heap, use hq.heapify(list)
flush = sys.stdout.flush
input = sys.stdin.readline
I = lambda: input().strip()
II = lambda: int(input())
A = lambda: [int(x) for x in input().split()]

debug = False

for i in range(II()):
