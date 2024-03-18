#include <iostream>

int main() {
    int time;
    std::cin >> time;

    int a, b, c;
    a = time / 300;
    b = time % 300 / 60;
    c = time % 300 % 60 / 10;

    if (time % 10 == 0) {
        std::cout << a << " " << b << " " << c;
    } else {
        std::cout << -1;
    }
    
    return 0;
}