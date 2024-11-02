#include <algorithm>
#include <iostream>
#include <numeric>
#include <stack>
#include <vector>
/////// Own Modules ///////
#include "tiff_utilities.h"

using namespace std;

struct point {
    int x, y;
};

bool point_cmp_x(const point& a, const point& b) { return a.x < b.x; }

bool point_cmp_y(const point& a, const point& b) { return a.y < b.y; }

long long rec_sum(int x1, int y1, int x2, int y2,
                  const vector<vector<long long>>& s) {
    return s[y2][x2] - s[y1 - 1][x2] - s[y2][x1 - 1] + s[y1 - 1][x1 - 1];
}

vector<point> locate_cross(const vector<int>& data, int width, int c_size = 31,
                           double thd_quantile = 0.98, int c_corner = 10,
                           int cross_cnt = 9) {
    int H = data.size() / width;
    int W = width;

    // Convert input data to a 2D array
    vector<vector<int>> a(H, vector<int>(W));
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            a[i][j] = static_cast<int>(
                data[i * width + j]); // Convert to long long for calculations
        }
    }

    vector<vector<long long>> s(H + 1, vector<long long>(W + 1, 0));
    vector<long long> s1(W + 1, 0);

    for (int y = 0; y < H; ++y) {
        for (int x = 0; x < W; ++x) {
            s1[x + 1] = s1[x] + a[y][x];
            s[y + 1][x + 1] = s1[x + 1] + s[y][x + 1];
        }
    }

    c_size -= 1;
    c_corner -= 1;

    vector<vector<long long>> sc(s.size(), vector<long long>(s[0].size(), 0));

    for (int y = 1; y < H - c_size; ++y) {
        for (int x = 1; x < W - c_size; ++x) {
            int x2 = x + c_size;
            int y2 = y + c_size;
            long long res = rec_sum(x, y, x2, y2, s);
            res -= rec_sum(x, y, x + c_corner, y + c_corner, s);
            res -= rec_sum(x2 - c_corner, y, x2, y + c_corner, s);
            res -= rec_sum(x, y2 - c_corner, x + c_corner, y2, s);
            res -= rec_sum(x2 - c_corner, y2 - c_corner, x2, y2, s);
            sc[y][x] = res;
        }
    }

    // vector<long long> flat_sc;
    // for (int y = 1; y < H; ++y) {
    //     for (int x = 1; x < W; ++x) {
    //         flat_sc.push_back(sc[y][x]);
    //     }
    // }
    //
    // sort(flat_sc.begin(), flat_sc.end());
    // long long thd = flat_sc[(int)(flat_sc.size() * thd_quantile)];

    vector<tuple<long long, int, int>> fsc;
    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            fsc.emplace_back(sc[y][x], x, y);
        }
    }

    sort(fsc.begin(), fsc.end());

    long long thd = get<0>(fsc[(int)(fsc.size() * thd_quantile)]);
    vector<vector<int>> vis(s.size(), vector<int>(s[0].size(), 0));
    int idx = fsc.size() - 1;
    int cnt = 0;

    vector<int> dx{-1, 0, 0, 1};
    vector<int> dy{0, 1, -1, 0};

    while (cnt < cross_cnt) {
        while (true) {
            auto [_, x, y] = fsc[idx];
            if (vis[y][x] == 0) {
                break;
            }
            idx--;
        }

        stack<pair<int, int>> stack;
        // stack.push({fsc[idx].get<1>(), fsc[idx].get<2>()});
        stack.push(make_pair(get<1>(fsc[idx]), get<2>(fsc[idx])));
        cnt++;

        while (!stack.empty()) {
            auto [x, y] = stack.top();
            stack.pop();
            vis[y][x] = cnt;

            for (int i = 0; i < dx.size(); ++i) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                if (vis[yy][xx] == 0 && sc[yy][xx] > thd) {
                    stack.push({xx, yy});
                    vis[yy][xx] = cnt;
                }
            }
        }
    }

    vector<vector<pair<int, int>>> blks(cross_cnt);

    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            if (vis[y][x] > 0) {
                blks[vis[y][x] - 1].emplace_back(x, y);
            }
        }
    }

    vector<point> res(cross_cnt);
    for (size_t i = 0; i < blks.size(); ++i) {
        if (!blks[i].empty()) {
            long long sum_x = accumulate(
                blks[i].begin(), blks[i].end(), static_cast<long long>(0),
                [](long long acc, const pair<int, int>& p) {
                    return acc + p.first;
                });

            long long sum_y = accumulate(
                blks[i].begin(), blks[i].end(), static_cast<long long>(0),
                [](long long acc, const pair<int, int>& p) {
                    return acc + p.second;
                });

            res[i].x =
                static_cast<int>(sum_x / blks[i].size() + c_size / 2) - 1;
            res[i].y =
                static_cast<int>(sum_y / blks[i].size() + c_size / 2) - 1;
        }
    }
    sort(res.begin(), res.end(), point_cmp_y);
    sort(res.begin(), res.begin() + 3, point_cmp_x);
    sort(res.begin() + 3, res.begin() + 6, point_cmp_x);
    sort(res.begin() + 6, res.end(), point_cmp_x);

    return res;
}

// Function to calculate the coefficients A, B, and C for a line given two
// points
std::tuple<double, double, double>
calculateLineCoefficients(double x1, double y1, double x2, double y2) {
    double A = y2 - y1;               // Coefficient for x
    double B = x1 - x2;               // Coefficient for y
    double C = (x2 * y1) - (x1 * y2); // Constant term

    return std::make_tuple(A, B, C);
}

// Function to find the intersection of two lines using tuples for coefficients
std::tuple<double, double>
findIntersection(const std::tuple<double, double, double>& line1,
                 const std::tuple<double, double, double>& line2) {
    double A1 = std::get<0>(line1);
    double B1 = std::get<1>(line1);
    double C1 = std::get<2>(line1);

    double A2 = std::get<0>(line2);
    double B2 = std::get<1>(line2);
    double C2 = std::get<2>(line2);

    // Calculate the determinant
    double determinant = (A1 * B2) - (A2 * B1);
    double x = 1e9, y = 1e9;
    if (determinant == 0) {
        cout << "lines parallel" << endl;

        // throw std::runtime_error(
        //     "The lines are parallel and do not intersect.");
    }

    // Calculate intersection point
    x = (B1 * C2 - B2 * C1) / determinant;
    y = (C1 * A2 - C2 * A1) / determinant;

    return std::make_tuple(x, y);
}

point cross_hatch(const vector<int>& im, int W, int H, int step = 10) {
    struct Cross_Section {
        vector<int> data;
        int y, FWHM, max_value, max_idx;
    };
    auto max_it = max_element(im.begin(), im.end());
    auto thd = (*max_it) / 10;
    vector<Cross_Section> cross_sections;
    for (int y = 0; y < H; y += step) {
        Cross_Section tmp;
        tmp.y = y;
        tmp.max_value = 0;
        for (int x = 0; x < W; x++) {
            tmp.data.push_back(im[W * y + x]);
            if (tmp.data.back() > tmp.max_value) {
                tmp.max_value = tmp.data.back();
                tmp.max_idx = tmp.data.size() - 1;
            }
        }
        if (tmp.max_value < thd)
            continue;
        // cout << "get cross section at y=" << y
        //      << " with max value = " << tmp.max_value << " at idx "
        //      << tmp.max_idx;
        // int left, right;
        // for (left = tmp.max_idx;
        //      left >= 0 and tmp.data[left] >= tmp.max_value / 2; left--)
        //     ;
        // for (right = tmp.max_idx;
        //      right < tmp.data.size() and tmp.data[right] >= tmp.max_value /
        //      2; right++)
        //     ;
        // // cout << " FWHM = " << right - left << endl;
        // tmp.FWHM = right - left;
        cross_sections.push_back(tmp);
    }
    auto vertical_line = calculateLineCoefficients(
        cross_sections[1].max_idx, cross_sections[1].y,
        cross_sections[cross_sections.size() - 2].max_idx,
        cross_sections[cross_sections.size() - 2].y);

    vector<Cross_Section> cross_sections2;
    for (int x = 0; x < W; x += step) {
        Cross_Section tmp;
        tmp.y = x;
        tmp.max_value = 0;
        for (int y = 0; y < H; y++) {
            tmp.data.push_back(im[W * y + x]);
            if (tmp.data.back() > tmp.max_value) {
                tmp.max_value = tmp.data.back();
                tmp.max_idx = tmp.data.size() - 1;
            }
        }
        if (tmp.max_value < thd)
            continue;
        // cout << "get cross section at y=" << y
        //      << " with max value = " << max_value;
        // cout << "get cross section at x=" << x
        //      << " with max value = " << tmp.max_value << " at idx "
        //      << tmp.max_idx;
        // int left, right;
        // for (left = tmp.max_idx;
        //      left >= 0 and tmp.data[left] >= tmp.max_value / 2; left--)
        //     ;
        // for (right = tmp.max_idx;
        //      right < tmp.data.size() and tmp.data[right] >= tmp.max_value /
        //      2; right++)
        //     ;
        // // cout << " FWHM = " << right - left << endl;
        // tmp.FWHM = right - left;
        cross_sections2.push_back(tmp);
    }

    auto horizontal_line = calculateLineCoefficients(
        cross_sections2[1].y, cross_sections2[1].max_idx,
        cross_sections2[cross_sections2.size() - 2].y,
        cross_sections2[cross_sections2.size() - 2].max_idx);

    auto intersect = findIntersection(horizontal_line, vertical_line);
    point res;
    res.x = (int)get<0>(intersect);
    res.y = (int)get<1>(intersect);
    // cout << res.x << "," << res.y << endl;
    return res;
}

vector<point> find9crossHairs(const vector<int>& imageData, int w, int h,
                              int ratio = 10) {
    int newH, newW;
    auto imS = shrinkImageByAveraging(imageData, w, h, ratio, newW, newH);
    auto crosses = locate_cross(imS, newW, 15, .98, 5, 9);

    // auto crosses = locate_cross(imageData, w);
    // Output the results
    vector<point> res;
    for (const auto& cross : crosses) {
        cout << "Cross located at: (" << cross.x << ", " << cross.y << ")\n";
        int x0 = cross.x * ratio - 200, y0 = cross.y * ratio - 200;
        int x1 = x0 + 400, y1 = y0 + 400;
        auto croppedData = cropImage(imageData, w, h, x0, y0, x1, y1);
        auto p = cross_hatch(croppedData, 401, 401);
        p.x += x0;
        p.y += y0;
        res.push_back(p);
    }
    return res;
}

