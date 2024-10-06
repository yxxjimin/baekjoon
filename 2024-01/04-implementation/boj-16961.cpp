#include <iostream>

using namespace std;

int main() {
    // Read input
    int num_guests;
    cin >> num_guests;

    int tab[366] = {0};
    int space[366] = {0};

    char family;
    int start, end;
    int longest_guest = 0;
    for (int i = 0; i < num_guests; i++) {
        cin >> family >> start >> end;

        // Find longest days of stay
        if (end - start + 1 > longest_guest)
            longest_guest = end - start + 1;
        
        // Record guest info
        for (int j = start - 1; j < end; j++) {
            if (family == 'T') tab[j]++;
            else space[j]++;
        }
    }

    // Count days
    int exist_guests = 0;
    int max_guests = 0;
    int no_fights = 0;
    int max_guest_no_fight = 0;

    for (int i = 0; i < 366; i++) {
        // Existing guests
        if (tab[i] + space[i] > 0) 
            exist_guests++;

        // Maximum number of guests
        if (tab[i] + space[i] > max_guests)
            max_guests = tab[i] + space[i];
        
        // No fights
        if (tab[i] == space[i] && tab[i] > 0 && space[i] > 0) {
            no_fights++;
            if (tab[i] + space[i] > max_guest_no_fight)
                max_guest_no_fight = tab[i] + space[i];
        }
    }

    cout << exist_guests << "\n";
    cout << max_guests << "\n";
    cout << no_fights << "\n";
    cout << max_guest_no_fight << "\n";
    cout << longest_guest;

    return 0;
}