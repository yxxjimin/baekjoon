#include <iostream>

using namespace std;

bool check_valid_move(int dx, int dy) {
    if ((dx == 2 && dy == 1)
        || (dx == 2 && dy == -1)
        || (dx == -2 && dy == 1)
        || (dx == -2 && dy == -1)
        || (dx == 1 && dy == 2)
        || (dx == 1 && dy == -2)
        || (dx == -1 && dy == 2)
        || (dx == -1 && dy == -2))
        return true;
    else
        return false;
}

int main() {
    char alpha, numr, init_alpha, init_numr;
    bool visited[6][6] = {0, };
    int visited_tiles_count = 0;
    int prev_alpha, prev_numr;
    bool current_move_valid, final_move_valid;
    for (int i = 0; i < 36; i++) {
        // Check move validity
        if (i == 0) {
            current_move_valid = true;
            cin >> alpha >> numr;
            init_alpha = alpha;
            init_numr = numr;
        } else {
            prev_alpha = alpha;
            prev_numr = numr;
            cin >> alpha >> numr;
            current_move_valid = check_valid_move(
                alpha - prev_alpha, numr - prev_numr);
        }
        
        // Count as visited if valid move
        if (current_move_valid && !visited[alpha - 'A'][numr - '1']) {
            visited[alpha - 'A'][numr - '1'] = true;
            visited_tiles_count++;
        }

        // Check validity of returning to initial point
        if (i == 35) {
            final_move_valid = check_valid_move(
                alpha - init_alpha, numr - init_numr);
        }
    }

    if (final_move_valid && visited_tiles_count == 36) {
        cout << "Valid";
    } else {
        cout << "Invalid";
    }

    return 0;
}