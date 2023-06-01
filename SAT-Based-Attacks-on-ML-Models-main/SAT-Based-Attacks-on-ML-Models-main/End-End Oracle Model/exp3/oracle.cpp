#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<int>> w = {{1, 2}, {2, 3}};
    vector<int> hid(2);
    vector<int> inputValues(2);
    inputValues[0] = inputs[0] - 3;
    inputValues[1] = inputs[1] - 3;
    hid[0] = inputValues[0] * w[0][0] + inputValues[1] * w[1][0];
    hid[1] = inputValues[0] * w[0][1] + inputValues[1] * w[1][1];

    vector<int> w2 = {7, 8};

    int ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}