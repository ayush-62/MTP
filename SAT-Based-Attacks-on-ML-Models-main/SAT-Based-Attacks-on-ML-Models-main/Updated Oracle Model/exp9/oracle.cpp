#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<int>> w = {{1, 2, 6}, {2, 3, 9}};
    vector<int> hid(3), bias = {12, 4, 8};

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0] + bias[0];
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1] + bias[1];
    hid[2] = inputs[0] * w[0][2] + inputs[1] * w[1][2] + bias[2];

    for(int i = 0; i < 3; ++i) {
        if(hid[i] < 0) {
            hid[i] = 0;
        }
    }

    vector<int> w2 = {7, 8, 9};

    int ans = hid[0] * w2[0] + hid[1] * w2[1] + hid[2] * w2[2];
    cout << hid[0] << " " << hid[1] << " " << hid[2] << " " << ans << endl;
}