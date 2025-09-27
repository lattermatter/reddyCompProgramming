// Problem: D. 1709
// Contest: Codeforces - Codeforces Round 1032 (Div. 3)
// URL: https://codeforces.com/problemset/problem/2121/D
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-07-30 14:53:38
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
1-read problem
20-valid sol, pain to impl
63-almost completed first array, off by one errors
76-operation logic
92-impled second array swaps. likely that submission fails.
108-still debugging impl. relize it wouldve been much better if used pointer function to perform repeated commands.
120-failed on test case 13 because too large. didnt spend NEARLY enough time on algo. do it even for impl problems, plan out the structure.
 */

void solve() {
	int n;
	cin >> n;
	
	vector<int> a(n);
	vector<int> b(n);
	vector<pair<int, int>> all;
	
	for (int i=0; i<n; i++) {cin >> a[i];}
	for (int i=0; i<n; i++) {cin >> b[i];}	
	
	int k = 1;
	bool inA = false;
	int index;
	int swap;
	int ops = 0;
	
	while (k < n + 1) {
		// find k
		for (int i=0; i<n; i++) {
			if (a[i] == k) inA = true;
			if (a[i] == k or b[i] == k) index = i;
		}
		
		if (inA and index != k-1) {
			swap = b[index];
			b[index] = a[index];
			a[index] = swap;
			all.push_back({3, index + 1});
			ops += 1;
		}
		
		if (inA and index == k-1) {
			k++;
			inA = false;
			continue;
		}
		
		if (index < k-1) {
			for (int i=index; i<k-1; i++) {
				swap = b[i+1];
				b[i+1] = b[i];
				b[i] = swap;
				ops++;
				all.push_back({2, i + 1});
			}
		} else if (index > k-1) {
			for (int i=index; i>k-1; i--) {
				swap = b[i-1];
				b[i-1] = b[i];
				b[i] = swap;
				ops++;
				all.push_back({2, i}); // accounts for 0 index
			}
		}
		swap = b[k-1];
		b[k-1] = a[k-1];
		a[k-1] = swap;
		all.push_back({3, k});
		ops += 1;
		
		k++;
		inA = false;
		index = 0;
		swap = 0;
	}
	cout << ops << endl;

	while (k < 2 * n + 1) {
		for (int i = 0; i < n; i++) {
			if (b[i] == k) index = i;
		}
		
		if (index < k-1-n) {
			for (int i=index; i<k-1-n; i++) {
				swap = b[i+1];
				b[i+1] = b[i];
				b[i] = swap;
				ops++;
				all.push_back({2, i+2});
			}
		} else if (index > k-1-n) {
			for (int i=index; i>k-1-n; i--) {
				swap = b[i-1];
				b[i-1] = b[i];
				b[i] = swap;
				ops++;
				all.push_back({2, i}); // accounts for 0 index
			}
		}
		k++;
		index = 0;
		
	}
	cout << ops << endl;
	pair<int, int> p;
	for (int i = 0; i < ops; i++) {
		p = all[i];
		cout << p.first << " " << p.second << endl;
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