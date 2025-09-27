// Problem: D. Segments Covering
// Contest: Codeforces - Educational Codeforces Round 181 (Rated for Div. 2)
// URL: https://codeforces.com/contest/2125/problem/D
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// START: 2025-07-22 12:08:40
// 
// Powered by CP Editor (https://cpeditor.org)

#include <bits/stdc++.h>
using namespace std;

#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll; // offset 9

/*
TIMESTAMP PLANNING
20 spent before
0-obs of same interval ranges
17-given complete interval sets, have formula to compute probability
27-created absolute formula, tested for graphs
40-exact graph based formula with fractions, if we can find all possible graphs that work problem ends
45-trying to find a way to determine all graphs. consider sort -> set of starts
57-works. need to use info to construct all graphs.
63-showed coords with same endpts can be compress w/o changing probability
98-created adj list and tried graphs but worst case o(n^2) time. will have to try dp even though dont know it
180-failed, learning algo: dp
330-figured out dp, impled in cpp

 */

long long pow_mod(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;  // Ensure a is within [0, mod-1]
    while (b > 0) {
        if (b % 2 == 1)  // If b is odd
            result = (result * a) % mod;
        a = (a * a) % mod;  // Square the base
        b /= 2;  // Halve the exponent
    }
    return result;
}

int mod = 998244353;

vector<ll> mul(vector<ll> a, vector<ll> b) {
	 return {(a[0] * b[0]) % mod, (a[1] * b[1]) % mod};
}

vector<ll> add(vector<ll> a, vector<ll> b) {
	 return {(a[0] * b[1] + a[1] * b[0]) % mod, (a[1] * b[1]) % mod};
}

void solve() {
	
    int n, m;
    cin >> n >> m;
    
    vector<vector<ll>> arr(n, vector<ll>(4)); // initialize length 4 by n
    for (int i = 0; i < n; i++) {
    	for (int j = 0; j < 4; j++) {
    		cin >> arr[i][j];
    	}
    }
    
    sort(arr.begin(), arr.end());
    
    vector<vector<ll>> dp(m+1, vector<ll>{0, 1}); // dp is n+1 * 2, fraction
    vector<ll> L{1, 1};
    vector<ll> frac(2);
    dp[0] = {1,1};
	
	ll p1, q1, l, r, N, D;
    for (vector<ll> k: arr) {
    	l = k[0]; r = k[1]; p1 = k[2]; q1 = k[3];
    	N = L[0]; D = L[1];
    	
    	dp[r] = add(dp[r], mul({p1, q1 - p1}, dp[l-1]));
    	L = mul({q1 - p1, q1}, {N, D});
    }
    
    vector<ll> f = mul(dp[m], L);
    ll x = f[0];
    ll y = f[1];
    cout << (x * pow_mod(y, mod - 2, mod)) % mod << endl;
}

int main() {
    FAST
	solve();
}