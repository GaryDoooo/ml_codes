// tiff_utilities.h
#include <vector>
#pragma once

#define TIFF_TO_INT_DECIMAL 1000

// std::vector<int> read_tiff_file(const char* filename, int& width, int& height,int);
std::vector<int> read_tiff_file(const char* filename, int& width, int& height,
                           int decimal_multiple = TIFF_TO_INT_DECIMAL); 

std::vector<int> shrinkImageByAveraging(const std::vector<int>& image,
                                        int originalWidth, int originalHeight,
                                        int blockSize, int& newWidth,
                                        int& newHeight);
std::vector<long long> compute2DPrefixSum(const std::vector<int>& image,
                                          int width, int height);
