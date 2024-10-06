// [이것이 코딩 테스트다]
// 07장. 이진 탐색
// 실전문제 - 부품 찾기
#include <iostream>
#include <algorithm>

using namespace std;

int n, m;

bool binary_search(int* arr, int tgt) {
    int start = 0;
    int end = n;
    int mid;

    while (true) {
        if (end < start) return false;

        mid = (end + start) / 2;

        if (arr[mid] == tgt) return true;
        else if (arr[mid] > tgt) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
}

int main() {
    // Read input
    cin >> n;
    int* existing = new int[n];
    for (int i = 0; i < n; i++) {
        cin >> existing[i];
    }
    sort(existing, existing + n);

    // Binary search
    cin >> m;
    int target;
    for (int i = 0; i < m; i++) {
        cin >> target;
        if (binary_search(existing, target)) {
            cout << "yes" << " ";
        } else {
            cout << "no" << " ";
        }
    }

    delete[] existing;

    return 0;
}