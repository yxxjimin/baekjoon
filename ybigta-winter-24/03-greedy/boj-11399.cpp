#include <iostream>
#include <algorithm>

int main() {
    int n;
    int* p_arr;

    std::cin >> n;
    p_arr = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> p_arr[i];
    }

    std::sort(p_arr, p_arr + n);
    int total_time = 0;
    for (int i = 0; i < n; i++) {
        total_time += (n - i) * p_arr[i];
    }

    std::cout << total_time;

    delete[] p_arr;

    return 0;
}