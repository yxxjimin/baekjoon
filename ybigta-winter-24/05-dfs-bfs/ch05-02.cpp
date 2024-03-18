// [이것이 코딩 테스트다]
// 05장. DFS/BFS
// 실전문제 - 미로 탈출
#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int** map = new int*[n];
    for (int i = 0; i < n; i++) {
        map[i] = new int[m];
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    }
    
    queue<int> bfs_queue;
    bfs_queue.push(0);
    int idx, cur_r, cur_c;
    while (!bfs_queue.empty()) {
        idx = bfs_queue.front();
        bfs_queue.pop();

        cur_r = idx / m;
        cur_c = idx % m;
        
        if (cur_r > 0 && map[cur_r - 1][cur_c] == 1) {
            bfs_queue.push(idx - m);
            map[cur_r - 1][cur_c] = map[cur_r][cur_c] + 1;
        }
        if (cur_r < n - 1 && map[cur_r + 1][cur_c] == 1) {
            bfs_queue.push(idx + m);
            map[cur_r + 1][cur_c] = map[cur_r][cur_c] + 1;
        }
        if (cur_c > 0 && map[cur_r][cur_c - 1] == 1) {
            bfs_queue.push(idx - 1);
            map[cur_r][cur_c - 1] = map[cur_r][cur_c] + 1;
        }
        if (cur_c < m - 1 && map[cur_r][cur_c + 1] == 1) {
            bfs_queue.push(idx + 1);
            map[cur_r][cur_c + 1] = map[cur_r][cur_c] + 1;
        }

        if (idx == n * m - 1) break;
    }

    cout << map[n - 1][m - 1];

    return 0;
}