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
	int n;
	cin >> n;
	vector<int> arr(n);
	int zeros = 0;
	int ones = 0;
	
	int tmp = 0;
	int sum = 0;
	
	for (int i=0; i<n; i++) {
		cin >> tmp;
		arr[i] = tmp;
		if (tmp == 0) zeros++;
		sum += tmp;
	}
	
	sum += zeros;
	
	cout << sum << endl;

}

int main() {
  FAST int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}