#include <algorithm>
#include <iostream>
#include <vector>
#include "tiffio.h"
#define TIFF_TO_INT_DECIMAL 1000
using namespace std;

vector<int> read_tiff_file(const char* filename, int& width, int& height,
                           int decimal_multiple = TIFF_TO_INT_DECIMAL) {
    // Open the TIFF file
    TIFF* tiff = TIFFOpen(filename, "r");
    if (!tiff) {
        std::cerr << "Could not open the TIFF file." << std::endl;
        vector<int> a;
        return a;
    }

    // Get the image width and height
    uint32_t width32, height32;
    TIFFGetField(tiff, TIFFTAG_IMAGEWIDTH, &width32);
    TIFFGetField(tiff, TIFFTAG_IMAGELENGTH, &height32);
    width  = width32;
    height = height32;

    // Allocate memory for the image data
    std::vector<float> imageData(width * height);

    // Read the image data
    for (uint32_t row = 0; row < height; ++row) {
        TIFFReadScanline(tiff, &imageData[row * width], row);
    }

    // Close the TIFF file
    TIFFClose(tiff);

    // Process the image data as needed

    vector<int> image(width * height);
    for (int i = 0; i < image.size(); i++) {
        if (imageData[i] < 0) imageData[i] = 0;
        image[i] = int(imageData[i] * decimal_multiple + 0.5);
    }

    return image;
}

std::vector<int> shrinkImageByAveraging(const std::vector<int>& image,
                                        int originalWidth, int originalHeight,
                                        int blockSize, int& newWidth,
                                        int& newHeight) {
    // Calculate new dimensions
    newWidth = (originalWidth + blockSize - 1) /
               blockSize;  // Round up to handle edges
    newHeight = (originalHeight + blockSize - 1) /
                blockSize;  // Round up to handle edges

    // Create a new vector for the shrunk image
    std::vector<int> shrunkImage(newWidth * newHeight, 0);

    // Iterate over each block in the original image
    for (int y = 0; y < newHeight; ++y) {
        for (int x = 0; x < newWidth; ++x) {
            long long sum = 0;
            int count     = 0;

            // Sum up all the pixels in the block, or smaller for edge blocks
            for (int dy = 0; dy < blockSize; ++dy) {
                for (int dx = 0; dx < blockSize; ++dx) {
                    int originalX = x * blockSize + dx;
                    int originalY = y * blockSize + dy;

                    // Check if the pixel is within bounds
                    if (originalX < originalWidth &&
                        originalY < originalHeight) {
                        sum += image[originalY * originalWidth + originalX];
                        ++count;
                    }
                }
            }

            // Compute the average for the block
            shrunkImage[y * newWidth + x] =
                sum / count;  // Average over the actual number of pixels
            // if (shrunkImage[y * newWidth + x] < 0)
            //     cout << x << "," << y << endl;
        }
    }

    return shrunkImage;
}

std::vector<long long> compute2DPrefixSum(const std::vector<int>& image,
                                          int width, int height) {
    // Initialize the prefix sum matrix as a 1D vector
    std::vector<long long> prefixSum(width * height, 0);

    // Compute the prefix sum
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            long long current = image[i * width + j];

            long long above = (i > 0) ? prefixSum[(i - 1) * width + j] : 0LL;
            long long left  = (j > 0) ? prefixSum[i * width + (j - 1)] : 0LL;
            long long aboveLeft =
                (i > 0 && j > 0) ? prefixSum[(i - 1) * width + (j - 1)] : 0LL;

            prefixSum[i * width + j] = current + above + left - aboveLeft;
            // if (i > 0 and j > 0) {
            //     if (prefixSum[i * width + j] < prefixSum[i * width + j - 1]
            //     or
            //         prefixSum[i * width + j] <
            //             prefixSum[(i - 1) * width + j - 1] or
            //         prefixSum[i * width + j] < prefixSum[(i - 1) * width +
            //         j]) cout << j << "," << i << endl;
            // }
        }
    }

    return prefixSum;
}
