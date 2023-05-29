#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(5);
    for(int i = 1; i < 6; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<int>> w = {{-6, 10, 5, 2, 1}, {8, -7, 1, -1, 2}, {4, 7, -3, -2, 4}, {8, -7, 1, -1, 2}, {4, 7, -3, -2, 4}};
    vector<int> l2out(5);
    for(int i = 0; i < 5; ++i) {
        for(int j = 0; j < 5; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    // for(auto x: l2out) {
    //     cout << x << " ";
    // }
    // cout << l2out[4] << endl;

    vector<vector<int>> w2 = {{-3, 4, 5, 9, 1}, {6, -7, 1, 4, 2}, {3, -3, -3, -3, 6}, {3, -3, -3, -3, 7}, {8, -7, 1, -1, 2}};
    vector<int> l3out(5);
    for(int i = 0; i < 5; ++i) {
        for(int j = 0; j < 5; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
        if(l3out[i] < 0) l3out[i] = 0;
    }
    // for(auto x: l3out) {
    //     cout << x << " ";
    // }
    cout << l3out[0] << endl;

    // vector<int> w3 = {2, -1, 1, 7};
    // int out = 0;
    // for(int i = 0; i < 4; ++i) {
    //     out += (w3[i] * l3out[i]);
    // }
    // cout << out << endl;
}