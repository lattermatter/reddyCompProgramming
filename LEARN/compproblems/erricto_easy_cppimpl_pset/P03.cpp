// Problem: P03. Way Too Long Words
// Contest: Codeforces - Day 1 - Strings and Arrays
// URL: https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P03
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-08-31 11:29:27
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
bool debug = true;

void solve() {
	string s;
	getline(cin, s);	
	
	
	size_t n = s.size();
	
	if (n <= 10) {cout << s << endl; return;}
	
	cout << s[0] << n-2 << s[n-1] << endl;
}

int main() {
  FAST int t;
  cin >> t;
  	string s;
	getline(cin, s); // clear
  
  while (t--) {
  	if (debug) cout << "case " << t << endl;
    solve();
  }
  return 0;
}