// Problem: C. Brr Brrr Patapim
// Contest: Codeforces - Codeforces Round 1017 (Div. 4)
// URL: https://codeforces.com/contest/2094/problem/C
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-17 15:41:55
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
	int n; cin >> n;
	int arr[2 * n];
	int nxt;
	bool down = false;
	unordered_set<int> s;
	for (int i=1; i<2*n+1; i++) {
		s.insert(i);
	}
	
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			cin >> nxt;
			if (down and j!=n-1) {
				continue;
			}
			arr[i+j+1] = nxt;
			s.erase(nxt);
			if (j==n-1) down = true;
		}
	}
	
	arr[0] = *s.begin();
	for (auto i: arr) {cout << i << " ";} cout << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}