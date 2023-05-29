#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(4);
    for(int i = 1; i < 5; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<int> w = {1, 2, 19, 7};
    int ans = 0;
    for(int i = 0; i < 4; ++i) {
        ans += (inputs[i] * w[i]);
    }
    cout << ans << endl; 
}