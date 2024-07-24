#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric> // for accumulate

using namespace std;

class AndersonDarlingTest {
public:
    AndersonDarlingTest(const vector<double>& data) : data(data), size(data.size()) {}

    double variance() {
        double mean_val = mean();
        double var_sum = 0.0;
        for(int i = 0; i < size; i++) {
            var_sum += pow(data.at(i) - mean_val, 2);
        }
        return var_sum / (size - 1);
    }

    double mean() {
        return accumulate(data.begin(), data.end(), 0.0) / size;
    }

    double phi(double x) {
        return 0.5 * erfc(-x * M_SQRT1_2);
    }

    vector<double> tostdnormal() {
        vector<double> Y(size);
        double mean_val = mean();
        double variance_val = variance();
        for(int i = 0; i < size; i++) {
            Y.at(i) = (data.at(i) - mean_val) / sqrt(variance_val);
        }
        return Y;
    }

    double Anderson_Darling() {
        sort(data.begin(), data.end());
        int n = size;
        vector<double> Y = tostdnormal();

        double S = 0;
        for(int i = 0; i < n; i++) {
            double a = 2.0 * (i + 1) - 1;
            double b = log(phi(Y.at(i)));
            double c = log(1 - phi(Y.at(n - i - 1)));
            S += a * (b + c);
        }
        return -n - S / n;
    }

private:
    vector<double> data;
    int size;
};

int main() {
    vector<double> data = {1.2, 2.3, 3.4, 4.5, 5.6}; // Example input data
    AndersonDarlingTest adTest(data);
    double result = adTest.Anderson_Darling();
    cout << "Anderson-Darling Statistic: " << result << endl;
    return 0;
}

