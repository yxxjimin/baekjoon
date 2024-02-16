// [이것이 코딩 테스트다]
// 08장. 다이나믹 프로그래밍
// 실전문제 - 개미 전사
#include <iostream>

using namespace std;

int storage[101] {0};

int main() {
    int num_storage;
    cin >> num_storage;

    for (int i = 0; i < num_storage; i++) {
        cin >> storage[i + 1];
    }

    int stolen = 0;
    int prev2 = storage[1];
    int prev1 = storage[2];
    int curr;
    for (int i = 3; i < num_storage + 1; i++) {
        curr = max(storage[i] + prev2, prev1);
        prev2 = prev1;
        prev1 = curr;
    }

    cout << curr;

    return 0;
}
