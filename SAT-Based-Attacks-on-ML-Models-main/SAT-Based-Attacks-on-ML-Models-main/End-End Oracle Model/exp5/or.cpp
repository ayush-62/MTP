#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    // for(int i = 1; i < 3; ++i) {
    //     inputs[i - 1] = stof(string(av[i]));
    // }

    cin >> inputs[0] >> inputs[1];

    vector<vector<int>> w = {{1, 2}, {2, 3}};
    vector<int> hid(2);

    int bias = 7;

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0] + bias;
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    // if(hid[0] < 0) hid[0] = 0;
    // if(hid[1] < 0) hid[1] = 0;

    vector<int> w2 = {7, 8};

    int ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}