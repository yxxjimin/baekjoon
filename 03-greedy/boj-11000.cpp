#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

int main() {
    // Read input
    int n;
    std::pair<int, int>* intervals;
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap_by_T;

    std::cin >> n;
    intervals = new std::pair<int, int>[n];
    for (int i = 0; i < n; i++) {
        int first, second;
        std::cin >> first >> second;
        intervals[i] = std::make_pair(first, second);
    }

    // Sort by starting time
    std::sort(intervals, intervals + n);

    // Start-first lecture assignment
    for (int i = 0; i < n; i++) {
        min_heap_by_T.push(intervals[i].second);
        if (min_heap_by_T.top() <= intervals[i].first) {
            min_heap_by_T.pop();
        }
    }

    std::cout << min_heap_by_T.size();

    delete[] intervals;

    return 0;
}