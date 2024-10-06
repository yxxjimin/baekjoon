#include <iostream>
#include <algorithm>
#include <climits>

int main() {
    int n;
    int* weights;

    std::cin >> n;
    weights = new int[n + 1];
    for (int i = 0; i < n; i++) {
        std::cin >> weights[i];
    }
    weights[n] = INT_MAX;

    std::sort(weights, weights + n);

    int max;
    int sum = 0;
    if (weights[0] != 1) {
        max = 1;
    } else {
        for (int i = 0; i < n; i++) {
            sum += weights[i];
            if (sum < weights[i + 1] - 1) {
                break;
            }
        }
        max = sum + 1;
    }

    std::cout << max;

    delete[] weights;

    return 0;
}