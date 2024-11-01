#include <algorithm>
#include <vector>
using namespace std;

float get_max(vector<float>& imageData) {
    float max_value = 0, min_value = 1e8;
    for (auto i : imageData) {
        max_value = max(max_value, i);
        min_value = min(min_value, i);
    }
    return max_value;
}

int get_one() { return 1; }
