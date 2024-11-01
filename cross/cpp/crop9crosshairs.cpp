#include <algorithm>
#include <iostream>
#include <vector>
/////// Own Modules ///////
#include "find9crossHairs.h"
#include "tiff_utilities.h"

using namespace std;

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

    vector<point> res = find9crossHairs(imageData, w, h, 10);
    for (auto p : res)
        cout << "Locate center again at (" << p.x + w / 3 << "," << p.y + h / 8
             << ")\n";

    // vector<int> imageCP(imageData.begin(), imageData.end());
    // sort(imageCP.begin(), imageCP.end());
    // int min_value = imageCP[(int)((float)imageCP.size() * 0.0001f)];
    // int max_value = imageCP[(int)((float)imageCP.size() * 0.9999f)];
    int max_value = *max_element(imageData.begin(), imageData.end());
    int min_value = *min_element(imageData.begin(), imageData.end());
    int step = (int)((double)(max_value - min_value) / 255);
    for (int i = 0; i < imageData.size(); i++)
        imageData[i] = clamp((imageData[i] - min_value) / step, 0, 255);
    int cropW, cropH, outputW, outputH;
    cropW = cropH = (res[2].x - res[0].x) / 10;
    outputW = outputH = cropW * 3 + 40;
    vector<int> outputImage(outputH * outputW, 255);
    for (int y = 0; y < 3; y++)
        for (int x = 0; x < 3; x++) {
            int idx = y * 3 + x;
            int x0 = res[idx].x - cropW / 2, y0 = res[idx].y - cropH / 2;
            int x1 = (x + 1) * 10 + cropW * x, y1 = (y + 1) * 10 + cropH * y;
            // vector<int> tmp;
            // for (int xx = 0; xx < cropW; xx++)
            //     for (int yy = 0; yy < cropH; yy++)
            //         tmp.append(imageData[(y0 + yy) * w + x0 + xx]);
            //
            for (int xx = 0; xx < cropW; xx++)
                for (int yy = 0; yy < cropH; yy++)
                    outputImage[(yy + y1) * outputW + xx + x1] =
                        imageData[(y0 + yy) * w + x0 + xx];
        }
    saveAsTiff8bit("output.tiff", outputImage, outputW);
    return 0;
}
