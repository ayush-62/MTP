#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(10);
    for(int i = 1; i < 11; ++i) {
        if(string(av[i]) == "True") {
            inputs[i - 1] = 1;
        } else {
            inputs[i - 1] = 0;
        }
    }

    vector<vector<int>> w(10, vector<int>(10, 0));
    w = {{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, }, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}};
    vector<int> l2out(10);
    for(int i = 0; i < 10; ++i) {
        for(int j = 0; j < 10; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
    }
    for(auto x: l2out) {
        if(x == 0) cout << "False" << " ";
        else cout << "True" << " ";
    }

    vector<vector<int>> w2 = {{1, 1, 0, 1, 1, 1, 1, 1, 0, 0}, {0, 1, 0, 1, 1, 1, 1, 1, 1, 1, }, {0, 1, 0, 1, 1, 1, 1, 0, 1, 1}, {1, 1, 1, 1, 0, 1, 1, 1, 1, 0}, {1, 1, 1, 0, 1, 1, 1, 1, 1, 0}, {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 0, 1, 1, 1, 0}, {1, 1, 1, 1, 0, 1, 1, 1, 1, 1}, {1, 1, 1, 1, 1, 1, 1, 1, 0, 1}, {0, 1, 1, 1, 0, 0, 1, 1, 1, 1}};
    vector<int> l3out(10);
    for(int i = 0; i < 10; ++i) {
        for(int j = 0; j < 10; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
    }
    for(auto x: l3out) {
        if(x == 0) cout << "False" << " ";
        else cout << "True" << " ";
    }

    vector<int> w3 = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    int out = 0;
    for(int i = 0; i < 10; ++i) {
        out += (w3[i] * l3out[i]);
    }
    if(out) {
        cout << "True" << " ";
    } else {
        cout << "False" << " ";
    }
    cout << endl;
}