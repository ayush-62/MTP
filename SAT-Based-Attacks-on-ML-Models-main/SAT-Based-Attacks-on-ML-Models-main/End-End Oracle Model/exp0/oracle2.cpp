#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
    vector<vector<int>> l1w = {{3, 4, -1}, {0, 3, -3}};
    vector<int> l1b = {-15, -2, 2};

    vector<vector<int>> l2w = {{0}, {5}, {-2}};
    vector<int> l2b = {-19};

    vector<int> hiddenValues(3, 0);
    hiddenValues = l1b;
    for(int i = 0; i < 3; ++i) {
        for(int j = 0; j < 2; ++j) {
            hiddenValues[i] += (inputs[j] * l1w[j][i]);
        }
        if(hiddenValues[i] < 0) {
            hiddenValues[i] = 0;
        }
    }

    int answer = l2b[0];
    for(int i = 0; i < 3; ++i) {
        answer += (hiddenValues[i] * l2w[i][0]);
    }

    cout << answer << endl;
}