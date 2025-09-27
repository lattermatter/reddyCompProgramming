// Problem: A. Trippi Troppi
// Contest: Codeforces - Codeforces Round 1017 (Div. 4)
// URL: https://codeforces.com/contest/2094/problem/A
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-17 14:56:58
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

	string s;
	getline(cin, s);
	
	cout << s[0];
	for (size_t i=0; i<s.length(); i++) {
		if (s[i] == ' ') cout << s[i+1];
		if (i==s.length()-1) cout << endl;
	}


}

int main() {
  FAST int t;
  string a;
  getline(cin, a);
  t = stoi(a);
  while (t--) {
    solve();
  }
  return 0;
}