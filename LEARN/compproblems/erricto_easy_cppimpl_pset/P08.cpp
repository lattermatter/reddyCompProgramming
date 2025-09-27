// Problem: P08. Cashier
// Contest: Codeforces - Day 1 - Strings and Arrays
// URL: https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P08
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-31 11:54:04
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
	int n, L, a;
	cin >> n >> L >> a;
	vector<int> t(2*n+2);
	
	t[2*n+1] = L;
	t[0] = 0;
	
	for (int i=1; i<2*n + 1; i+=2) {
		cin >> t[i] >> t[i+1];
		t[i+1] += t[i];
	}
	
	int s = 0;
	for (int i=0; i<2*n + 2; i+=2) {
		s += (t[i+1] - t[i]) / a;
	}
	
	cout << s << endl;
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