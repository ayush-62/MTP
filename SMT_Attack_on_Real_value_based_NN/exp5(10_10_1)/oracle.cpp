#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<double> inputs(10);
    for(int i = 1; i < 11; ++i) {
        // string numerator , denominator = "1" , s;
        // int flag = 0;
        // s = av[i];
        // for(int i = 0 ; i < s.size() ; i++)
        // {
        //     if(s[i] == '/')
        //     {
        //         flag = 1;
        //         i++;
        //         denominator.pop_back();
        //     }
        //     if(flag == 0)
        //     numerator.push_back(s[i]);
        //     else
        //     denominator.push_back(s[i]);
        // }
        inputs[i - 1] = stod(av[i]);
    }

    vector<vector<double>> w = {{6, 10, 6, 2, 1, 4, 0, 6, 3, 1}, {8, 7, 5, 3, 7, 4, 9, 10, 2, 0}, {10, 8, 5, 0, 4, 6, 0, 10, 3, 10}, {10, 7, 10, 3, 7, 9, 7, 8, 2, 10}, {7, 10, 4, 1, 0, 10, 4, 9, 7, 6}, {8, 6, 2, 2, 7, 6, 6, 5, 5, 7}, {4, 4, 4, 3, 6, 9, 10, 2, 4, 1}, {0, 10, 9, 4, 0, 10, 1, 2, 6, 9}, {7, 1, 4, 9, 3, 9, 2, 10, 3, 7}, {6, 8, 9, 8, 9, 4, 5, 9, 5, 9}};
    vector<double> l2out(10);
    for(int i = 0; i < 10; ++i) {
        for(int j = 0; j < 10; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    cout << l2out[2] << endl;

    // vector<vector<int>> w2 = {{8, 3, 8, 7, 5, 7, 4, 7, 7, 8}, {5, 1, 10, 7, 8, 0, 6, 10, 8, 9}, {4, 2, 4, 3, 10, 3, 5, 2, 10, 8}, {10, 5, 0, 5, 10, 6, 10, 3, 0, 7}, {10, 5, 6, 9, 10, 4, 9, 5, 3, 7}, {2, 8, 7, 4, 9, 4, 5, 1, 7, 4}, {10, 6, 8, 8, 0, 7, 3, 9, 0, 1}, {5, 8, 4, 0, 6, 4, 2, 2, 9, 6}, {7, 9, 1, 3, 3, 8, 8, 8, 9, 4}, {0, 8, 8, 8, 4, 6, 4, 7, 4, 2}};
    // vector<int> l3out(10);
    // for(int i = 0; i < 10; ++i) {
    //     for(int j = 0; j < 10; ++j) {
    //         l3out[i] += (l2out[j] * w2[j][i]);
    //     }
    //     if(l2out[i] < 0) l2out[i] = 0;
    // }
    // for(auto x: l3out) {
    //     cout << x << " ";
    // }

    // vector<int> w3 = {9, 7, 10, 2, 6, 3, 4, 8, 6, 1};
    // int out = 0;
    // for(int i = 0; i < 10; ++i) {
    //     out += (w3[i] * l3out[i]);
    // }
    // cout << out << endl;
}