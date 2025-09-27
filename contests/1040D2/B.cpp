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
	int zero = 0; int one = 0; int two = 0;
	int n, s;
	cin >> n >> s;
	int tmp;
	int sum = 0;
	vector<int> arr(n);
	for (int i=0; i<n; i++) {
		cin >> tmp;
		arr[i] = tmp;
		if (tmp == 0) zero++;
		if (tmp == 1) one++;
		if (tmp == 2) two++;
		sum += tmp;
	}
	
	if (not (s < sum or s == sum + 1)) {
		cout << -1 << endl; 
		return;
	}
	
	for (int i=0; i<zero; i++) {
		cout << 0 << " ";
	}
	for (int i=0; i<two; i++) {
		cout << 2 << " ";
	}
	for (int i=0; i<one; i++) {
		cout << 1 << " ";
	}
	cout << endl;
}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}