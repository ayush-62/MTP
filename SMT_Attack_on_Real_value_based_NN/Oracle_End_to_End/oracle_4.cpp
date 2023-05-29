#include <bits/stdc++.h>
using namespace std;
//2*2*1 + bias
int main(int ac, char* av[]) {
    vector<double> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }

    vector<vector<double>> w = {{1.7, 2.0}, {2.5, 3.0}};
    vector<double> hid(2);

    double bias = 7;

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0] + bias;
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    if(hid[0] < 0) hid[0] = 0;
    if(hid[1] < 0) hid[1] = 0;

    vector<double> w2 = {7.6, 8.0};

    double ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}