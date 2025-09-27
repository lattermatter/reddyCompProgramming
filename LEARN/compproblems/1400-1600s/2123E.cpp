// Problem: E. MEX Count
// Contest: Codeforces - Codeforces Round 1034 (Div. 3)
// URL: https://codeforces.com/problemset/problem/2123/E
// Memory Limit: 256 MB
// Time Limit: 3000 ms
// START: 2025-07-20 14:06:05
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll; // offset 9

/*
TIMESTAMP PLANNING
0-start
1-read
3-removal: 0, 1, 2.. to change mex
4-if arr has no 0 mex = 0 for all k
6-try casework on mex
15-proving mex lemma off observation that mex decreases after a point
23-proved mex lemma
29-leftovers location doesnt matter after leftovers < k
52-proving final map algo correctness
56-relatively confindent. will need to look at proof if failure. start impl
60-sort(v.begin(), v.end())
100-solved
 */

void solve() {
    unordered_map<int, int> atK;
    int n;
    cin >> n;
    vector<int> nums(n), numOfNums;
    
    for (int i=0;i<n;i++) {cin >> nums[i];}
    
	sort(nums.begin(), nums.end());
	
	// case of 0
	if (nums[0] != 0 or nums[nums.size()-1] == 0) {
		for (int i =0; i <= n; i++) {cout << 1 << " ";} cout << endl; return;
	} 
	
	// get counts of numbers
	int cnt = 0;
	int leftover = 0;
	
	nums.push_back(-1); // easier stopping 
	
	for (int i = 0; i < n; i++) {
		cnt++;
		if (nums[i] != nums[i+1]) {
			numOfNums.push_back(cnt);
			cnt = 0;
		}
		
		if (nums[i] + 1 < nums[i+1]) {
			leftover = n-i-1;
			break;
		}
		
		if (nums[i+1] == -1) {break;}
	}
	
	// find num leftover
	for (int i: numOfNums) {
		// cout << i << " ";
		if (i > 1){
			leftover += i-1;
		}
	}
	// cout << endl << leftover << endl;
	
	// create pref hash
	sort(numOfNums.begin(), numOfNums.end());
	numOfNums.push_back(-1);
	cnt = 0;
	for (int i = 0; i < numOfNums.size()-1; i++) { // account for added -1
		if (numOfNums[i] != numOfNums[i+1]) {
			atK[numOfNums[i]] = i+1;
		}
		
		if (numOfNums[i+1] == -1) {
			break;
		}
	}
	
	
	// final calculation
	int m = 0;
	for (int k = 0; k <= n; k++) {
		if (k==0) {cout << 1 << " "; continue;}
		if (k <= leftover) {
			if (atK.count(k)) m = k;
			cout << atK[m] + 1 << " ";
		}
		else cout << n-k+1 << " ";
	}
	cout << endl;
	
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