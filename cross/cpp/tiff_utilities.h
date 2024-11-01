// tiff_utilities.h
#include <vector>
#pragma once

#define TIFF_TO_INT_DECIMAL 1000

// std::vector<int> read_tiff_file(const char* filename, int& width, int&
// height,int);
std::vector<int> read_tiff_file(const char* filename, int& width, int& height,
                                int decimal_multiple = TIFF_TO_INT_DECIMAL);

std::vector<int> shrinkImageByAveraging(const std::vector<int>& image,
                                        int originalWidth, int originalHeight,
                                        int blockSize, int& newWidth,
                                        int& newHeight);
std::vector<long long> compute2DPrefixSum(const std::vector<int>& image,
                                          int width, int height);
std::vector<int> cropImage(const std::vector<int>& originalData, int width,
                           int height, int x0, int y0, int x1, int y1);
void saveAsTiff8bit(const std::string& filename, const std::vector<int>& image,
                    int w);
bool saveRGBTIFF(const std::string& filename,
                 const std::vector<unsigned char>& imageData, int width,
                 int height);
