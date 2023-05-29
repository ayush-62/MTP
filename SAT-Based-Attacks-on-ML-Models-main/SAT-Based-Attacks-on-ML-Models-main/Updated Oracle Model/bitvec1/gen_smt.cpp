#include <bits/stdc++.h>
using namespace std;

void print(string s, int t) {
    while(t--) {
        cout << "\t";
    }
    cout << s << endl;
}

int main(int ac, char* av[]) {
    // arguments
    int layers = stoi(string(av[1])), outsz = 0;
    vector<int> layer_sz(layers);
    for(int i = 0; i < layers; ++i) {
        layer_sz[i] = stoi(string(av[i + 2]));
        if(i) outsz += layer_sz[i];
    }
    
    // imports
    print("from z3 import *", 0);
    print("import subprocess", 0);
    print("import time", 0);
    cout << endl;

    // cexec function
    print("def Cexec(init_string):", 0);
    print("out = subprocess.check_output(\"./a.out %s\" % init_string, shell=True,)", 1);
    print("return list(map(int, out.decode('utf-8').split()))", 1);
    cout << endl;

    print("start_time = time.time()", 0);
    cout << endl;

    // variables declaration
    
    // for inputs
    string s = "", weights[2];
    for(int i = 0; i < layer_sz[0]; ++i) {
        s += ("in" + to_string(i + 1) + ",");
    }
    s.back() = ' ';
    if(layer_sz[0] > 1) {
        s += "= BitVecs('";
    } else {
        s += "= BitVec('";
    }
    for(int i = 0; i < layer_sz[0]; ++i) {
        s += ("in" + to_string(i + 1) + " ");
    }
    s.back() = '\'';
    s += ",8)";
    print(s, 0);
    
    // for parameters
    for(int ver = 1; ver < 3; ++ver) {
        for(int l = 1; l < layers; ++l) {
            for(int nd = 1; nd <= layer_sz[l - 1]; ++nd) {
                s = "";
                for(int j = 0; j < layer_sz[l]; ++j) {
                    s += ("l" + to_string(l) + "n" + to_string(nd) + "v" + to_string(ver) + "_" + to_string(j + 1) + ",");
                    weights[ver - 1] += ("l" + to_string(l) + "n" + to_string(nd) + "v" + to_string(ver) + "_" + to_string(j + 1) + ",");
                }
                s.back() = ' ';
                if(layer_sz[l] > 1) {
                    s += "= BitVecs('";
                } else {
                    s += "= BitVec('";
                }
                for(int j = 0; j < layer_sz[l]; ++j) {
                    s += ("l" + to_string(l) + "n" + to_string(nd) + "v" + to_string(ver) + "_" + to_string(j + 1) + " ");
                }
                s.back() = '\'';
                s += ",8)";
                print(s, 0);
            }
        }
    }

    // for outputs
    for(int ver = 1; ver < 3; ++ver) {
        s = "";
        for(int i = 0; i < outsz; ++i) {
            s += ("ov" + to_string(ver) + "_" + to_string(i + 1) + ",");
        }
        s.back() = ' ';
        if(outsz > 1) {
            s += "= BitVecs('";
        } else {
            s += "= BitVec('";
        }
        for(int i = 0; i < outsz; ++i) {
            s += ("ov" + to_string(ver) + "_" + to_string(i + 1) + " ");
        }
        s.back() = '\'';
        s += ",8)";
        print(s, 0);
    }
    cout << endl;

    // tuple
    print("tuple = Datatype('tuple')", 0);
    
    s = "tuple.declare('tuple',";
    for(int i = 1; i <= outsz; ++i) {
        s += "('" + to_string(i) + "'," + "BitVecSort()),";
    }
    s.pop_back();
    s+=")";
    print(s, 0);

    print("tuple = tuple.create()", 0);

    for(int ver = 1; ver < 3; ++ver) {
        s = "out" + to_string(ver) + " = tuple.tuple(";
        for(int i = 1; i <= outsz; ++i) {
            s += ("ov" + to_string(ver) + "_" + to_string(i) + ",");
        }
        s.pop_back();
        s+=")";
        print(s, 0);
    }
    cout << endl;

    // define the neural network model
    s = "def NN(";
    for(int i = 0; i < layer_sz[0]; ++i) {
        s += ("in" + to_string(i + 1) + ",");
    }
    for(int l = 1; l < layers; ++l) {
        for(int nd = 1; nd <= layer_sz[l - 1]; ++nd) {
            for(int j = 0; j < layer_sz[l]; ++j) {
                s += ("l" + to_string(l) + "n" + to_string(nd) + "_" + to_string(j + 1) + ",");
            }
        }
    }
    s.pop_back();
    s += "):";
    print(s, 0);

    string t = "";
    for(int i = 2; i <= layers; ++i) {
        s = "";
        for(int j = 1; j <= layer_sz[i - 1]; ++j) {
            s += ("l" + to_string(i) + "out_" + to_string(j) + ",");
            t += ("l" + to_string(i) + "out_" + to_string(j) + ",");
        }
        s.pop_back();
        if(layer_sz[i - 1] > 1) {
            s += " = BitVecs('";
        } else {
            s += " = BitVec('";
        }
        for(int j = 1; j <= layer_sz[i - 1]; ++j) {
            s += ("l" + to_string(i) + "out_" + to_string(j) + " "); 
        }
        s.pop_back();
        s += "',8)";
        print(s, 1);

        for(int j = 1; j <= layer_sz[i - 1]; ++j) {
            s = ("l" + to_string(i) + "out_" + to_string(j) + " = ");
            for(int k = 1; k <= layer_sz[i - 2]; ++k) {
                s += "(";
                if(i == 2) {
                    s += ("in" + to_string(k));
                } else {
                    s += ("l" + to_string(i - 1) + "out_" + to_string(k));
                }
                s += " * ";
                s += ("l" + to_string(i - 1) + "n" + to_string(k) + "_" + to_string(j) + ") + ");
            }
            s.pop_back(); s.pop_back();
            print(s, 1);
            s = ("l" + to_string(i) + "out_" + to_string(j) + " = ");
            s += ("If(l" + to_string(i) + "out_" + to_string(j) + " < 0, 0, " + "l" + to_string(i) + "out_" + to_string(j) + ")");
            print(s, 1);
        }
        print("", 1);
    }

    t.pop_back();
    s = "out = tuple.tuple(" + t + ")";
    print(s, 1);
    s = "return out";
    print("", 1);
    print(s, 1);

    cout << endl;

    // declare model
    print("s = Tactic('smt').solver()", 0);
    cout << endl;

    // add parameter ranges to model
    // ifstream ranges("parameters_range.txt");
    // while(getline(ranges, s)) {
    //     string t[4]; int r = 0;
    //     for(int i = 0; i < s.size(); ++i) {
    //         if(!(s[i] == ' ' || s[i] == '_')) {
    //             t[r].push_back(s[i]);
    //         } else {
    //             r++;
    //         }
    //     }
    //     int low = stoi(t[2]), high = stoi(t[3]);
    //     cout << "s.add(" + t[0] + "v1_" + t[1] + " > " + t[2] + ", " + t[0] + "v1_" + t[1] + " < " + t[3] + ")" << endl;
    //     cout << "s.add(" + t[0] + "v2_" + t[1] + " > " + t[2] + ", " + t[0] + "v2_" + t[1] + " < " + t[3] + ")" << endl;
    // }
    // cout << endl;

    // add base condition to our model
    for(int ver = 1; ver < 3; ++ver) {
        s = "s.add(NN(";
        for(int i = 0; i < layer_sz[0]; ++i) {
            s += ("in" + to_string(i + 1) + ",");
        }
        s += weights[ver - 1];
        s.pop_back();
        s += ") == out" + to_string(ver) + ")";
        print(s, 0);
    }
    cout << endl;

    // while loop until unsat happens
    print("while s.check(out1 != out2) == sat:",0);
    print("m = s.model()", 1);

    s = "ia = ";
    for(int i = 0; i < layer_sz[0]; ++i){
        s += "str(m[in" + to_string(i + 1) + "])";
        if(i != layer_sz[0] - 1) {
            s += " + \" \" + ";
        }
    }
    print(s, 1);
    print("print(ia)", 1);
    print("out = Cexec(ia)", 1);
    cout << endl;
    
    for(int i = 1; i <= layer_sz[0]; ++i) {
        print("inp" + to_string(i) + " = m[in" + to_string(i) + "]", 1);
    }
    cout << endl;

    s = "out_tup = tuple.tuple(";
    for(int i = 0; i < outsz; ++i) {
        s += "out[" + to_string(i) + "],";
    }
    s.pop_back();
    s += ")";
    print(s, 1);
    cout << endl;

    for(int ver = 1; ver < 3; ++ver) {
        s = "s.add(NN(";
        for(int i = 0; i < layer_sz[0]; ++i) {
            s += ("inp" + to_string(i + 1) + ",");
        }
        s += weights[ver - 1];
        s.pop_back();
        s += ") == out_tup)";
        print(s, 1);
    }
    cout << endl;

    // print the details
    print("print(s.check(out1 == out2))", 0);
    print("print(s.model())", 0);
    cout << endl;
    print("print(\"Finished in \" + str(time.time() - start_time))", 0);
}