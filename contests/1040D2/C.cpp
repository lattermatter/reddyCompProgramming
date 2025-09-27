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
	vector<pair<int, int>> arr(n);
	map<pair<int, int>, int> indexes;
	map<int, set<int>> adj;
	vector<bool> seen(n, false);
	
	for (int i = 0; i<n; i++) {
		cin >> arr[i].first >> arr[i].second;
		indexes[arr[i]] = i+1;
		adj[arr[i].first].insert(arr[i].second);
	}
	
	int next;
	for (int i = 0; i<n; i++) {
		if (seen[i]) continue;
		while (adj[arr[i].first].size()) {
			next = *adj[arr[i].first].begin();
			cout << next << " ";
			adj[arr[i].first].erase(next);
		}
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