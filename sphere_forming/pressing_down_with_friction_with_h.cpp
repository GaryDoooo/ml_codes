#define PI 3.14159265358979323846
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#include <math.h>
#include <stdio.h>
#include <string.h>
#include "./pressing_parameters.h"

const double R0               = MEMBERANCE_RADIUS;  // the radius of flat circle
const double R                = DOME_RADIUS;        // the radius of the dome
const double Theta            = FAN_SLICE_THETA;  // top angle of the fan slice
const int N                   = NUM_OF_SEGMENTS;  // number of segments
const double Mass_Time_factor = MASS_TIME_FACTOR;
// a line's movement is propotion to the factor, and segment width l0
// it includes dT, and mass etc.
const double K_Density = YOUNGS_MODULUS * 100;
// K of the spring const of unit
// width (cut line length) of the segment
// Both density uses the l0 before strech
// and unit length, longer spring K drops proportionally
// So the sagittal K will be K_Density / d0 * l0
// The tangential K is K_Density / l0 * d0
const double Friction_factor = FRICTION_FACTOR;
// the friction from outside air balloom pressure
const double Friction_motion_to_static_ratio = FRICTION_MOTION_TO_STATIC_RATIO;
const double Dome_Height                     = R - sqrt(R * R - R0 * R0);

struct cut_line {
    // This segment is the cut line between the segments
    double d;   // distance on sphere from the north pole
    double d0;  // original distance to the origin
    double l;   // current length of the line segment
    double l0;  // original length
};

cut_line c[N + 5];

double get_tangential_angle(const double d) {
    const double C = R - Dome_Height + d;
    double a = R0 * R0 + C * C, b = -2 * R0 * R, c = R * R - C * C;
    // double root1 = (-b + sqrt(b * b - 4 * a * c)) / 2 / a;
    double root2 = (-b - sqrt(b * b - 4 * a * c)) / 2 / a;
    // root1 is decrease with d decrease, which is wrong.
    return asin(root2);
}

double memberance_length(const double d) {
    double theta = (get_tangential_angle(d));
    double x1 = R * sin(theta), y1 = R * cos(theta);
    double x2 = R0, y2 = (R - Dome_Height) + d;
    double d1_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    return sqrt(d1_square) + theta * R;
}

// void test_angle_calc() {
//     for (double d = Dome_Height; d >= 0; d -= Dome_Height / 100) {
//         double theta = (get_tangential_angle(d));
//         double x1 = R * sin(theta), y1 = R * cos(theta);
//         double x2 = R0, y2 = (R - Dome_Height) + d;
//         double d1_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
//         double d2_square = x2 * x2 + (y2 * y2);
//         if (d2_square - d1_square - R * R > 1e-10) cout << "ERROR" << endl;
//         cout << theta << " ";
//     }
// }

double ring_radius(double d)  // radius of the ring slice,
                              // d is the distance on sphere surface from the
                              // north pole to the ring
{
    return sin(d / R) * R;
}

void init() {
    // cut line 0 is from the center point
    // cut lien N is a the fixed rim
    // first give value of the d0 and l0 as the flat circle
    // The memberance is above the dome
    for (int i = 0; i <= N; i++) {
        c[i].d = c[i].d0 = R0 / N * i;
        c[i].l = c[i].l0 = Theta * c[i].d0;
    }
}

double sagittal_stretch_force(const cut_line &c_top, const cut_line &c_bottom) {
    // return the sagittal force produced by the piece
    // between the two cut lines. The width use the bottom
    // cut line width
    double original_length = c_bottom.d0 - c_top.d0;
    double new_length      = c_bottom.d - c_top.d;
    double K               = K_Density / original_length * c_bottom.l0;
    if (new_length <= original_length)  // the spring won't give any push force
        return 0;
    return (new_length - original_length) * K;
}

double ring_stretch_force_on_sagittal(const cut_line &c_top,
                                      const cut_line &c_bottom) {
    // The portion of force from the ring of membrance stretched into a new size
    double original_length = (c_bottom.l0 + c_top.l0) / 2;
    // double new_center_d    = (c_bottom.d + c_top.d) / 2;
    double new_length = (c_bottom.l + c_top.l) / 2;
    double K          = K_Density / (c_bottom.d0 - c_top.d0) * original_length;
    if (new_length <= original_length)  // the spring won't give any push force
        return 0;
    return (new_length - original_length) * K * Theta;
    // The force has sin(Theta/2) portion in the sagittal direction each side
    // Since Theta is small, total is approximately Theta
}

double static_friction_sagittal(const cut_line &c1, const cut_line &c2,
                                const cut_line &c3) {
    // The c1 is the cut line above, c2 is self, c3 is the bottom one
    double width  = c2.l;  // Theta * ring_radius(c2.d);
    double height = (c3.d + c2.d) / 2 - (c1.d + c2.d) / 2;
    double area   = width * height;
    return abs(area * Friction_factor);
}

template <typename T>
int sgn(T val) {
    return (T(0) < val) - (val < T(0));
}

double move_pieces(const double memberance_height) {  // return the max movement
                                                      // from all pieces
    // Get the arc angle of the memberance already touching the dome
    const double alpha = get_tangential_angle(memberance_height);
    const double length_of_memberance_touching_dome = R * alpha;
    // Move the rim edge which is the c[N].d to the new position
    c[N].d = memberance_length(memberance_height);
    // Using c_old for previous stage, and updating c
    double max_move = 0;
    cut_line c_old[N + 5];
    memcpy(c_old, c, sizeof(cut_line) * (N + 5));
    //
    for (int i = 1; i < N; i++) {
        // If contacing the dome or not uses different models.
        bool contact_dome = c_old[i].d <= length_of_memberance_touching_dome;
        // The saggittal force only relates to the stretching and friction
        // no matter it's on dome or not
        double pull_force_from_top =
            sagittal_stretch_force(c_old[i - 1], c_old[i]) +
            ring_stretch_force_on_sagittal(c_old[i - 1], c_old[i]);
        double pull_force_from_bottom =
            sagittal_stretch_force(c_old[i], c_old[i + 1]) -
            ring_stretch_force_on_sagittal(c_old[i], c_old[i + 1]);
        double net_force_out_sagittal =
            pull_force_from_bottom - pull_force_from_top;
        if (contact_dome) {
            double static_friction =
                static_friction_sagittal(c[i - 1], c[i], c[i + 1]);
            if (static_friction >= abs(net_force_out_sagittal))
                net_force_out_sagittal = 0;
            else
                net_force_out_sagittal =
                    sgn(net_force_out_sagittal) *
                    (abs(net_force_out_sagittal) -
                     static_friction * Friction_motion_to_static_ratio);
        }
        // Move with force whose sign is + for out - for moving in
        double move = net_force_out_sagittal / c[i].l0 * Mass_Time_factor;
        max_move    = MAX(max_move, abs(move));
        c[i].d += move;
        // Cancel, if moves too much
        if (c[i].d <= c[i - 1].d or c[i].d >= c[i + 1].d) c[i].d = c_old[i].d;
        // Calculate the new l
        if (c[i].d <= length_of_memberance_touching_dome)
            c[i].l = Theta * ring_radius(c[i].d);
        else {
            double contact_rim_radius =
                ring_radius(length_of_memberance_touching_dome);
            double l_at_rim = contact_rim_radius * Theta;
            c[i].l          = (c[i].d - length_of_memberance_touching_dome) /
                         (c[N].d - length_of_memberance_touching_dome) *
                         (c[N].l0 - l_at_rim) +
                     l_at_rim;
        }
    }
    return max_move;
}

void print_c() {
    for (int i = 1; i < N; i++)
        printf("%f,", (c[i].d - c[i - 1].d) / (c[i].d0 - c[i - 1].d0));
    printf("%f\n", (c[N].d - c[N - 1].d) / (c[N].d0 - c[N - 1].d0));
    for (int i = 1; i < N; i++)
        printf("%f,", (c[i].l + c[i - 1].l) / (c[i].l0 + c[i - 1].l0));
    printf("%f\n", (c[N].l + c[N - 1].l) / (c[N].l0 + c[N - 1].l0));
    for (int i = 1; i < N; i++) printf("%f,", (c[i].d));
    printf("%f\n", (c[N].d));
}

int main() {
    init();
    // cout << "Dome degree: " << 2 * asin(R0 / R) / 2 / PI * 360 << endl;
    double d;
    int i;
    for (d = Dome_Height, i = 0; d >= 0;
         i++, d -= Dome_Height / PRESSING_STEPS) {
        while (1) {
            double max_move = move_pieces(d);
            // cout << max_move << endl;
            if (max_move < MOVE_THRESHOLD) break;
        }
        if (i % PRINT_EVERY_X_STEPS == 0) print_c();
    }
    print_c();
}
