#include <iostream>

int main() {
    int price, change;
    std::cin >> price;
    change = 1000 - price;

    int count = 0;
    int coins[6] = { 500, 100, 50, 10, 5, 1 };

    for (int i = 0; i < 6; i++) {
        count += change / coins[i];
        change %= coins[i];
    }

    std::cout << count;

    return 0;
}