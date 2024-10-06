// [이것이 코딩 테스트다]
// 04장. 구현
// 실전문제 - 왕실의 나이트

#include <iostream>

int main() {
    // Read input
    char input[2];
    int row, col;
    std::cin >> input;

    col = input[0] - 'a';
    row = input[1] - '1';

    std::pair<int, int> movements[8] = {
        std::make_pair(2, 1),
        std::make_pair(2, -1),
        std::make_pair(1, 2),
        std::make_pair(-1, 2),
        std::make_pair(1, -2),
        std::make_pair(-1, -2),
        std::make_pair(-2, 1),
        std::make_pair(-2, -1),
    };

    int count = 0;
    for (int i = 0; i < 8; i++) {
        if (col + movements[i].first >= 0 && col + movements[i].first < 8
            && row + movements[i].second >= 0 && row + movements[i].second < 8)
            count++;
    }

    std::cout << count;

    return 0;
}