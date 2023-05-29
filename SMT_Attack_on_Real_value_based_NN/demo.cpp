#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    double number = 3.14769;
    double i = 3.7899;
    std::cout << "Original number: " << number << std::endl;
    
    std::cout << std::fixed;
    std::cout << std::setprecision(2);  // Set precision to 2 decimal places
    
    std::cout << "Truncated number: " << number << std::endl;
    cout<<number*i;
    return 0;
}