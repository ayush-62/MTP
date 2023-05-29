#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(4);
    for(int i = 1; i < 5; ++i) {
        inputs[i - 1] = stoi(string(av[i]));
    }

    vector<vector<int>> w = {{6, 10, 1, 2}, {8, 7, 4, 5}, {1, 2, 3, 4}, {2, 3, 4, 5}};
    vector<int> l2out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    // vector<vector<int>> w2 = {{8}, {5}};
    // vector<int> l3out(1);
    // for(int i = 0; i < 1; ++i) {
    //     for(int j = 0; j < 2; ++j) {
    //         l3out[i] += (l2out[j] * w2[j][i]);
    //     }
    // }
    // for(auto x: l3out) {
    //     cout << x << " ";
    // }
    // cout << endl;

    // vector<int> w3 = {9, 7, 10, 2, 6, 3, 4, 8, 6, 1};
    // int out = 0;
    // for(int i = 0; i < 10; ++i) {
    //     out += (w3[i] * l3out[i]);
    // }
    // cout << out << endl;
}