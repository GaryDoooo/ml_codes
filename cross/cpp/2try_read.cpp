#include <algorithm>
#include <iostream>
#include <vector>
/////// Own Modules ///////
#include "tiff_utilities.h"

using namespace std;

int main() {
    int w, h;
    vector<float> imageData = read_tiff_file("1.tif", w, h);
    // Open the TIFF file
    // TIFF* tiff = TIFFOpen("1.tif", "r");
    // if (!tiff) {
    //     std::cerr << "Could not open the TIFF file." << std::endl;
    //     return -1;
    // }
    //
    // Get the image width and height
    // uint32_t width, height;
    // TIFFGetField(tiff, TIFFTAG_IMAGEWIDTH, &width);
    // TIFFGetField(tiff, TIFFTAG_IMAGELENGTH, &height);
    //
    // Allocate memory for the image data
    // std::vector<float> imageData(width * height);
    //
    // Read the image data
    // for (uint32_t row = 0; row < height; ++row) {
    //     TIFFReadScanline(tiff, &imageData[row * width], row);
    // }
    //
    // Close the TIFF file
    // TIFFClose(tiff);

    // Process the image data as needed
    float max_value = 0, min_value = 1e8;
    for (auto i : imageData) {
        max_value = max(max_value, i);
        min_value = min(min_value, i);
    }
    cout << max_value << " " << min_value << endl;
    // cout << get_one() << endl;
    // cout << get_max(imageData) << endl;
    // cout << imageData[80] << " " << imageData[0][80] << endl;
    // cout << imageData[3 * width + 3] << " " << imageData[3][3] << endl;
    return 0;
}

