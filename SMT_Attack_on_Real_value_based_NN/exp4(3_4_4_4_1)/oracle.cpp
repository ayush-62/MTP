#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<double> inputs(3);
    for(int i = 1; i < 4; ++i) {
        inputs[i - 1] = stod(av[i]);
    }
    vector<vector<double>> w = {{-6.6, 10.3, 5.0, 1.2}, {8.5, -7.0, 1.2, -1.0}, {4.0, 7.9, -3.7, -2.0}};
    vector<double> l2out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 3; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
           
        }
         if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    vector<vector<double>> w2 = {{-3.5, 4.0, 5.0, 9.7}, {6.6, -7.0, 1.0, 4.0}, {3.5, -3.8, -3.8, -3.0}, {3.6, -3.0, -3.7, -3.9}};
    vector<double> l3out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            l3out[i] += (inputs[j] * w2[j][i]);
            
        }
         if(l3out[i] < 0) l3out[i] = 0;
    }
    // for(auto x: l3out) {
    //     cout << x << " ";
    // }

    vector<vector<double>> w3 = {{-3.8, 4.6, 5.0, 9.0}, {6.3, -7.6, 1.9, 4.0}, {3.4, -3.2, -3.6, -3.8}, {3.0, -3.0, -3.0, -3.0}};
    vector<double> l4out(4);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            l4out[i] += (l3out[j] * w3[j][i]);
        }
         if(l4out[i] < 0) l4out[i] = 0;
    }
    // for(auto x: l4out) {
    //     cout << x << " ";
    // }

    vector<double> w4 = {2.0, -1.3, 1.4, 7.6};
    double out = 0;
    for(int i = 0; i < 4; ++i) {
        out += (w4[i] * l4out[i]);
    }
    if(out < 0) out = 0;
   // cout << out << endl;
}