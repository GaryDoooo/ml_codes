#include <bits/stdc++.h>
/////// Own Modules ///////
#include "tiff_utilities.h"

using namespace std;

struct point {
    int x, y;
};

int ManhattanDis(int x, int y, int x0, int y0) {
    return abs(x - x0) + abs(y - y0);
}

point farthest_ManDis(vector<point>& ps, int x0, int y0) {
    int mdis = 0;
    point p1;
    for (auto p : ps) {
        int md = ManhattanDis(p.x, p.y, x0, y0);
        if (md > mdis) {
            mdis = md;
            p1.x = p.x;
            p1.y = p.y;
        }
    }
    return p1;
}

vector<point> get_EWNS_from_ctr(vector<int>& im, int width, int height) {  //,
    // int& east, int& west, int& north, int& th) {
    vector<vector<int>> vis(height, vector<int>(width, 0));
    stack<point> stk;
    int x0 = width / 2, y0 = height / 2;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    stk.push({x0, y0});
    // int thd = im[x0 + y0 * width] / 10;
    auto maxElementIterator = max_element(im.begin(), im.end());
    int thd                 = (*maxElementIterator) / 10;
    // east = west = x0;
    // north = south = y0;
    vis[y0][x0] = 1;
    vector<point> res;
    while (!stk.empty()) {
        auto [x, y] = stk.top();
        stk.pop();
        int apex = 1, mdis = ManhattanDis(x, y, x0, y0);
        for (int i = 0; i < 4; i++) {
            int new_x = x + dx[i], new_y = y + dy[i];
            if (new_x < 0 or new_y < 0 or new_x >= width or new_y >= height)
                continue;
            if (im[new_y * width + new_x] < thd) continue;
            if (ManhattanDis(new_x, new_y, x0, y0) > mdis) apex = 0;
            if (vis[new_y][new_x]) continue;
            vis[new_y][new_x] = 1;
            stk.push({new_x, new_y});
            // east  = max(east, new_x);
            // west  = min(west, new_x);
            // north = min(north, new_y);
            // south = max(south, new_y);
        }
        if (apex) {
            res.push_back({x, y});
            // cout << res.size() << " ";
        }
    }
    return res;
}

// Function to calculate the distance from a point to a line
double distanceToLine(const point& p, const point& lineStart,
                      const point& lineEnd) {
    // Line equation: Ax + By + C = 0
    double A = (double)lineEnd.y - (double)lineStart.y;
    double B = (double)lineStart.x - (double)lineEnd.x;
    double C = (double)lineEnd.x * (double)lineStart.y -
               (double)lineStart.x * (double)lineEnd.y;

    // Calculate the distance
    return std::abs(A * (double)p.x + B * (double)p.y + C) /
           std::sqrt(A * A + B * B);
}

// Function to find the point with the largest distance from the line
point findFarthestPoint(const std::vector<point>& points,
                        const point& lineStart, const point& lineEnd) {
    double maxDistance = -std::numeric_limits<double>::infinity();
    point farthestPoint;

    for (const auto& p : points) {
        double dist = distanceToLine(p, lineStart, lineEnd);
        if (dist > maxDistance) {
            maxDistance   = dist;
            farthestPoint = p;
        }
    }

    return farthestPoint;
}

// Function to calculate the centroid of the points
point calculateCentroid(const std::vector<point>& points) {
    point centroid = {0, 0};
    for (const auto& p : points) {
        centroid.x += p.x;
        centroid.y += p.y;
    }
    centroid.x /= points.size();
    centroid.y /= points.size();
    return centroid;
}

// Function to sort points into upper left, upper right, lower right, lower left
std::vector<point> sortPoints(const std::vector<point>& points) {
    std::vector<point> sortedPoints = points;
    point centroid                  = calculateCentroid(points);

    // Sort points based on their angle relative to the centroid
    std::sort(sortedPoints.begin(), sortedPoints.end(),
              [&](const point& a, const point& b) {
                  if (a.y < centroid.y && b.y >= centroid.y) return true;
                  if (a.y >= centroid.y && b.y < centroid.y) return false;
                  if (a.y < centroid.y && b.y < centroid.y) return a.x < b.x;
                  if (a.y >= centroid.y && b.y >= centroid.y) return a.x > b.x;
                  return false;
              });

    return sortedPoints;
}

vector<point> find4corners(vector<int>& imageData, int width, int height) {
    int w = width, h = height;
    vector<point> aps = get_EWNS_from_ctr(imageData, w, h);  //, E, W, N, S);
    cout << "Found apexes total: " << aps.size() << endl;
    // Find the one has biggest Manhattan distance to the w/2,h/2
    // Must be one apex
    point p1 = farthest_ManDis(aps, w / 2, h / 2);
    // Find the one has largest Manhattan distance to p1, also an apex too
    point p2 = farthest_ManDis(aps, p1.x, p1.y);
    // Find the one has largest distance to the line connecting p1 and p2
    point p3 = findFarthestPoint(aps, p1, p2);
    // Find the one has largest distance to the third point
    point p4             = farthest_ManDis(aps, p3.x, p3.y);
    vector<point> points = {p1, p2, p3, p4};
    // Sort the points
    // << "Sorted points (upper left, upper right, lower right, lower left):"
    vector<point> sortedPoints = sortPoints(points);
    return sortedPoints;
}

int main() {
    int w = 0, h = 0;
    string filename;
    cin>>filename;
    vector<int> imageData = read_tiff_file(filename.c_str(), w, h, 1);
    if (w == 0) {
        std::cerr << "Could not open the TIFF file." << std::endl;
        return -1;
    }

    vector<point> sortedPoints = find4corners(imageData, w, h);
    // Output the sorted points
    std::cout
        << "Sorted points (upper left, upper right, lower right, lower left):"
        << std::endl;
    for (const auto& p : sortedPoints) {
        std::cout << "" << p.x << "," << p.y << "" << std::endl;
    }

    return 0;
}

