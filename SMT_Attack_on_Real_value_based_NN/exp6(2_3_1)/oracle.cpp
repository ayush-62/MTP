#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<float> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }

    vector<vector<float>> w = {{0.3572 , 3.0436 , -1.606}, {-0.3158 , 3.5808, -0.6303}};
    vector<float> l1bias = {-0.1541 , -2.2765 , 2.3786};
    vector<float> hid(3);
    // long long int q_w1=1559941072;
    // long long int q_b1=1529762159;
    // long long int shift_w1=9;
    // long long int shift_b1=2;

    // vector<int>zp_i(2,0);
    // vector<int>zp_w={78,89};
    // vector<int>zp_b = {124 , 1};

    // vector<vector<float>> updated_weight(2 , vector<float>(0 , 3));
    // updated_weight[0][0] = 



    hid[0] = inputs[0] * w[0][0] + inputs[1] * w[1][0] + l1bias[0];
    if(hid[0] < 0 ) hid[0] = 0;
    hid[1] = inputs[0] * w[0][1] + inputs[1] * w[1][1] + l1bias[1];
    if(hid[1] < 0 ) hid[1] = 0;
    hid[2] = inputs[0] * w[0][2] + inputs[1] * w[1][2] + l1bias[2];
    if(hid[2] < 0 ) hid[2] = 0;

    cout<<hid[0]<<" "<<hid[1]<<" "<<hid[2];
    vector<float> w2 = {-0.00689 , 5.1292 , -2.7963};
    float l3bias = -1.9866;
    ans = hid[0] * w2[0] + hid[1] * w2[1] + hid[2] * w2[2] + l3bias;
    if(ans < 0) ans = 0;
    // cout << ans << endl;
}