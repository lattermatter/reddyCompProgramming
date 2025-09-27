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
	int c = 1;
	int n;
	cin >> n;
	vector<int> a(n);
	vector<int> b(n);
	for (int i=0; i<n; i++) {cin >> a[i];}
	for (int i=0; i<n; i++) {cin >> b[i];}
	
	for (int i=0; i<n; i++) {
		if (a[i] > b[i]) {
			c += a[i] - b[i];
		}
	}
	cout << c << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}