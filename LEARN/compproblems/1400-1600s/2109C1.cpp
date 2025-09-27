// Problem: C1. Hacking Numbers (Easy Version)
// Contest: Codeforces - Codeforces Round 1025 (Div. 2)
// URL: https://codeforces.com/contest/2109/problem/C1
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-07-21 14:40:00
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll; // offset 9

/*
TIMESTAMP PLANNING
0-start
5-read
6-search for an invariant
8-x >= 1
25-algo found, reduce as fast as possible
53-had right algo but thought it was 10*18 instead of 10**9 and wasted 15 min
58-solved
 */

void solve() {
	int n, waste;
	cin >> n;
	cout << "digit" << endl;
	cout.flush();
	cin >> waste;
	cout << "digit" << endl;
	cin >> waste;
	cout.flush();
	cout << "add -8" << endl;
	cin >> waste;
	cout.flush();
	cout << "add -4" << endl;
	cin >> waste;
	cout.flush();
	cout << "add -2" << endl;
	cin >> waste;
	cout.flush();
	cout << "add -1" << endl;
	cin >> waste;
	cout.flush();
	cout << "add " << n-1 << endl;
	cin >> waste;
	cout.flush();
	cout << "!" << endl;
	cout.flush();	
	cin >> waste;
}

int main() {
    FAST
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}