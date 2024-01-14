#include <iostream>

int main() {
    int n, k;
    std::cin >> n >> k;

    int count = 0;
    while (n > 1) {
        if (n % k == 0) {
            n = n / k;
            count++;
        } else {
            int r = n % k;
            n -= r;
            count += r;
        }
    }
    
    std::cout << count << std::endl;

    return 0;
}