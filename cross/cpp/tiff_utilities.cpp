#include "tiffio.h"
#include <algorithm>
#include <iostream>
#include <vector>
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
    width = width32;
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
        if (imageData[i] < 0)
            imageData[i] = 0;
        image[i] = int(imageData[i] * decimal_multiple + 0.5);
    }

    return image;
}

std::vector<int> shrinkImageByAveraging(const std::vector<int>& image,
                                        int originalWidth, int originalHeight,
                                        int blockSize, int& newWidth,
                                        int& newHeight) {
    // Calculate new dimensions
    newWidth =
        (originalWidth + blockSize - 1) / blockSize; // Round up to handle edges
    newHeight = (originalHeight + blockSize - 1) /
                blockSize; // Round up to handle edges

    // Create a new vector for the shrunk image
    std::vector<int> shrunkImage(newWidth * newHeight, 0);

    // Iterate over each block in the original image
    for (int y = 0; y < newHeight; ++y) {
        for (int x = 0; x < newWidth; ++x) {
            long long sum = 0;
            int count = 0;

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
                sum / count; // Average over the actual number of pixels
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
            long long left = (j > 0) ? prefixSum[i * width + (j - 1)] : 0LL;
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

std::vector<int> cropImage(const std::vector<int>& originalData, int width,
                           int height, int x0, int y0, int x1, int y1) {
    // Ensure coordinates are within bounds
    x0 = std::max(0, x0);
    y0 = std::max(0, y0);
    x1 = std::min(width - 1, x1);
    y1 = std::min(height - 1, y1);

    // Calculate the cropped width and height
    int croppedWidth = x1 - x0 + 1;
    int croppedHeight = y1 - y0 + 1;
    vector<int> croppedData(croppedWidth * croppedHeight, 0);

    // Copy the cropped data into the new array
    for (int y = 0; y < croppedHeight; ++y) {
        for (int x = 0; x < croppedWidth; ++x) {
            croppedData[y * croppedWidth + x] =
                originalData[(y0 + y) * width + (x0 + x)];
        }
    }
    return croppedData;
}

void saveAsTiff8bit(const string& filename, const vector<int>& image, int w) {
    int width = w;
    int height = image.size() / w;

    TIFF* tiff = TIFFOpen(filename.c_str(), "w");
    if (!tiff) {
        cerr << "Could not open TIFF file for writing." << endl;
        return;
    }

    TIFFSetField(tiff, TIFFTAG_IMAGEWIDTH, width);
    TIFFSetField(tiff, TIFFTAG_IMAGELENGTH, height);
    TIFFSetField(tiff, TIFFTAG_SAMPLESPERPIXEL, 1);
    TIFFSetField(tiff, TIFFTAG_BITSPERSAMPLE, 8);
    TIFFSetField(tiff, TIFFTAG_PLANARCONFIG, PLANARCONFIG_CONTIG);
    TIFFSetField(tiff, TIFFTAG_PHOTOMETRIC, PHOTOMETRIC_MINISBLACK);
    // int max_value=*max_element(image.begin(),image.end());
    // int min_value=*min_element(image.begin(),image.end());
    // int step=m

    // Write each row of pixels
    for (int i = 0; i < height; i++) {
        uint8_t* row = new uint8_t[width];
        for (int j = 0; j < width; j++) {
            row[j] = static_cast<uint8_t>(image[i * width + j]);
        }
        TIFFWriteScanline(tiff, row, i);
        delete[] row;
    }

    TIFFClose(tiff);
}

bool saveRGBTIFF(const std::string& filename, const std::vector<unsigned char>& imageData, int width, int height) {
    TIFF* tif = TIFFOpen(filename.c_str(), "w");
    if (!tif) {
        std::cerr << "Could not open " << filename << " for writing." << std::endl;
        return false;
    }

    // Set TIFF tags
    TIFFSetField(tif, TIFFTAG_IMAGEWIDTH, width);
    TIFFSetField(tif, TIFFTAG_IMAGELENGTH, height);
    TIFFSetField(tif, TIFFTAG_SAMPLESPERPIXEL, 3);  // RGB
    TIFFSetField(tif, TIFFTAG_BITSPERSAMPLE, 8);
    TIFFSetField(tif, TIFFTAG_ORIENTATION, ORIENTATION_TOPLEFT);
    TIFFSetField(tif, TIFFTAG_PLANARCONFIG, PLANARCONFIG_CONTIG);
    TIFFSetField(tif, TIFFTAG_PHOTOMETRIC, PHOTOMETRIC_RGB);
    TIFFSetField(tif, TIFFTAG_ROWSPERSTRIP, TIFFDefaultStripSize(tif, width * 3));

    // Write image data
    for (int row = 0; row < height; ++row) {
        if (TIFFWriteScanline(tif, const_cast<unsigned char*>(&imageData[row * width * 3]), row, 0) < 0) {
            std::cerr << "Error writing TIFF scanline." << std::endl;
            TIFFClose(tif);
            return false;
        }
    }

    TIFFClose(tif);
    return true;
}
