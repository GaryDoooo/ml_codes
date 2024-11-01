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

    vector<int> imageData = read_tiff_file(filename.c_str(), w, h, 100);
    if (w == 0) {
        std::cerr << "Could not open the TIFF file." << std::endl;
        return -1;
    }

    vector<int> imageData_cropped = cropImage(
        imageData, w, h, w / 10 * 2, h / 10 , w / 10 * 8, h / 10 * 9);

    int w_cropped = w / 10 * 6 + 1, h_cropped = h / 10 * 8 + 1;

    vector<point> res =
        find9crossHairs(imageData_cropped, w_cropped, h_cropped);
    for (auto p : res)
        cout << "Locate center again at (" << p.x + w / 10 * 2 << ","
             << p.y + h / 10  << ")\n";
    return 0;
}
