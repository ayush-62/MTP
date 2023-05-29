#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> inputs(2);
    // for(int i = 1; i < 3; ++i) {
    //     inputs[i - 1] = stof(string(av[i]));
    // }
    cin >> inputs[0] >> inputs[1];
    vector<vector<int>> w = {{7, 2}, {14, 3}};
    vector<int> hid(2);

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0];
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    if(hid[0] < 0) hid[0] = 0;
    if(hid[1] < 0) hid[1] = 0;

    vector<int> w2 = {1, 8};

    int ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}

/*

7 2
14 3

1 8

*/