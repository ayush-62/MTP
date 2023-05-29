#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<int>> w = {{-6, 10}, {8, -7}};
    vector<int> l2out(2);
    for(int i = 0; i < 2; ++i) {
        for(int j = 0; j < 2; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    vector<vector<int>> w2 = {{-3}, {6}};
    vector<int> l3out(1);
    for(int i = 0; i < 1; ++i) {
        for(int j = 0; j < 2; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
        if(l3out[i] < 0) l3out[i] = 0;
    }
    for(auto x: l3out) {
        cout << x << " ";
    }
}