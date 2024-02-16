// [이것이 코딩 테스트다]
// 08장. 다이나믹 프로그래밍
// 실전문제 - 1로 만들기
#include <iostream>

using namespace std;

int cache[30001] {0};

int main() {
    int num;
    cin >> num;

    for (int i = 2; i < num + 1; i++) {
        cache[i] = cache[i - 1] + 1;
        if (i % 2 == 0)
            cache[i] = min(cache[i], cache[i / 2] + 1);
        if (i % 3 == 0)
            cache[i] = min(cache[i], cache[i / 3] + 1);
        if (i % 5 == 0)
            cache[i] = min(cache[i], cache[i / 5] + 1);
    }

    cout << cache[num];

    return 0;
}
