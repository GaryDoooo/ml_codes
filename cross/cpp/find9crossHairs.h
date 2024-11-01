#include <vector>
#pragma once

struct point {
    int x, y;
};

std::vector<point> find9crossHairs(const std::vector<int>& imageData, int w,
                                   int h, int ratio = 10);

point cross_hatch(const std::vector<int>& im, int W, int H,
                  int step = 10); // {
                                  // struct Cross_Section {

std::vector<point> locate_cross(const std::vector<int>& data, int width,
                                int c_size = 31, double thd_quantile = 0.98,
                                int c_corner = 10,
                                int cross_cnt = 9); // {
