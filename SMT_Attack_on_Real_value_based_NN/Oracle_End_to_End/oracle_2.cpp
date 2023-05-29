#include <bits/stdc++.h>
using namespace std;

//4*1

int main(int ac, char* av[]) {
    vector<double> inputs(4);
    for(int i = 1; i < 5; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }

    vector<double> w = {1.5, 2.0, 19.2, 7.0};
    double ans = 0;
    for(int i = 0; i < 4; ++i) {
        ans += (inputs[i] * w[i]);
    }
    cout << ans << endl; 
}