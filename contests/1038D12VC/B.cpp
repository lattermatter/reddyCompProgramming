// Problem: B. Pile Shuffling
// Contest: Codeforces - Order Capital Round 1 (Codeforces Round 1038, Div. 1 + Div. 2)
// URL: https://codeforces.com/contest/2122/problem/B
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-15 11:15:28
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
-
-
-
-
-
-
 */

void solve() {
	int n;
	cin >> n;
	
	int ops = 0;
	
	vector<vector<int>> a(n, vector<int>(4));
	for (int i=0; i<n; i++) {
		for (int j=0; j<4; j++) {
			cin >> a[i][j];
		}
	}
	
	int ones = 0;
	int zeroes = 0;
	for (vector<int> p: a) {
		ones += abs(p[3]-p[1]);
		zeroes += abs(p[2]-p[0]);
		if (p[3] > p[1]) {
			ops += p[0];
		}
	}
	
	ops += floor((ones + zeroes) / 2);
	
	cout << ops << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}