// Problem: C. Cool Partition
// Contest: Codeforces - Codeforces Round 1029 (Div. 3)
// URL: https://codeforces.com/problemset/problem/2117/C
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-29 13:41:12
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
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) {cin >> a[i];}
	vector<int> c(n+1);
	for (int i=0; i<n; i++) {
		c[a[i]]++;
	}
	
	int index = 0;
	int partition = 1;
	set<int> curr;
	set<int> next;
	set<int> inc;
	curr.insert(a[index]);
	
	while (index < n) {
		if (index == 0) index++;
		
		while (inc != curr) {
			if (index >= n) break;
			next.insert(a[index]);
			if (curr.find(a[index]) != curr.end()) {
				inc.insert(a[index]);
			}
			if (debug) {for (auto it = inc.begin(); it != inc.end(); it++) {cout << *it << " " << index << endl;} for (auto it = next.begin(); it != next.end(); it++) {cout << *it << "N" << index << endl;}
			for (auto it = curr.begin(); it != curr.end(); it++) {cout << *it << "C" << index << endl;}}
			index++;
			if (inc == curr) partition++;
		}
		
		curr = next;
		next.clear();
		inc.clear();
	}
	
	cout << partition << endl;
	
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}