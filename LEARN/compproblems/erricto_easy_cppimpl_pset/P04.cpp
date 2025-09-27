// Problem: P04. Petya and Strings
// Contest: Codeforces - Day 1 - Strings and Arrays
// URL: https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P04
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-31 11:41:08
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
bool debug = false;

void solve() {
	string a, b;
	cin >> a >> b;
	transform(a.begin(), a.end(), a.begin(),
              ::tolower);
   transform(b.begin(), b.end(), b.begin(),
              ::tolower);
	for (size_t i=0; i<a.size(); i++) {
		if (a[i] > b[i]) {
			cout << 1 << endl;
			return;
		}
		if (a[i] < b[i]) {
			cout << -1 << endl;
			return;
		}
	}
	cout << 0 << endl;
}

int main() {
  FAST int t;
  // cin >> t;
  t = 1;
  while (t--) {
  	if (debug) cout << "case " << t << endl;
    solve();
  }
  return 0;
}