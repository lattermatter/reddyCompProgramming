// Problem: B. Bobritto Bandito
// Contest: Codeforces - Codeforces Round 1017 (Div. 4)
// URL: https://codeforces.com/contest/2094/problem/B
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-17 15:31:48
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
	int n, m, l ,r;
	cin >> n >> m >> l >> r;
	
	if (m <= abs(l)) {
		cout << -1 * m << " " << 0 << endl;
	} else {
		cout << l << " " << m - abs(l) << endl;
	}

}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}