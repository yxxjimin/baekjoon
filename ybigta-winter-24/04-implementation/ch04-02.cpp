// [이것이 코딩 테스트다]
// 04장. 구현
// 실전문제 - 게임 개발

#include <iostream>

using namespace std;

int main() {
    // Read input
    int height, width, pos_x, pos_y, direction;
    cin >> height >> width;
    cin >> pos_x >> pos_y >> direction;

    int** map = new int*[height];
    for (int i = 0; i < height; i++) {
        map[i] = new int[width];
        for (int j = 0; j < width; j++) {
            cin >> map[i][j];
        }
    }

    // Count visited tiles
    int visit_count = 1;
    map[pos_x][pos_y] = 2;
    int turns_waited = 0;
    pair<int, int> move[4] = {
        make_pair(-1, 0),
        make_pair(0, 1),
        make_pair(1, 0),
        make_pair(0, -1)
    };

    while (true) {
        direction = (direction + 3) % 4;

        if (turns_waited == 4) {
            if (map[pos_x - move[direction].first][pos_y - move[direction].second] == 1) {
                break;
            } else {
                pos_x -= move[direction].first;
                pos_y -= move[direction].second;
                turns_waited = 0;
            }
        } else {
            if (map[pos_x + move[direction].first][pos_y + move[direction].second] == 0) {
                pos_x += move[direction].first;
                pos_y += move[direction].second;
                map[pos_x][pos_y] = 2;
                visit_count++;
                turns_waited = 0;
            } else {
                turns_waited++;
            }
        }
    }

    cout << visit_count;

    return 0;
}