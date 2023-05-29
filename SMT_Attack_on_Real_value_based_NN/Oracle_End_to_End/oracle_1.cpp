#include <bits/stdc++.h>
using namespace std;

//2*1

int main(int ac, char* av[]) {
    vector<double> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }

    vector<double> w = {1.7, 2.9};
    double ans = w[0] * inputs[0] + w[1] * inputs[1];
    cout << ans << endl; 
}