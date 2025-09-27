// Problem: E. Sponsor of Your Problems
// Contest: Codeforces - Codeforces Round 1032 (Div. 3)
// URL: https://codeforces.com/problemset/problem/2121/E
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-07-19 11:50:59
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll; // offset 9

int getDigit(int num, int place) {
	int sub = pow(10, place - 1);
	int act = num % (sub * 10);
	int c = -1;
	while (act >= 0) {
		act -= sub;
		c += 1;
	}
	return c;
}

void solve() {
    int l, r;
    cin >> l >> r;
	int ld, rd;
	int thresh = r-l;
	bool flag = false;
	bool firstnonzero = false;
	int cnt = 0;
	
	for (int i = 9; i > 0; i--) {
		ld = getDigit(l, i);
		rd = getDigit(r, i);
		
		// cout << ld << " " << rd << endl;
		
		if (not flag) {
			flag = (ld != rd);
			if (ld == rd and ld != 0) {firstnonzero = true;}
			if (firstnonzero and ld == rd) {cnt += 2;}
		}
		
		if (flag) {
			if (thresh >= pow(10, i)) {
				break;
			}
			
			if (rd > ld) {
				if (rd - ld >= 2) {
					break;
				}
				if (rd - ld == 1) {
					cnt++;
				}
			}
			
			if (rd < ld) {
				if (rd + 10 - ld >= 2) {
					break;
				}
				if (rd + 10 - ld == 1) {
					cnt++;
				}
			}
		}
		
	}
	
	cout << cnt << endl;
    
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