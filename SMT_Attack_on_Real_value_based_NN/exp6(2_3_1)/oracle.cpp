#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> inputs(2);
    for(int i = 1; i < 3; ++i) {
        inputs[i - 1] = stof(string(av[i]));
    }
    //cout<<setprecision(3)<<fixed;
    vector<vector<int>> w = {{96 , 228 , 0}, {62 , 254 , 47}};
    vector<long long int> l1bias = {116 , 0 , 454};
    vector<double> hid(3);
    long long int q_w1 = 1559941072;
    long long int q_b1 = 1529762159;
    long long int shift_w1 = 9;
    long long int shift_b1 = 2;

    vector<int> zp_i = {0 , 0};
    vector<int> zp_w = {78 , 89};
    vector<int> zp_b = {124 , 1};

    vector<vector<float>> l1_updated_weight(2 , vector<float>(3 , 0));
    double valw = round((q_w1/pow(2,shift_w1+31))*1000)/1000;
    for(int i = 0 ; i < 2 ; i++)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            l1_updated_weight[i][j] = ((w[i][j] - zp_w[0])*valw);
            // cout<<" l1_updated_weight"<< i << j << " = " << l1_updated_weight[i][j]<<endl;
        }
    }
    vector<double> l1_updated_bias(3 , 0);
    double valb = round(q_b1/pow(2,shift_b1+31)*1000)/1000;
    for(int i = 0 ; i < 3 ; i++)
    {
        
        l1_updated_bias[i] = (l1bias[i]-zp_b[0])*valb;
        //cout<< setprecision(15) << fixed<< l1_updated_bias[i] <<" ";
    }

    vector<int> input_updated(2 , 0);
    for(int i = 0 ; i < 2 ; i++)
    {
        input_updated[i] = inputs[i] - zp_i[0];
        // cout<<"input_updated "<<i<<" "<<input_updated[i]<<endl;
    }



    hid[0] = input_updated[0] * l1_updated_weight[0][0] + input_updated[1] * l1_updated_weight[1][0] + l1bias[0];
    if(hid[0] < 0 ) hid[0] = 0;
    hid[0] = hid[0] + zp_i[1];

    hid[1] = input_updated[0] * l1_updated_weight[0][1] + input_updated[1] * l1_updated_weight[1][1] + l1bias[1];
    if(hid[1] < 0 ) hid[1] = 0;
    hid[1] = hid[1] + zp_i[1];

    hid[2] = input_updated[0] * l1_updated_weight[0][2] + input_updated[1] * l1_updated_weight[1][2] + l1bias[2];
    if(hid[2] < 0 ) hid[2] = 0;
    hid[2] = hid[2] + zp_i[1];

    cout<<hid[0]<<" "<<hid[1]<<" "<<hid[2];
    // vector<float> w2 = {-0.00689 , 5.1292 , -2.7963};
    // float l3bias = -1.9866;
    // float ans = hid[0] * w2[0] + hid[1] * w2[1] + hid[2] * w2[2] + l3bias;
    // if(ans < 0) ans = 0;
    // cout << ans << endl;
}