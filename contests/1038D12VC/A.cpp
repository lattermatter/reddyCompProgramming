// Problem: A. Greedy Grid
// Contest: Codeforces - Order Capital Round 1 (Codeforces Round 1038, Div. 1 + Div. 2)
// URL: https://codeforces.com/contest/2122/problem/A
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-15 10:31:22
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
	int n, m;
	cin >> n >> m;
	if (n == 1 or m == 1 or (n == 2 and m == 2)) cout << "NO";
	else cout << "YES";
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