#include <bits/stdc++.h>
using namespace std;
//2*2*1
int main(int ac, char* av[]) {
    vector<double> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }

    vector<vector<double>> w = {{1.0, 2.6}, {2.8, 3.0}};
    vector<double> hid(2);

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0];
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    vector<double> w2 = {7, 8};

    double ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}