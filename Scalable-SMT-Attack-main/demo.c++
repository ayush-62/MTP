#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;
int main(){
    for(int i = 1; i <= 32; i++){
        printf("s.add(i%d >= 0 , i%d <= 255)\n",i,i);
    }
}