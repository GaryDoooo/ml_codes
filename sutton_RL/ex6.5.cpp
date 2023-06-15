#include <bits/stdc++.h>
#define START 30
#define GOAL 37
#define EPSILON 0.1
#define ALPHA 0.5
#define GAMMA 0.9
using namespace std;
double q[100][5];  // Expected all future return of Q[state][action]
// State is the poision on the grid, first row is 0-9, 2nd is 10-19... total 7
// rows action is 0-3, representing left, right, up, down
struct rs {
    double r;
    int s;
};  // structure of returning next state and the reward before it.

rs get_RS(int state, int action) {
    rs result;
    int x = state % 10, y = state / 10;
    int dx[]      = {-1, 1, 0, 0};
    int dy[]      = {0, 0, -1, 1};
    int up_wind[] = {0, 0, 0, 1, 1, 1, 2, 2, 1, 0};

    if ((x == 0 and action == 0) or (x == 9 and action == 1) or
        (y == 0 and action == 2) or (y == 6 and action == 3)) {
        result.r = -2;
        result.s = state;
        return result;
    }
    int new_x = x + dx[action], new_y = y + dy[action] - up_wind[x];
    if ((new_y) < 0) new_y = 0;
    result.s = new_y * 10 + new_x;
    result.r = (result.s == GOAL ? 0 : -1);
    return result;
}

int get_max_a(int state) {
    return max_element(begin(q[state]), end(q[state])) - begin(q[state]);
}

int generate_action(int state) {
    int mod           = 1e8;
    int random_select = (int)((double)1e8 * (double)EPSILON);
    // printf("%d\n%d\n", mod, random_select);
    if (rand() % mod > random_select)
        return get_max_a(state);
    else
        return rand() % 4;
}

vector<int> run_episode() {
    vector<int> path;
    int s = START;
    path.push_back(s);
    while (s != GOAL) {
        int a     = generate_action(s);
        rs result = get_RS(s, a);
        q[s][a] += ALPHA * (result.r +
                            GAMMA * q[result.s][get_max_a(result.s)] - q[s][a]);
        // This is the equation of P153 (6.8)
        s = result.s;
        path.push_back(s);
    }
    return path;
}

int main() {
    time_t t;
    srand((unsigned)time(&t));
    /* Intializes random number generator */
    // q[1][2] = 3;
    // printf("%d\n%d\n", get_max_a(1), generate_action(1));
    while (1) {
        vector<int> path;
        path = run_episode();
        printf("%ld\n", path.size());
        if (path.size() <= 16) {
            for (int s : path) printf("(%d,%d) ", s % 10, s / 10);
            return 0;
        }
    }
}
