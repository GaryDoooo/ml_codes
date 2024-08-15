#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
#define SAMPLE_TIMES 1000000
using namespace std;

// Function to calculate the mean
double calculateMean(const std::vector<double>& data) {
    if (data.empty()) return 0.0;
    double sum = std::accumulate(data.begin(), data.end(), 0.0);
    return sum / data.size();
}
//
// Function to calculate the standard deviation
double calculateStandardDeviation(const std::vector<double>& data) {
    if (data.size() < 2) return 0.0;
    double mean         = calculateMean(data);
    double sumOfSquares = 0.0;
    for (const double& value : data) {
        sumOfSquares += (value - mean) * (value - mean);
    }
    return std::sqrt(sumOfSquares /
                     (data.size() - 1));  // Sample standard deviation
}
pair<double, double> gapStat(double gap, bool print = false) {
    vector<double> res;
    double mean, std;
    // Seed with a real random value, if available
    std::random_device rd;

    // Initialize a Mersenne Twister random number generator
    std::mt19937 gen(rd());

    // Define a normal distribution with mean 0.0 and standard deviation 1.0
    std::normal_distribution<> d(0.0, 1.0);
    for (int i = 0; i < SAMPLE_TIMES; i++)
        res.push_back((d(gen) - d(gen) - gap));
    mean = calculateMean(res);
    std  = calculateStandardDeviation(res);
    if (print) {
        cout << "Mean of the abs difference of two samples: " << mean << endl;
        cout << "Std of them " << std << endl;
    }
    return make_pair(mean, std);
}

int main() {
    // Generate two samples and get their distance
    cout << "Mean,Stdev" << endl;
    for (double gap = 0; gap <= 10; gap += .5) {
        pair<double, double> res = gapStat(gap);
        cout << gap << "," << res.first << "," << res.second << endl;
    }
}
