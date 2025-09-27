// Problem: D. Stay or Mirror
// Contest: Codeforces - Codeforces Round 1040 (Div. 2)
// URL: https://codeforces.com/contest/2130/problem/D
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-01 14:46:55
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST                   \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);
typedef long long ll;  // offset 9

/*
TIMESTAMP PLANNING
0-start
5-observations algebra
14-working with perms
64-trying impl greedy on fixes vs changes, could not prove optimality           
80-impled, fast
-
-
 */

void solve() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {cin >> a[i];}
	
	int curr;
	int change;
	for (int j = 0; j < n; j++) {
		curr = 0; change = 0;
		for (int i = 0; i < n; i++) {
			if (i == j) continue;
			if (a[i] < a[j] and i < j) curr++;
			if (a[j] < a[i] and j < i) curr++;
			if (a[i] < 2*n - a[j] and i < j) change++;
			if (2*n - a[j] < a[i] and j < i) change++;
		}
		if (change > curr) a[j] = 2 * n - a[j];
	}

	int inv = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			if (a[j] < a[i]) inv++;
		}
	}
	
	cout << inv << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}