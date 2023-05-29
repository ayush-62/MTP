#include <bits/stdc++.h>
using namespace std;

int main(int ac, char* av[]) {
    vector<int> a(3, 0);
    for(int i = 1; i < 4; ++i) {
        string t = string(av[i]);
        if(t == "True") {
            a[i - 1] = 1;
        }
    }
    int ans = (((a[0] && a[1]) || (a[1] && a[2]) || (!(1 ^ (a[0] && a[2])))) ^ 0);
    cout << ((ans == 0) ? "False" : "True") << endl;
}