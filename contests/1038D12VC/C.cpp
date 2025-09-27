// Problem: C. Manhattan Pairs
// Contest: Codeforces - Order Capital Round 1 (Codeforces Round 1038, Div. 1 + Div. 2)
// URL: https://codeforces.com/contest/2122/problem/C
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-08-15 11:32:32
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

struct byX {
	bool operator()(pair<int, int> a, pair<int, int> b) const {return a.first < b.first;}
};

struct byY {
	bool operator()(pair<int, int> a, pair<int, int> b) const {return a.second < b.second;}
};

int dist(pair<int, int> a, pair<int, int> b) {
	return abs(a.first - b.first) + abs(a.second - b.second);
}

void solve() {
	multiset<pair<int, int>> x;
	multiset<pair<int, int>> y;
	map<pair<int, int>, vector<int>> mp;
	
	int n;
	cin >> n;
	// vector<vector<int>> pts(n, vector<int>(2));
	// vector<vector<int>> c(n, vector<int>(3));
	
	int l, o;
	pair<int, int> t;
	for (int i=0; i<n; i++) {
		cin >> l >> o;
		x.insert({l, o});
		y.insert({o, l});
		mp[{l,o}].push_back(i+1);
	}
	
	pair<int, int> a, b, c, d;
	int mx;

	int p = 0;
	while (x.size()) {
		cout << p << endl;
		a = *x.begin();
		b = *x.end();
		c = *y.begin();
		d = *y.end();
		mx = max({dist(a, b), dist(b, c), dist(c, d), dist(a, d), dist(b, d), dist(a, c)});
		cout << mx << endl;
		if (mx == dist(a, b)) {
			x.erase(a);
			x.erase(b);
			y.erase(a);
			y.erase(b);
			cout << *(mp[a].end()) << " ";
			mp[a].pop_back();
			cout << *(mp[b].end()) << endl;
			mp[b].pop_back();
		} 		
		else if (mx == dist(b, c)) {
			x.erase(b);
			x.erase(c);
			y.erase(c);
			y.erase(b);
			cout << *(mp[b].end()) << " ";
			mp[b].pop_back();
			cout << *(mp[{c.second, c.first}].end()) << endl;
			mp[{c.second, c.first}].pop_back();
		}
		else if (mx == dist(c, d)) {
			x.erase(c);
			x.erase(d);
			y.erase(c);
			y.erase(d);
			cout << *(mp[{c.second, c.first}].end()) << " "; 
			mp[{c.second, c.first}].pop_back();
			cout << *(mp[{d.second, d.first}].end()) << endl;
			mp[{d.second, d.first}].pop_back();
		}
		else if (mx == dist(a, d)) {
			x.erase(a);
			x.erase(d);
			y.erase(a);
			y.erase(d);
			cout << *(mp[a].end()) << " ";
			mp[a].pop_back();
			cout << *(mp[{d.second, d.first}].end()) << endl;
			mp[{d.second, d.first}].pop_back();
		}
		else if (mx == dist(b, d)) {
			x.erase(d);
			x.erase(b);
			y.erase(d);
			y.erase(b);
			cout << *(mp[b].end()) << " ";
			mp[b].pop_back();
			cout << *(mp[{d.second, d.first}].end()) << endl;
			mp[{d.second, d.first}].pop_back();
		}
		else if (mx == dist(a, c)) {
			x.erase(a);
			x.erase(c);
			y.erase(a);
			y.erase(c);
			cout << *(mp[a].end()) << " ";
			mp[a].pop_back();
			cout << *(mp[{c.second, c.first}].end()) << endl;
			mp[{c.second, c.first}].pop_back();
		}
		p += 1;
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