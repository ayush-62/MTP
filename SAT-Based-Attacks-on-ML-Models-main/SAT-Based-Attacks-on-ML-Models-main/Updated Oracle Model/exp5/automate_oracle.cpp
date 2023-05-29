#include <bits/stdc++.h>
using namespace std;

int rand(int a, int b) {
    int res = a + rand() % (b - a + 1);
    return res;
}

string generate_random(int k, int l, int h) {
    string ans = "{";
    for(int i = 0; i < k; ++i) {
        int x = rand(l, h);
        ans += (to_string(x) + ", ");
    }
    ans.pop_back(); ans.pop_back();
    ans.push_back('}');
    return ans;
}

int main() {
    string ans = "{";
    for(int i = 0; i < 10; ++i) {
        string x = generate_random(10, 0, 1);
        ans += (x + ", ");
    }
    ans.pop_back(); ans.pop_back();
    ans.push_back('}');
    cout << ans << endl;

    ans = "{";
    for(int i = 0; i < 10; ++i) {
        string x = generate_random(10, 0, 1);
        ans += (x + ", ");
    }
    ans.pop_back(); ans.pop_back();
    ans.push_back('}');
    cout << ans << endl;

    cout << generate_random(10, 0, 1) << endl;
}