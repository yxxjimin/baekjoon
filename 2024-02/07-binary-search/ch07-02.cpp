// [이것이 코딩 테스트다]
// 07장. 이진 탐색
// 실전문제 - 떡볶이 떡 만들긱
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    // Read input
    int n, m;
    cin >> n >> m;

    int* tteoks = new int[n];
    for (int i = 0; i < n; i++) {
        cin >> tteoks[i];
    }

    // Parametric search
    int start = 0;
    int end = *max_element(tteoks, tteoks + n);
    int mid, sum;
    while (start < end) {
        mid = (start + end) / 2;

        sum = 0;
        for (int i = 0; i < n; i++) {
            if (tteoks[i] > mid) sum += (tteoks[i] - mid);
        }

        if (sum == m) break;
        else if (sum > m) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }

    cout << mid;

    delete[] tteoks;

    return 0;
}