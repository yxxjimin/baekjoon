// [이것이 코딩 테스트다]
// 08장. 다이나믹 프로그래밍
// 실전문제 - 바닥 공사
#include <iostream>

using namespace std;

int main() {
    int length;
    cin >> length;

    int prev2 = 1;
    int prev1 = 1;
    int curr;

    if (length == 1)
        curr = 1;
    else {
        for (int i = 2; i < length + 1; i++) {
            curr = (prev1 * 1) + (prev2 * 2) % 796796;
            prev2 = prev1;
            prev1 = curr;
        }
    }

    cout << curr;

    return 0;
}