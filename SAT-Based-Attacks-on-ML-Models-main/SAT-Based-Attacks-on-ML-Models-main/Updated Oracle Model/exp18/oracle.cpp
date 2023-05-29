#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(5);
    for(int i = 1; i < 6; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<int>> w = {{6, 10, 6, 2, 1}, {8, 7, 5, 3, 7}, {10, 8, 5, 0, 4}, {10, 7, 10, 3, 7}, {7, 10, 4, 1, 0}};
    vector<int> l2out(5);
    for(int i = 0; i < 5; ++i) {
        for(int j = 0; j < 5; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    vector<vector<int>> w2 = {{8, 3, 8, 7, 5}, {5, 1, 10, 7, 8}, {4, 2, 4, 3, 10}, {10, 5, 0, 5, 10}, {10, 5, 6, 9, 10}};
    vector<int> l3out(5);
    for(int i = 0; i < 5; ++i) {
        for(int j = 0; j < 5; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
    }
    for(auto x: l3out) {
        cout << x << " ";
    }

    vector<int> w3 = {9, 7, 10, 2, 6};
    int out = 0;
    for(int i = 0; i < 5; ++i) {
        out += (w3[i] * l3out[i]);
    }
    cout << out << endl;
}