#include <bits/stdc++.h>
#include <png.h>
#include <iostream>
#include <vector>
using namespace std;

std::vector<unsigned char> readPNGFile(const char* filename, int& width,
                                       int& height) {
    FILE* fp = fopen(filename, "rb");
    if (!fp) {
        throw std::runtime_error("Failed to open file");
    }

    png_structp png = png_create_read_struct(PNG_LIBPNG_VER_STRING, nullptr,
                                             nullptr, nullptr);
    if (!png) {
        fclose(fp);
        throw std::runtime_error("Failed to create PNG read struct");
    }

    png_infop info = png_create_info_struct(png);
    if (!info) {
        png_destroy_read_struct(&png, nullptr, nullptr);
        fclose(fp);
        throw std::runtime_error("Failed to create PNG info struct");
    }

    if (setjmp(png_jmpbuf(png))) {
        png_destroy_read_struct(&png, &info, nullptr);
        fclose(fp);
        throw std::runtime_error("Error reading PNG file");
    }

    png_init_io(png, fp);
    png_read_info(png, info);

    width               = png_get_image_width(png, info);
    height              = png_get_image_height(png, info);
    png_byte color_type = png_get_color_type(png, info);
    png_byte bit_depth  = png_get_bit_depth(png, info);

    if (bit_depth == 16) {
        png_set_strip_16(png);
    }

    if (color_type == PNG_COLOR_TYPE_PALETTE) {
        png_set_palette_to_rgb(png);
    }

    if (color_type == PNG_COLOR_TYPE_GRAY && bit_depth < 8) {
        png_set_expand_gray_1_2_4_to_8(png);
    }

    if (png_get_valid(png, info, PNG_INFO_tRNS)) {
        png_set_tRNS_to_alpha(png);
    }

    if (color_type == PNG_COLOR_TYPE_RGB || color_type == PNG_COLOR_TYPE_GRAY ||
        color_type == PNG_COLOR_TYPE_PALETTE) {
        png_set_filler(png, 0xFF, PNG_FILLER_AFTER);
    }

    if (color_type == PNG_COLOR_TYPE_GRAY ||
        color_type == PNG_COLOR_TYPE_GRAY_ALPHA) {
        png_set_gray_to_rgb(png);
    }

    png_read_update_info(png, info);

    std::vector<png_bytep> row_pointers(height);
    std::vector<unsigned char> image_data(width * height * 4);

    for (int y = 0; y < height; y++) {
        row_pointers[y] = &image_data[y * width * 4];
    }

    png_read_image(png, row_pointers.data());

    fclose(fp);
    png_destroy_read_struct(&png, &info, nullptr);

    return image_data;
}

// Function to calculate the prefix sum array
void calculatePrefixSum(const vector<vector<double>>& a, vector<vector<double>>& s) {
    int H = a.size();
    int W = a[0].size();
    vector<double> s1(W + 1, 0.0);

    for (int y = 0; y < H; ++y) {
        for (int x = 0; x < W; ++x) {
            s1[x + 1] = s1[x] + a[y][x];
            s[y + 1][x + 1] = s1[x + 1] + s[y][x + 1];
        }
    }
}

// Function to calculate the sum of a submatrix
double rec_sum(const vector<vector<double>>& s, int x1, int y1, int x2, int y2) {
    return s[y2][x2] - s[y1 - 1][x2] - s[y2][x1 - 1] + s[y1 - 1][x1 - 1];
}

int find9cross(vector<vector<double>> &a) {
    int H = a.size();
    int W = a[0].size();

    vector<vector<double>> s(H + 1, vector<double>(W + 1, 0.0));
    calculatePrefixSum(a, s);

    // Define the cross window
    int c_size = 15 - 1;
    int c_corner = 5 - 1;

    vector<vector<double>> sc(H + 1, vector<double>(W + 1, 0.0));

    for (int y = 1; y < H - c_size; ++y) {
        for (int x = 1; x < W - c_size; ++x) {
            int x2 = x + c_size;
            int y2 = y + c_size;
            double res = rec_sum(s, x, y, x2, y2);
            res -= rec_sum(s, x, y, x + c_corner, y + c_corner);
            res -= rec_sum(s, x2 - c_corner, y, x2, y + c_corner);
            res -= rec_sum(s, x, y2 - c_corner, x + c_corner, y2);
            res -= rec_sum(s, x2 - c_corner, y2 - c_corner, x2, y2);
            sc[y][x] = res;
        }
    }

    // Calculate the threshold
    vector<double> flat_sc;
    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            flat_sc.push_back(sc[y][x]);
        }
    }
    sort(flat_sc.begin(), flat_sc.end());
    double thd = flat_sc[static_cast<int>(0.98 * flat_sc.size())];

    vector<tuple<double, int, int>> fsc;
    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            fsc.emplace_back(sc[y][x], x, y);
        }
    }
    sort(fsc.begin(), fsc.end());

    vector<vector<int>> vis(H + 1, vector<int>(W + 1, 0));
    int idx = fsc.size() - 1;
    int cnt = 0;
    vector<int> dx = {-1, 0, 0, 1};
    vector<int> dy = {0, 1, -1, 0};

    while (cnt < 9) {
        while (true) {
            auto [_, x, y] = fsc[idx];
            if (vis[y][x] == 0) {
                break;
            }
            idx--;
        }
        vector<pair<int, int>> stack = {{get<1>(fsc[idx]), get<2>(fsc[idx])}};
        cnt++;
        while (!stack.empty()) {
            auto [x, y] = stack.back();
            stack.pop_back();
            vis[y][x] = cnt;
            for (int i = 0; i < 4; ++i) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                if (vis[yy][xx] == 0 && sc[yy][xx] > thd) {
                    stack.emplace_back(xx, yy);
                }
            }
        }
    }

    vector<vector<pair<int, int>>> blks(9);
    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            if (vis[y][x] > 0) {
                blks[vis[y][x] - 1].emplace_back(x, y);
            }
        }
    }

    // Output the blocks
    for (int i = 0; i < 9; ++i) {
        cout << "Block " << i + 1 << ":\n";
        for (const auto& [x, y] : blks[i]) {
            cout << "(" << x << ", " << y << ")\n";
        }
    }

    return 0;
}

int main() {
    string filename;
    cin >> filename;
    cout << "Got filename: " << filename << endl;
    if (filename.size() == 0) return 1;
    int width, height;
    vector<unsigned char> image_data;

    try {
        image_data = readPNGFile(filename.c_str(), width, height);
        std::cout << "Image size: " << width << "x" << height << std::endl;
        std::cout << "Image data size: " << image_data.size() << " bytes"
                  << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    // Each pixel is represented by 4 bytes (RGBA)
    // For example, to access the red component of the pixel at (x, y):
    // unsigned char red = image_data[(y * width + x) * 4];

    int a[height + 5][width + 5];
    for (y = 0; y < height; y++)
        for (x = 0; x < width; x++) {
            int pos = y * width + x;
            a[y][x] =
                image_data[pos] + image_data[pos + 1] + image_data[pos + 2];
        }

    return 0;
}

