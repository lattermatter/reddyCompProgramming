// Problem: P01. Reverse an array
// Contest: Codeforces - Day 1 - Strings and Arrays
// URL: https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P01
// Memory Limit: 256 MB
// Time Limit: 5000 ms
// START: 2025-08-31 11:19:19
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
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	for (int i=0; i<n; i++) cout << a[n-1-i] << " ";
	cout << endl;
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