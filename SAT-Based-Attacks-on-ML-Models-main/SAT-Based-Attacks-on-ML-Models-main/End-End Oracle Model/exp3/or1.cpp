#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> inputs(2);
    cin >> inputs[0] >> inputs[1];

    vector<vector<int>> w = {{23, 0}, {-1, -1}};
    vector<int> hid(2);

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0];
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    vector<int> w2 = {1, -39};

    int ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}
