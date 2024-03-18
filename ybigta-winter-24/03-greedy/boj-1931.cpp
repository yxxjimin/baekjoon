#include <iostream>
#include <algorithm>

bool compare(const std::pair<int, int> &a, const std::pair<int, int> &b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    return a.second < b.second;
}

int main() {
    // Read input
    int n;
    std::pair<int, int>* intervals;

    std::cin >> n;
    intervals = new std::pair<int, int>[n];
    for (int i = 0; i < n; i++) {
        int start, end;
        std::cin >> start >> end;
        intervals[i] = std::make_pair(start, end);
    }

    // Sort by earliest end time
    std::sort(intervals, intervals + n, compare);
    
    // Select by earliest end time
    int count = 0;
    int start_time = 0;
    int end_time = 0;
    for (int i = 0; i < n; i++) {
        if (intervals[i].first >= end_time) {
            count++;
            start_time = intervals[i].first;
            end_time = intervals[i].second;
        }
    }

    std::cout << count;
    
    delete[] intervals;

    return 0;
}