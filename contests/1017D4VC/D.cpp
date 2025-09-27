// Problem: D. Tung Tung Sahur
// Contest: Codeforces - Codeforces Round 1017 (Div. 4)
// URL: https://codeforces.com/contest/2094/problem/D
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-17 15:59:50
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
	string a, b;
	 
	cin >> a >> b;
	a += "S"; b += "S"; // different string for stopping
	
	vector<int> x, y;
	
	int c = 0;
	for (size_t i = 1; i<a.length(); i++) {
		c++;
		if (a[i] != a[i-1]) {
			x.push_back(c);
			c = 0;
		}
	}
	
	for (size_t i = 1; i<b.length(); i++) {
		c++;
		if (b[i] != b[i-1]) {
			y.push_back(c);
			c = 0;
		}
	}
	
	if (a[0] != b[0] or x.size() != y.size()) {
		cout << "NO" << endl;
		return;
	}
	
	for (int i=0; i<x.size(); i++) {
		if (x[i] > y[i] or x[i]*2 < y[i]) {
			cout << "NO" << endl;
			return;
		}
	}
	
	cout << "YES" << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}