#include <bits/stdc++.h>
/////// Own Modules ///////
#include "tiff_utilities.h"

using namespace std;

vector<int> rangeByX(const vector<int> &image, int width, int height,
                     int &newWidth, int &newHeight, int X) {
    newWidth  = width - X;
    newHeight = height - X;
    vector<int> res(newWidth * newHeight);
    for (int y = 0; y < newHeight; y++)
        for (int x = 0; x < newWidth; x++) {
            int min_v = 1e8, max_v = 0;
            for (int yy = y; yy < y + X; yy++)
                for (int xx = x; xx < x + X; xx++) {
                    min_v = min(image[yy * width + xx], min_v);
                    max_v = max(image[yy * width + xx], max_v);
                }
            res[y * newWidth + x] = max_v - min_v;
            // if (max_v < min_v) {
            //     cout << x << "," << y << endl;
            // }
        }
    return res;
}

long long rec_sum(const vector<long long> &im, int x0, int y0, int x1, int y1,
                  int W) {
    long long current   = im[y1 * W + x1];
    long long above     = (y0 > 0) ? im[(y0 - 1) * W + x1] : 0;
    long long left      = (x0 > 0) ? im[y1 * W + (x0 - 1)] : 0;
    long long aboveLeft = (x0 > 0 && y0 > 0) ? im[(y0 - 1) * W + (x0 - 1)] : 0;
    long long res       = current - above - left + aboveLeft;
    if (res < 0) {
        cout << current << " " << above << " " << left << " "
             << " " << aboveLeft << " " << res << endl;
    }
    return res;
}

vector<long long> applyMask(
    const vector<long long> &im,  // 2D pre sum
    int W, int H, int &newW, int &newH,
    int width,  // the base square edge length
    int x0,
    int y0,  // the upper left corner of the rec to remove
    int x1,
    int y1  // the lower right corner of the rec to remove
) {
    newW = W - width;
    newH = H - width;
    vector<long long> res(newW * newH);
    for (int y = 0; y < newH; y++)
        for (int x = 0; x < newW; x++)
            res[y * newW + x] = rec_sum(im, x, y, x + width, y + width, W) -
                                rec_sum(im, x + x0, y + y0, x + x1, y + y1, W);
    return res;
}

vector<pair<int, int>> find_islands(const vector<long long> &im, int W, int H,
                                    float percentile, int count) {
    // Calculate the threshold
    vector<long long> flat_sc(im);
    sort(flat_sc.begin(), flat_sc.end());
    int thd = flat_sc[static_cast<int>(percentile / 100 * flat_sc.size())];

    vector<tuple<long long, int, int>> fsc;
    for (int y = 0; y < H; ++y) {
        for (int x = 0; x < W; ++x) {
            fsc.emplace_back(im[y * W + x], x, y);
        }
    }
    sort(fsc.begin(), fsc.end());
    cout << thd << endl;
    printf("%lld\n", fsc[fsc.size() - 1, 0]);

    vector<vector<int>> vis(H + 1, vector<int>(W + 1, 0));
    int idx        = fsc.size() - 1;
    int cnt        = 0;
    vector<int> dx = {-1, 0, 0, 1};
    vector<int> dy = {0, 1, -1, 0};
    while (cnt < count) {
        while (true) {
            auto [_, x, y] = fsc[idx];
            if (vis[y][x] == 0) {
                break;
            }
            idx--;
        }
        stack<pair<int, int>> stk;
        stk.push(make_pair(get<1>(fsc[idx]), get<2>(fsc[idx])));
        cnt++;
        while (!stk.empty()) {
            auto [x, y] = stk.top();
            stk.pop();
            vis[y][x] = cnt;
            for (int i = 0; i < 4; ++i) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                if (vis[yy][xx] == 0 && im[yy * W + xx] > thd) {
                    stk.push(make_pair(xx, yy));
                    vis[yy][xx] = cnt;
                }
            }
        }
    }
    // return;
    vector<vector<pair<int, int>>> blks(count);
    for (int y = 1; y < H; ++y) {
        for (int x = 1; x < W; ++x) {
            if (vis[y][x] > 0) {
                blks[vis[y][x] - 1].emplace_back(x, y);
            }
        }
    }

    // Output the blocks
    vector<pair<int, int>> res;
    for (int i = 0; i < count; ++i) {
        cout << "Block " << i + 1 << ":\n";
        if (!blks[i].empty()) {
            long long avg_x = 0, avg_y = 0;
            for (const auto &[x, y] : blks[i]) {
                avg_x += x;
                avg_y += y;
            }
            avg_x /= blks[i].size();
            avg_y /= blks[i].size();

            cout << "Block " << i + 1 << " average: ";
            cout << "(" << fixed << setprecision(2) << avg_x << ", " << avg_y
                 << ")\n";
            res.push_back(make_pair(avg_x, avg_y));
        } else {
            cout << "Block " << i + 1 << " is empty\n";
        }
    }

    // return 0;
}

// void print_out(const vector<int> &p, int W, int H) {
//     for (int y = 0; y < 50; y++) {
//         for (int x = 0; x < 50; x++) printf("%.2f ", p[W * y + x]);
//         puts("");
//     }
// }

pair<int, int> upper_corner(const vector<int> &im, int W, int H) {
    int WR, HR, WAM, HAM;
    vector<int> imR        = rangeByX(im, W, H, WR, HR, 3);
    vector<long long> imPS = compute2DPrefixSum(imR, WR, HR);
    //
    vector<long long> imAM =
        applyMask(imPS, WR, HR, WAM, HAM, 10, 2, 2, 10, 10);
    // print_out(imAM, WAM, HAM);
    vector<pair<int, int>> res = find_islands(imAM, WAM, HAM, 0.99f, 1);

    if (res.size() > 0) return res[0];
    return make_pair(0, 0);
}

int main() {
    int w = 0, h = 0;
    vector<int> imageData = read_tiff_file("1.tif", w, h);
    if (w == 0) {
        std::cerr << "Could not open the TIFF file." << std::endl;
        return -1;
    }

    // Get an image shrunk by 8 to a smaller image
    int ws = 0, hs = 0;
    vector<int> imageS = shrinkImageByAveraging(imageData, w, h, 8, ws, hs);

    pair<int, int> ul = upper_corner(imageS, ws, hs);

    return 0;
}

