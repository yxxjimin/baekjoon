#include <iostream>

int main() {
    int n;

    std::cin >> n;

    int amount;
    int coins[] = { 25, 10, 5, 1 };
    for (int i = 0; i < n; i++) {
        std::cin >> amount;
        
        for (int j = 0; j < 4; j++) {
            std::cout << amount / coins[j] << " ";
            amount %= coins[j];
        }
        std::cout << std::endl;
    }

    return 0;
}