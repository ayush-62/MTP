#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<double> inputs(3);
    for(int i = 1; i < 4; ++i) {
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
        inputs[i - 1] = stof(av[i]);
    }
    //cout<<inputs[0]<<"  "<<inputs[1]<<"  "<<inputs[2]<<" ";
    vector<vector<double>> w = {{-6.0, 10.6, 5.0, 1.2}, {8.0, -7.0, 1.0, -1.0}, {4.0, 7.0, -3.5, -2.0}};
    vector<double> l2out(4,0);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 3; ++j) {
            l2out[i] += (inputs[j] * w[j][i]);
        }
        if(l2out[i] < 0) l2out[i] = 0;
    }
    for(auto x: l2out) {
        cout << x << " ";
    }

    vector<vector<double>> w2 = {{-3.0, 4.4, 5.0, 9.0}, {6.0, -7.6, 1.0, 4.0}, {3.0, -3.0, -3.0, -3.8}, {3.0, -3.0, -3.0, -3.0}};
    vector<double> l3out(4,0);
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            l3out[i] += (l2out[j] * w2[j][i]);
        }
        if(l3out[i] < 0) l3out[i] = 0;
    }
    for(auto x: l3out) {
        cout << x << " ";
    }

    vector<double> w3 = {2.0, -1.3, 1.0, 7.3};
    double out = 0;
    for(int i = 0; i < 4; ++i) {
        out += (w3[i] * l3out[i]);
    }
     cout << out << endl;
}