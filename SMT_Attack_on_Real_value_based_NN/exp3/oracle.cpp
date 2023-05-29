#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<float> inputs(2);
    for(int i = 1; i < 3; ++i) {
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
    vector<vector<float>> w = {{1.3, 2}, {2.0, 3}};
    vector<float> hid(2);

    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0];
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1];

    if(hid[0] < 0) hid[0] = 0;
    if(hid[1] < 0) hid[1] = 0;

    vector<float> w2 = {7.8, 8.0};

    float ans = hid[0] * w2[0] + hid[1] * w2[1];
    cout << ans << endl;
}