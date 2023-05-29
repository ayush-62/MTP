#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<float> inputs(2);
      for(int i = 1; i < 3; ++i) {
        string numerator , denominator = "1" , s;
        int flag = 0;
        s = av[i];
        for(int i = 0 ; i < s.size() ; i++)
        {
            if(s[i] == '/')
            {
                flag = 1;
                i++;
                denominator.pop_back();
            }
            if(flag == 0)
            numerator.push_back(s[i]);
            else
            denominator.push_back(s[i]);
        }
        inputs[i - 1] = stof(numerator)/stof(denominator);
    }

    vector<float> w = {8667, 7893};
    double ans = w[0] * inputs[0] + w[1] * inputs[1];
    cout << (long long int )ans << endl; 
}