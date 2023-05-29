#include <bits/stdc++.h>
using namespace std;

//2*3*1 + bias

int main(int ac, char* av[]) {
    vector<double> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stod(string(av[i]));
    }
    vector<vector<double>> l1w = {{3.06, 4.3, -1.0}, {0.0, 3.4, -3.0}};
    vector<double> l1b = {-15.09, -2.0, 2.0};

    vector<vector<double>> l2w = {{0.0}, {5.7}, {-2.0}};
    vector<double> l2b = {-19.0};

    vector<double> hiddenValues(3.0, 0.0);
    hiddenValues = l1b;
    for(int i = 0; i < 3; ++i) {
        for(int j = 0; j < 2; ++j) {
            hiddenValues[i] += (inputs[j] * l1w[j][i]);
        }
        if(hiddenValues[i] < 0) {
            hiddenValues[i] = 0;
        }
    }

    double answer = l2b[0];
    for(int i = 0; i < 3; ++i) {
        answer += (hiddenValues[i] * l2w[i][0]);
    }

    cout << answer << endl;
}