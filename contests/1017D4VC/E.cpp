// Problem: E. Boneca Ambalabu
// Contest: Codeforces - Codeforces Round 1017 (Div. 4)
// URL: https://codeforces.com/contest/2094/problem/E
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-17 16:43:22
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
	vector<int> arr(n);
	for (int i=0; i<n; i++) {cin >> arr[i]; }
	vector<int> mask(30, 0);
	
	int m = 1;
	for (int l=0; l<30; l++) {
		for (int i=0; i<n; i++) {
			if ((arr[i] ^ m) != arr[i] - m) continue;
			mask[l]++;
		}
		m = m << 1;
	}
	
	ll final = 0;
	ll curr;
	for (int i=0; i<n; i++) {
		curr = 0;
		int m = 1;
		for (int l=0; l<30; l++) {
			if ((arr[i] ^ m) != arr[i] - m) { // if bit is 0, use 1 bits
				curr += pow(2, l) * mask[l];
			} else if ((arr[i] ^ m) == arr[i] - m) {
				curr += pow(2, l) * (n - mask[l]);
			}// it bit is 1, use 0 bits
			m = m << 1;
		}
		final = max(curr, final);
	}
	
	cout << final << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}