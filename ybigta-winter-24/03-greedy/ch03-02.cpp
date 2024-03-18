#include <iostream>
#include <climits>

int main () {
    // Read Input
    int m, n;
    int** arr;

    std::cin >> m >> n;
    arr = new int*[m];
    for (int i = 0; i < m; i++) {
        int* row = new int[n];
        for (int j = 0; j < n; j++) {
            std::cin >> row[j];
        }
        arr[i] = row;
    }

    // 1. Find minimum value for each row
    // 2. Find maximum value among row minimum
    int max_value = INT_MIN;
    for (int i = 0; i < m; i++) {
        int row_min = INT_MAX;
        for (int j = 0; j < n; j++) {
            if (row_min > arr[i][j]) {
                row_min = arr[i][j];
            }
        }

        if (row_min > max_value) {
            max_value = row_min;
        }
    }

    std::cout << max_value << std::endl;

    for (int i = 0; i < m; i++) {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}