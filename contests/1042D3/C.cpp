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
	int n, k;
	cin >> n >> k;
	multiset<int> a, b;
	int p;
	for (int i=0; i<n; i++) {
		cin >> p; 
		p %= k;
		a.insert(p);
	}
	for (int i=0; i<n; i++) {
		cin >> p; 
		p %= k;
		b.insert(p);
	}
	
	int curr;
	while (size(a)) {
		p = *a.begin();
		a.erase(a.begin());


		if (b.find(p) != b.end()) {

			b.erase(b.find(p));
		} else if (b.find(k-p) != b.end()) {

			b.erase(b.find(k-p));
		} else {
			cout << "NO" << endl;
			return;
		}
	
	}
	if (a == b) {
		cout << "YES" << endl;
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