#include <bits/stdc++.h>
using namespace std;

int rand(int a, int b) {
    return a + rand() % (b - a + 1);
}

int main(int ac, char* av[]) {
    srand(atoi(av[1]));
    int a = rand(1, 1000);
    int b = rand(1, 1000);
    cout << a << " " << b << endl;
}