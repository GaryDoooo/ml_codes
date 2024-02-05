#include <bits/stdc++.h>
// #define EPSILON 0.1
#define ALPHA 0.9
#define GAMMA 0.9
#define STOP_ROUNDS 100000
using namespace std;
struct game {
    int board;  // use bit 0 to 19 to record the status of the grid
    // first row is 0-3, 2nd is 4-7, so on
    int score;  // accumulated award
};
struct RS {         // Reward after the action and the resulted state
    double reward;  // Put a block down without game over is -1,
    // Game over is -1e8, clean one row is 2, clean two row is 5
    int board;
};

double q[1 << 20][7];  // Expected all future return of Q[state][action]
double EPSILON = 0.1;

RS get_RS(int board, int action) {
    // Action is coded from 0-6
    // 0-3 is vertically put the block down at the col 0-3
    // 4-6 is horizontally put the block down while the left block is at col 0-2
    int entry_by_action[7][2] = {{0, 4}, {1, 5}, {2, 6}, {3, 7},
                                 {0, 1}, {1, 2}, {2, 3}};
    RS result;
    int b1 = entry_by_action[action][0], b2 = entry_by_action[action][1];

    if ((board >> b1) & 1 or (board >> b2) & 1) {
        // Block can't fall into the board, Game over
        result.board  = board;
        result.reward = -1e8;
        return result;
    }
    // Drop the block
    bool dropped = false;
    while (!dropped) {
        int new_b1 = b1 + 4, new_b2 = b2 + 4;
        if ((board >> new_b1) & 1 or (board >> new_b2) & 1 or new_b1 > 19 or
            new_b2 > 19) {
            dropped = true;
            board |= 1 << b1;
            board |= 1 << b2;
        } else {
            b1 = new_b1;
            b2 = new_b2;
        }
    }
    // Check if there is a clear
    int clear_cnt = 0;
    for (int row_start = 0; row_start < 20; row_start += 4) {
        bool filled = true;
        for (int cell = row_start; cell < row_start + 4; cell++)
            filled &= board >> cell;
        if (filled) {
            clear_cnt++;
            board &= ~(15 << row_start);  // clear the row that is filled
            int mask = (1 << 20) - (1 << row_start);
            // Mask has all 1 at the bit higher than the cleared row
            int stationary_part = board & mask;  // record the parts don't move
            board &= (~mask);          // remove all the stationary parts.
            board <<= 4;               // move the rest of blocks one line down
            board |= stationary_part;  // put the stationary blocks back
        }
    }
    int reward_by_row_cleared[] = {-1, 2, 5};
    result.reward               = reward_by_row_cleared[clear_cnt];
    result.board                = board;
    return result;
}

void print_game(game g) {
    int b = g.board;
    for (int y = 0; y < 5; ++y) {
        printf("|");
        for (int x = 0; x < 4; ++x) {
            if (b & 1)
                printf("[]");
            else
                printf("  ");
            b >>= 1;
        }
        printf("|");
        if (y == 1) printf(" Score: %d", g.score);
        printf("\n");
    }
    printf("----------\n\n");
}

int get_max_a(int state) {
    return max_element(begin(q[state]), end(q[state])) - begin(q[state]);
}

int generate_action(game g) {
    int state         = g.board;
    int mod           = 1e8;
    int random_select = (int)((double)1e8 * (double)EPSILON);
    // printf("%d\n%d\n", mod, random_select);
    if (rand() % mod > random_select)
        return get_max_a(state);
    else
        return rand() % 7;
}

vector<game> run_episode() {
    vector<game> path;
    game g = {0, 0};
    path.push_back(g);
    while (path.size() <= STOP_ROUNDS) {
        int a     = generate_action(g);
        RS result = get_RS(g.board, a);
        if (result.reward <= -1e8)  // Game Over
            return path;
        q[g.board][a] +=
            ALPHA *
            (result.reward + GAMMA * q[result.board][get_max_a(result.board)] -
             q[g.board][a]);
        // This is the equation of P153 (6.8)
        g.board = result.board;
        g.score += result.reward;
        path.push_back(g);
    }
    return path;
}

int main() {
    time_t t;
    srand((unsigned)time(&t));
    // [> Intializes random number generator <]
    int episode_cnt = 0;
    while (++episode_cnt) {
        vector<game> path;
        path = run_episode();
        if (path.size() >= STOP_ROUNDS) {
            print_game(path.back());
            printf("Total episode: %d\n", episode_cnt);
            return 0;
        } else {
            if (ceil(log2(episode_cnt)) == floor(log2(episode_cnt))) {
                print_game(path.back());
                printf("Total episode: %d\tPlayed %ld steps.\n\n", episode_cnt,
                       path.size());
            }
        }
        if (ceil(log(episode_cnt) / log(10)) ==
            floor(log(episode_cnt) / log(10)))
            EPSILON /= 2;
    }
}
