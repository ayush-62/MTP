#include <bits/stdc++.h>
using namespace std;

int main() {
    // imports
    cout << "from z3 import *" << endl;
    cout << "import subprocess" << endl;
    cout << "import time" << endl;

    // variable declaration
    
    // input
    string s;
    for(int i = 1; i < 11; ++i) {
        s += ("in" + to_string(i) + ",");
    }
    s += " = BitVecs('";
    for(int i = 1; i < 11; ++i) {
        s += ("in" + to_string(i) + " ");
    }
    s += "',8)";
    cout << s << endl;

    // parameters
    for(int ver = 1; ver < 3; ++ver) {
        for(int l = 1; l < 4; ++l) {
            for(int node = 1; node < 11; ++node) {
                s = "";
                for(int i = 1; i < 11; ++i) {
                    s += ("l" + to_string(l) + "n" + to_string(node) + "v" + to_string(ver) + "_" + to_string(i) + ",");
                }
                s += " = BitVecs('";
                for(int i = 1; i < 11; ++i) {
                    s += ("l" + to_string(l) + "n" + to_string(node) + "v" + to_string(ver) + "_" + to_string(i) + " ");
                }
                s += "',8)";
                cout << s << endl;
            }
        }
    }

    // output
    for(int ver = 1; ver < 3; ++ver) {
        s = "";
        for(int i = 1; i < 22; ++i) {
            s += ("ov" + to_string(ver) + "_" + to_string(i) + ",");
        }
        s += " = BitVecs('";
        for(int i = 1; i < 22; ++i) {
            s += ("ov" + to_string(ver) + "_" + to_string(i) + " ");
        }
        s += "',8)";
        cout << s << endl;
    }

    // neural network function
    s = "def NN(";
    for(int i = 1; i < 11; ++i) {
        s += ("in" + to_string(i) + ","); 
    }
    for(int l = 1; l < 4; ++l) {
        for(int node = 1; node < 11; ++node) {
            for(int i = 1; i < 11; ++i) {
                s += ("l" + to_string(l) + "n" + to_string(node) + "_" + to_string(i) + ",");
            }
        }
    }
    s += ")";
    cout << s << endl;

    for(int ver = 1; ver < 3; ++ver) {
        s = "";
        for(int i = 1; i < 11; ++i) {
            s += ("in" + to_string(i) + ",");
        }
        for(int l = 1; l < 3; ++l) {
            for(int node = 1; node < 11; ++node) {
                for(int i = 1; i < 11; ++i) {
                    s += ("l" + to_string(l) + "n" + to_string(node) + "v" + to_string(ver) + "_" + to_string(i) + ",");
                }
            }
        }
        for(int node = 1; node < 11; ++node) {
            s += ("l" + to_string(3) + "n" + to_string(node) + "v" + to_string(ver) + "_" + to_string(1) + ",");
        }
        cout << s << endl;
    }
}