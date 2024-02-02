#define PI 3.14159265358979323846
#include <bits/stdc++.h>
using namespace std;
const double R0               = 1;     // the radius of flat circle
const double R                = 2;     // the radius of the dome
const double Theta            = 0.01;  // top angle of the fan slice
const int N                   = 100;   // number of segments
const double Mass_Time_factor = 1e-4;
// a line's movement is propotion to the factor, and segment width l0
// it includes dT, and mass etc.
const double K_Density = 10;
// K of the spring const of unit
// width (cut line length) of the segment
// Both density uses the l0 before strech
// and unit length, longer spring K drops proportionally
// So the sagittal K will be K_Density / d0 * l0
// The tangential K is K_Density / l0 * d0
const double Friction_factor = 0.1;  // the friction from outside air pressure
const double Friction_motion_to_static_ratio = 0.9;
const double Dome_Height                     = R - sqrt(R * R - R0 * R0);

double get_tangential_angle(const double d) {
    const double C = R - Dome_Height + d;
    double a = R0 * R0 + C * C, b = -2 * R0 * R, c = R * R - C * C;
    // double root1 = (-b + sqrt(b * b - 4 * a * c)) / 2 / a;
    double root2 = (-b - sqrt(b * b - 4 * a * c)) / 2 / a;
    // root1 is decrease with d decrease, which is wrong.
    return asin(root2);
}

void test_angle_calc() {
    for (double d = Dome_Height; d >= 0; d -= Dome_Height / 100) {
        double theta = (get_tangential_angle(d));
        double x1 = R * sin(theta), y1 = R * cos(theta);
        double x2 = R0, y2 = (R - Dome_Height) + d;
        double d1_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        double d2_square = x2 * x2 + (y2 * y2);
        if (d2_square - d1_square - R * R > 1e-10) cout << "ERROR" << endl;
        cout << theta << " ";
    }
}

int main() { test_angle_calc(); }
