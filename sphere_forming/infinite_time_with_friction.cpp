#define PI 3.14159265358979323846
#include <bits/stdc++.h>
using namespace std;
/*
 * Having a round pc of memberance with parimeter fixed
 * and center part can be streched.
 * Radius = 1
 * Get a thin slice of sector of the arc theta = 0.01
 * chop the slice along the radius into 100 segments
 */
const double R0               = 1;     // the radius of flat circle
const double R                = 3;     // the radius of the dome
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

struct cut_line {
    // This segment is the cut line between the segments
    double d;   // distance on sphere from the north pole
    double d0;  // original distance to the origin
    // double l;   // current length of the line segment
    double l0;  // original length
};

cut_line c[N + 5];

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
    for (int i = 0; i <= N; i++) {
        c[i].d0 = R0 / N * i;
        c[i].l0 = Theta * c[i].d0;
    }
    // put the memberance on the dome and give the d with even distribution
    // first
    double half_arc_len = asin(R0 / R) * R;
    for (int i = 0; i <= N; i++) {
        c[i].d = half_arc_len / N * i;
        // c[i].l = Theta * ring_radius(c[i].d);
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
    double new_center_d    = (c_bottom.d + c_top.d) / 2;
    double new_length      = Theta * ring_radius(new_center_d);
    double K = K_Density / (c_bottom.d0 - c_top.d0) * original_length;
    if (new_length <= original_length)  // the spring won't give any push force
        return 0;
    return (new_length - original_length) * K * Theta;
    // The force has sin(Theta/2) portion in the sagittal direction each side
    // Since Theta is small, total is approximately Theta
}

double static_friction_sagittal(const cut_line &c1, const cut_line &c2,
                                const cut_line &c3) {
    // The c1 is the cut line above, c2 is self, c3 is the bottom one
    double width  = Theta * ring_radius(c2.d);
    double height = (c3.d + c2.d) / 2 - (c1.d + c2.d) / 2;
    double area   = width * height;
    return area * Friction_factor;
}

double move_pieces() {  // return the max movement from all pieces
    double max_move = 0;
    cut_line c_old[N + 5];
    memcpy(c_old, c, sizeof(cut_line) * (N + 5));
    for (int i = 1; i < N; i++) {
        double pull_force_from_top =
            sagittal_stretch_force(c_old[i - 1], c_old[i]) +
            ring_stretch_force_on_sagittal(c_old[i - 1], c_old[i]);
        double pull_force_from_bottom =
            sagittal_stretch_force(c_old[i], c_old[i + 1]) -
            ring_stretch_force_on_sagittal(c_old[i], c_old[i + 1]);
        double net_force_out_sagittal =
            pull_force_from_bottom - pull_force_from_top;
        double static_friction =
            static_friction_sagittal(c[i - 1], c[i], c[i + 1]);
        double move;
        if (static_friction >= abs(net_force_out_sagittal))
            move = 0;
        else
            move = (net_force_out_sagittal -
                    static_friction * Friction_motion_to_static_ratio) /
                   c[i].l0 * Mass_Time_factor;
        max_move = max(max_move, abs(move));
        c[i].d += move;
        if (c[i].d <= 0 or c[i].d >= c[N].d) c[i].d = c_old[i].d;
    }
    return max_move;
}

// int main() {
//     init();
//     cout << "Dome degree: " << 2 * asin(R0 / R) / 2 / PI * 360 << endl;
//     while (1) {
//         double max_move = move_pieces();
//         // cout << max_move << endl;
//         if (max_move < 1e-10) break;
//     }
//     for (int i = 1; i <= N; i++)
//         cout << (c[i].d - c[i - 1].d) / (c[i].d0 - c[i - 1].d0) << " ";
// }
void print_c() {
    for (int i = 1; i < N; i++)
        printf("%f,", (c[i].d - c[i - 1].d) / (c[i].d0 - c[i - 1].d0));
    printf("%f\n", (c[N].d - c[N - 1].d) / (c[N].d0 - c[N - 1].d0));
}

int main() {
    init();
    cout << "Dome degree: " << 2 * asin(R0 / R) / 2 / PI * 360 << endl;
    int cnt = 0;
    while (1) {
        double max_move = move_pieces();
        if (++cnt % 100 == 0) print_c();
        // cout << max_move << endl;
        if (max_move < 1e-10) break;
    }
    // for (int i = 1; i <= N; i++)
    //     cout << (c[i].d - c[i - 1].d) / (c[i].d0 - c[i - 1].d0) << " ";
}
