#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<int> w = {8667, 7893};
    int ans = w[0] * inputs[0] + w[1] * inputs[1];
    cout << ans << endl; 
}