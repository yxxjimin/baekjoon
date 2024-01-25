// [이것이 코딩 테스트다]
// 05장. DFS/BFS
// 실전문제 - 음료수 얼려 먹기
#include <iostream>

using namespace std;

int n, m;

void dfs(bool** g, bool* visited, int idx) {
    visited[idx] = true;
    int r = idx / m;
    int c = idx % m;
    cout << r << " " << c << endl;

    if (r > 0 && !visited[idx - m] && !g[r - 1][c]) {
        dfs(g, visited, idx - m);
    }
    if (r < n - 1 && !visited[idx + m] && !g[r + 1][c]) {
        dfs(g, visited, idx + m);
    }
    if (c > 0 && !visited[idx - 1] && !g[r][c - 1]) {
        dfs(g, visited, idx - 1);
    }
    if (c < m - 1 && !visited[idx + 1] && !g[r][c + 1]) {
        dfs(g, visited, idx + 1);
    }
}

int main() {
    cin >> n >> m;

    bool* visited = new bool[n * m];
    fill_n(visited, n * m, false);

    bool** frame = new bool*[n];
    for (int i = 0; i <  n; i++) {
        frame[i] = new bool[m];
        for (int j = 0; j < m; j++) {
            cin >> frame[i][j];
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!frame[i][j] && !visited[i * m + j]) {
                dfs(frame, visited, i * m + j);
                count++;
            }
        }
    }
    
    cout << count;


    return 0;
}