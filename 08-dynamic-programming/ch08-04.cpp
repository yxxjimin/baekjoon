// [이것이 코딩 테스트다]
// 08장. 다이나믹 프로그래밍
// 실전문제 - 효율적인 화폐 구성
#include <iostream>
#include <climits>

using namespace std;

int cache[10001] {0};

int main() {
    int coin_types, tgt;
    cin >> coin_types >> tgt;

    int* coins = new int[coin_types];
    for (int i = 0; i < coin_types; i++) {
        cin >> coins[i];
        cache[coins[i]] = 1;
    }

    for (int i = coins[0]; i < tgt + 1; i++) {
        for (int j = 0; j < coin_types; j++) {
            if (i - coins[j] > 0 && cache[i - coins[j]] > 0)
                cache[i] = cache[i - coins[j]] + 1;
        }
    }

    if (cache[tgt] > 0)
        cout << cache[tgt];
    else
        cout << -1;

    delete[] coins;

    return 0;
}