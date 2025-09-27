// Problem: C. Dining Hall
// Contest: Codeforces - Codeforces Round 1012 (Div. 2)
// URL: https://codeforces.com/contest/2090/problem/C
// Memory Limit: 512 MB
// Time Limit: 2000 ms
// START: 2025-09-05 17:54:17
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
	int n;
	cin >> n;
	
	vector<int> q(n);
	for (int i=0; i<n; i++) {cin >> q[i];}
	
	set<vector<int>> tables;
	set<vector<int>> open;
	int dist;
	
	int s = 0;
	int c;
	int cnt = 0;
	while (cnt < n) {
		for (int r=0; r<=s; r++) {
			c = s-r;
			dist = r*3 + c*3;
			tables.insert({dist+2, r*3+1, c*3+1});
			open.insert({dist+2, r*3+1, c*3+1});
			open.insert({dist+3, r*3+1, c*3+2});
			open.insert({dist+3, r*3+2, c*3+1});
			open.insert({dist+6, r*3+2, c*3+2});
			cnt++;
		}
		s++;
	}

	
	// for (auto it=open.begin(); it!=open.end(); it++) {cout << (*it)[0] << " ";} cout << endl;
	
	vector<int> best;
	for (auto e: q) {
		if (e) {
			best = *open.begin();
			open.erase(best);
			tables.erase(best);
			cout << best[1] << " " << best[2] << endl;
		} else {
			best = *tables.begin();
			open.erase(best);
			tables.erase(best);
			cout << best[1] << " " << best[2] << endl;
		}
	}
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
  	if (debug) cout << "case " << t << endl;
    solve();
  }
  return 0;
}