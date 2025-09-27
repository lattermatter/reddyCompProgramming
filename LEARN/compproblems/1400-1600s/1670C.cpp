// Problem: C. Where is the Pizza?
// Contest: Codeforces - Codeforces Round 788 (Div. 2)
// URL: https://codeforces.com/problemset/problem/1670/C
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// START: 2025-07-19 14:08:31
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll; // offset 9

int mod = 1e9 + 7;

/*
TIMESTAMP PLANNING
0-start
17-graph insight with chains. make jumps faster?
34-impl start, learning about maps
39-restart, progress lost
73-paused impl had to go
-
-
-
 */

void solve() {
    int n;
    cin >> n;
    
    vector<int> x;
    vector<int> y;
    vector<int> r;
    unordered_map<int, pair<int, int>> u;
    vector<bool> seen(n, false);
    
    int up;
    
    for (int i = 0; i<n; i++) {
    	cin >> up;
    	x.push_back(up);
    }
    for (int i = 0; i<n; i++) {
    	cin >> up;
    	y.push_back(up);
    }
    for (int i = 0; i<n; i++) {
    	cin >> up;
    	r.push_back(up);
    }
    
    
    for (int i=0; i<n; i++) {
    	u[x[i]] = {y[i], r[i]}; // {} creates a pair
    }
    
    int total = 0;
	bool flag = false;
	int perm = 1;
	int curr, next, restrict = 0;
	vector<int> graph;
    
    while (total < n) {
    	flag = false; // so that future graphs dont auto flag
    	// auto& [curr, val] = *u.begin(); // doesnt work for changing curr
    	auto it = u.begin();
    	curr = it->first;
    	graph.push_back(curr);
    	auto val = it->second;
    	// auto [next, restrict] = val; // doesnt work for changing var, local
    	next = val.first;
    	restrict = val.second;
    	
    	if (curr == next) {
    		total += 1;
    		flag = true;
    		seen[curr - 1] = true;
    	}
    	
    	// traverse the linked graph
    	while (not seen[curr - 1]) {
    		// cout << curr << " " << next << " " << restrict << endl;
    		seen[curr - 1] = true;
    		if (restrict != 0) flag = true;
    		curr = next;
	    	graph.push_back(curr);
	    	restrict = u[next].second;
    		next = u[next].first;
    		total += 1;
    	}
    	
    	// remove seen elements so loop can find new beginning element
    	for (int i = graph.size()-1; i > 0; i--) {
    		u.erase(graph[i]);
    		graph.pop_back(); // forgot to remove elements from the graph
    	}
    	
    	perm = (flag) ? perm: perm*2;
    	perm %= mod;
    }
    
    cout << perm << endl;
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