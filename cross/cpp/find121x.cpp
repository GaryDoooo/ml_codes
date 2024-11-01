#include <algorithm>
#include <cmath>
#include <iostream>
#include <stack>
#include <vector>
/////// Own Modules ///////
#include "find9crossHairs.h"
#include "tiff_utilities.h"

using namespace std;

double getAngleToXAxis(double x, double y) {
    // Calculate the angle in radians
    double angleRadians = std::atan2(y, x);

    // Convert radians to degrees
    double angleDegrees = angleRadians * 180.0 / M_PI;

    // Ensure the angle is positive (0 to 360 degrees)
    if (angleDegrees < 0) {
        angleDegrees += 360.0;
    }
    if (angleDegrees > 350)
        angleDegrees = 360 - angleDegrees;
    return angleDegrees;
}

point crop_and_cross_hatch(int center_x, int center_y,
                           int cross_hatch_crop_half_with,
                           const vector<int>& imageData, int w, int h) {
    int x0 = center_x - cross_hatch_crop_half_with,
        y0 = center_y - cross_hatch_crop_half_with;
    int x1 = x0 + cross_hatch_crop_half_with * 2,
        y1 = y0 + cross_hatch_crop_half_with * 2;
    auto croppedData = cropImage(imageData, w, h, x0, y0, x1, y1);
    auto p = cross_hatch(croppedData, cross_hatch_crop_half_with * 2 + 1,
                         cross_hatch_crop_half_with * 2 + 1);
    p.x += x0;
    p.y += y0;
    return p;
}

struct node {
    point p;
    int good;
    int neighbor[4];
};
int inversed_direction[4] = {1, 0, 3, 2};
double min_d[4] = {-5, 175, 85, 265}; // in degree
double max_d[4] = {5, 185, 95, 275};
double deg[4] = {0, 90, 180, 270};
node nodes[1000];
int n_tail = 1, vis[500];
int max_neighbor_dis = 500;

int find_neighbor_in5degree(int start, int direction) {
    int res = 0;
    double min_dis = 1e8;
    int x0 = nodes[start].p.x, y0 = nodes[start].p.y;
    for (int i = 1; i < n_tail; i++) {
        if (i == start)
            continue;
        double deltaX = (double)(nodes[i].p.x - x0);
        double deltaY = (double)(nodes[i].p.y - y0);
        double angle = getAngleToXAxis((double)deltaX, (double)deltaY);
        if (angle < max_d[direction] and angle > min_d[direction]) {
            double dis = hypot(deltaX, deltaY);
            if (dis < min_dis) {
                min_dis = dis;
                res = i;
            }
        }
    }
    return res;
}

double get_dis(int n1, int n2) {
    return hypot((double)(nodes[n1].p.x - nodes[n2].p.x),
                 (double)(nodes[n1].p.y - nodes[n2].p.y));
}

point getCoordinates(double angleDegrees, double radius) {
    // Convert angle from degrees to radians
    double angleRadians = angleDegrees * M_PI / 180.0;

    // Calculate x and y
    point p;
    p.x = (int)(radius * std::cos(angleRadians));
    p.y = (int)(radius * std::sin(angleRadians));
    return p;
}

vector<point> find121crossHairs(const vector<int>& imageData, int w, int h,
                                int ratio = 10) {
    int newH, newW;
    auto imS = shrinkImageByAveraging(imageData, w, h, ratio, newW, newH);
    auto crosses = locate_cross(imS, newW, 15, .98, 6, 100);

    // Output the results
    vector<point> res;
    int cross_hatch_crop_half_with = 100;
    for (const auto& cross : crosses) {
        auto p =
            crop_and_cross_hatch(cross.x * ratio, cross.y * ratio,
                                 cross_hatch_crop_half_with, imageData, w, h);
        // cout << "Cross located at: (" << cross.x << ", " << cross.y << ")\n";
        res.push_back(p);
    }

    // add res points to nodes
    for (auto p : res)
        nodes[n_tail++].p = p;
    //     nodes[n_tail].x = p.x;
    //     nodes[n_tail++].y = p.y;
    // }

    // Fill all the neighbors in
    vector<double> all_dis[4];
    for (int i = 1; i < n_tail; i++)
        for (int d = 0; d < 4; d++) {
            int res = find_neighbor_in5degree(i, d);
            nodes[i].neighbor[d] = res;
            if (res > 0)
                all_dis[d].push_back(get_dis(res, i));
        }
    double median_dis[4];
    for (int d = 0; d < 4; d++) {
        sort(all_dis[d].begin(), all_dis[d].end());
        median_dis[d] = all_dis[d][all_dis[d].size() / 2];
        cout << median_dis[d] << " " << all_dis[d].size() << endl;
    }
    // return res;
    for (int i = 1; i < n_tail; i++)
        for (int d = 0; d < 4; d++) {
            int j = nodes[i].neighbor[d];
            if (j == 0)
                continue;
            double dis = get_dis(j, i);
            if (dis > median_dis[d] * 1.05 or dis < median_dis[d] * .95)
                nodes[i].neighbor[d] = 0;
        }

    // get the initial good points with four avaible neighbors
    for (int i = 1; i < n_tail; i++) {
        int cnt = 0;
        for (int d = 0; d < 4; d++)
            cnt += (nodes[i].neighbor[d] > 0);
        nodes[i].good = (cnt == 4);
    }

    // all good points' neighbors are good too
    for (int i = 1; i < n_tail; i++) {
        if (vis[i])
            continue;
        if (nodes[i].good) {
            stack<int> s;
            s.push(i);
            vis[i] = 1;
            while (s.size()) {
                int now = s.top();
                s.pop();
                for (int d = 0; d < 4; d++) {
                    int j = nodes[now].neighbor[d];
                    if (j > 0) {
                        if (vis[j] == 0) {
                            vis[j] = 1;
                            nodes[j].good = 1;
                            s.push(j);
                        }
                    } else {
                        auto dp = getCoordinates(deg[d], median_dis[d]);
                        int x = dp.x + nodes[now].p.x,
                            y = dp.y + nodes[now].p.y;
                        auto p = crop_and_cross_hatch(
                            x, y, cross_hatch_crop_half_with, imageData, w, h);
                        double deltaX = (double)(p.x - nodes[now].p.x);
                        double deltaY = (double)(p.y - nodes[now].p.y);
                        double angle =
                            getAngleToXAxis((double)deltaX, (double)deltaY);
                        if (angle < max_d[d] and angle > min_d[d]) {
                            double dis = hypot(deltaX, deltaY);
                            if (dis < median_dis[d] * 1.05 and
                                dis > median_dis[d] * .95) {
                                j = n_tail++;
                                nodes[j].p = p;
                                vis[j] = 1;
                                nodes[j].good = 1;
                                s.push(j);
                                for (int d = 0; d < 4; d++) {
                                    int res = find_neighbor_in5degree(j, d);
                                    if (nodes[res].good)
                                        nodes[j].neighbor[d] = res;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    res.clear();
    for (int i = 1; i < n_tail; i++)
        if (nodes[i].good)
            res.push_back(nodes[i].p);

    return res;
}

void output_image(vector<int>& imageData, int W, int H, vector<point>& points,
                  string output_filename = "output.tiff") {
    vector<unsigned char> output_image_data(W * H * 3);
    int max_value = *max_element(imageData.begin(), imageData.end());
    int min_value = *min_element(imageData.begin(), imageData.end());
    int step = (int)((double)(max_value - min_value) / 255);
    for (int i = 0; i < imageData.size(); i++) {
        unsigned char l =
            (unsigned char)clamp((imageData[i] - min_value) / step, 0, 255);
        int index = i * 3;
        output_image_data[index] = l;
        output_image_data[++index] = l;
        output_image_data[++index] = l;
    }
    int radius = 9;
    for (auto p : points) {
        for (int x = p.x - radius; x <= p.x + radius; x++)
            for (int y = p.y - radius; y <= p.y + radius; y++) {
                int index = (y * W + x) * 3;
                output_image_data[index] = 255;
                output_image_data[++index] = 0;
                output_image_data[++index] = 00;
            }
    }

    saveRGBTIFF(output_filename, output_image_data, W, H);
}

void output_image_x5(vector<int>& imageData, int W, int H,
                     vector<point>& points,
                     string output_filename = "output.tiff") {
    int newW, newH, ratio = 5;
    auto imS = shrinkImageByAveraging(imageData, W, H, ratio, newW, newH);
    vector<point> new_points;
    for (auto p : points) {
        point new_p;
        new_p.x = p.x / ratio;
        new_p.y = p.y / ratio;
        new_points.push_back(new_p);
    }
    output_image(imS, newW, newH, new_points, output_filename);
}

string removeBeforeLastSlash(const std::string& input) {
    size_t lastSlashPos = input.find_last_of('/');
    if (lastSlashPos != std::string::npos) {
        return input.substr(lastSlashPos + 2);
    }
    return input; // Return the original string if no '/' is found
}

int main() {
    int w, h;
    string filename;
    cin >> filename;

    vector<int> imageData_orig = read_tiff_file(filename.c_str(), w, h, 100);
    if (w == 0) {
        std::cerr << "Could not open the TIFF file." << std::endl;
        return -1;
    }

    vector<int> imageData = cropImage(imageData_orig, w, h, w / 10 * 2, h / 10,
                                      w / 10 * 8, h / 10 * 9);

    w = w / 10 * 6 + 1;
    h = h / 10 * 8 + 1;

    vector<point> res = find121crossHairs(imageData, w, h);
    for (auto p : res)
        cout << "Locate center again at (" << p.x + w / 3 << "," << p.y + h / 8
             << ")\n";

    output_image_x5(imageData, w, h, res,
                    "output" + removeBeforeLastSlash(filename));

    return 0;
}
