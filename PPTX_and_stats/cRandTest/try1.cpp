#include <iostream>
#include <random>

int main() {
    // Seed with a real random value, if available
    std::random_device rd;

    // Initialize a Mersenne Twister random number generator
    std::mt19937 gen(rd());

    // Define a normal distribution with mean 0.0 and standard deviation 1.0
    std::normal_distribution<> d(0.0, 1.0);

    // Generate and print 10 random numbers from the normal distribution
    for (int n = 0; n < 10; ++n) {
        std::cout << d(gen) << std::endl;
    }

    return 0;
}
