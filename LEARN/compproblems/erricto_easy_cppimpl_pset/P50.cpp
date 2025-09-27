// Problem: P50. Jzzhu and Sequences
// Contest: Codeforces - Day 5 - Math II
// URL: https://codeforces.com/group/yg7WhsFsAp/contest/355498/problem/P50
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-31 12:24:14
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

int mod = 1e9 + 7;

void solve() {
	int x, y;
	cin >> x >> y;
	int n;
	cin >> n;
	n = n % 6;
	int mods[6] = {0};
	
	mods[0] = x - y;
	mods[1] = x;

	for (int i=2; i<6; i++) {
		mods[i] = mods[i-1] - mods[i-2];

	}
	
	if (mods[n] < 0) mods[n] += mod;
	cout << mods[n] << endl;
}

int main() {
  FAST int t;
  t = 1;
  while (t--) {
  	if (debug) cout << "case " << t << endl;
    solve();
  }
  return 0;
}