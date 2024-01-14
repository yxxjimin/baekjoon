#include <iostream>
#include <algorithm>

int main() {
    // Read input
    int n, m, k;
    int* arr;

    std::cin >> n >> m >> k;
    arr = new int[n];

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    // Sort array
    std::sort(arr, arr + n, std::greater<int>());

    // Calculate sum
    int repeated_sum = k * arr[0] + arr[1];
    int q = m / (k + 1);
    int r = m % (k + 1);

    int sum = q * repeated_sum + r * arr[0];

    std::cout << sum << std::endl;
    
    delete[] arr;

    return 0;
}
