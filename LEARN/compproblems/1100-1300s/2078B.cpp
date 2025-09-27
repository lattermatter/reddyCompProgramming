// Problem: B. Vicious Labyrinth
// Contest: Codeforces - Codeforces Round 1008 (Div. 2)
// URL: https://codeforces.com/problemset/problem/2078/B?mobile=false
// Memory Limit: 256 MB
// Time Limit: 1500 ms
// START: 2025-08-04 22:21:27
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
	int n, k;
	cin >> n >> k;
	
	if (k % 2 == 0) {
		for (int i = 0; i < n; i++) {
			if (i != n-2) cout << n-1 << " ";
			else cout << n << " ";
		}
	} else {
		for (int i = 0; i < n; i++) {
			if (i != n-1) cout << n << " ";
			else cout << n-1 << " ";
		}
	}
	cout << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}