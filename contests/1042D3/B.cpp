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
	if (n == 2) {
		cout << -1 << " " << 2 << endl;
		return;
	}
	
	for (int i=0; i<n; i++) {
		if (i % 2) {
			if (i == n-1 and n%2 == 0) {
				cout << 2 << " ";
			}
			else {
				cout << 3 << " ";
			}
		} else {
			cout << -1 << " "; 
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