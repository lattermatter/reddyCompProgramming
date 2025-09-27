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
	vector<vector<int>> a(n);
	int s, e;
	for (int i=0; i<n-1; i++) {
		cin >> s >> e;
		a[s-1].push_back(e-1);
		a[e-1].push_back(s-1);
	}
	
	int r = 0;
	int m = 0;
	for (int i=0; i<n; i++) {
		if (a[i].size() > m) {
			m = a[i].size();
			r = i;
		}
	}
	
	cout << r;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}