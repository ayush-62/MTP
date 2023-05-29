#include <bits/stdc++.h>
using namespace std;

int main() {
    for(int ver = 1; ver < 3; ++ver) {
        for(int layer = 1; layer < 4; ++layer) {
            for(int node = 1; node < 11; ++node) {
                cout << "l" << layer << "n" << node << "v" << ver << " = IntVector(" << "'layer" << layer << "node" << node << "v" << ver << "'" << ", 10)" << endl;
            }
        }
    }

    for(int l = 1; l < 4; ++l) {
        cout << "l" << l << "outv1" << " = IntVector(" << "'l" << l << "outv1'" << ", 10)" << endl;
        cout << "l" << l << "outv2" << " = IntVector(" << "'l" << l << "outv2'" << ", 10)" << endl;
    }

    cout << "l" << 4 << "outv1" << " = IntVector(" << "'l" << 4 << "outv1'" << ", 1)" << endl;
    cout << "l" << 4 << "outv2" << " = IntVector(" << "'l" << 4 << "outv2'" << ", 1)" << endl;

    cout << "def NN(input";
    for(int layer = 1; layer < 4; ++layer) {
        for(int node = 1; node < 11; ++node) {
            cout << ", l" << layer << "n" << node;
        }
    }
    cout << "):" << endl;

    cout << "l2out = IntVector('l2out', 10)" << endl;
    for(int i = 0; i < 10; ++i) {
        string s = "l2out[" + to_string(i) + "] = Or(";
        for(int inp = 0; inp < 10; ++inp) {
            s = s + "And(input[" + to_string(inp) + "], l1n" + to_string(inp + 1) + "[" + to_string(i) + "])";
            if(inp < 9) {
                s = s + ", ";
            } else {
                s = s + ")";
            }
        }
        cout << s << endl;
    }

    cout << "l3out = IntVector('l3out', 10)" << endl;
    for(int i = 0; i < 10; ++i) {
        string s = "l3out[" + to_string(i) + "] = Or(";
        for(int inp = 0; inp < 10; ++inp) {
            s = s + "And(l2out[" + to_string(inp) + "], l2n" + to_string(inp + 1) + "[" + to_string(i) + "])";
            if(inp < 9) {
                s = s + ", ";
            } else {
                s = s + ")";
            }
        }
        cout << s << endl;
    }

    cout << "l4out = IntVector('l4out', 1)" << endl;
    for(int i = 0; i < 1; ++i) {
        string s = "l4out[" + to_string(i) + "] = Or(";
        for(int inp = 0; inp < 10; ++inp) {
            s = s + "And(l3out[" + to_string(inp) + "], l3n" + to_string(inp + 1) + "[" + to_string(i) + "])";
            if(inp < 9) {
                s = s + ", ";
            } else {
                s = s + ")";
            }
        }
        cout << s << endl;
    }

    vector<string> nn(2, "");
    for(int v = 0; v < 2; ++v) {
        nn[v] = "NN(input";
        for(int layer = 1; layer < 4; ++layer) {
            for(int node = 1; node < 11; ++node) {
                nn[v] +=  (", l" + to_string(layer) + "n" + to_string(node) + "v" + to_string(v+1));
            }
        }
        nn[v] += ")";
    }
    
    vector<string> s(2, "");
    for(int v = 1; v < 3; ++v) {
        for(int i = 0; i < 21; ++i) {
            s[v - 1] += (nn[v - 1] + "[" + to_string(i) + "] == outv" + to_string(v) + "[" + to_string(i) + "], ");
        }
    }
    cout << s[0] << endl << s[1] << endl;

    for(int i = 0; i < 21; ++i) {
        cout << "outv1[" + to_string(i) + "] != outv2[" + to_string(i) + "], ";
    }
    cout << endl;

    for(int i = 0; i < 21; ++i) {
        cout << "outv1[" + to_string(i) + "] == outv2[" + to_string(i) + "], ";
    }
    cout << endl;

    nn[0] = ""; nn[1] = "";
    for(int v = 0; v < 2; ++v) {
        nn[v] = "NN(inp";
        for(int layer = 1; layer < 4; ++layer) {
            for(int node = 1; node < 11; ++node) {
                nn[v] +=  (", l" + to_string(layer) + "n" + to_string(node) + "v" + to_string(v+1));
            }
        }
        nn[v] += ")";
    }

    s[0] = ""; s[1] = "";
    for(int v = 1; v < 3; ++v) {
        for(int i = 0; i < 21; ++i) {
            s[v - 1] += (nn[v - 1] + "[" + to_string(i) + "] == out" + "[" + to_string(i) + "], ");
        }
    }
    cout << s[0] << endl << s[1] << endl;

    // m[l1n1v1[0]] + m[l1n1v1[1]] + 
    for(int node = 0; node < 10; ++node) {
        string w = "";
        for(int i = 0; i < 10; ++i) {
            w += "str(m[l1n" + to_string(node + 1) + "v1[" + to_string(i) + "]])";
            if(i < 9) {
                w += (" + ");
            }
        }
        cout << w << endl;
    }
}