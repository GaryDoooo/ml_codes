#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Load an image
    cv::Mat image = cv::imread("1.png", cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "Error: Could not load image." << std::endl;
        return -1;
    }

    // Apply Gaussian blur
    cv::Mat blurredImage;
    cv::GaussianBlur(image, blurredImage, cv::Size(5, 5), 1.4);

    // Display the original and blurred images
    cv::imshow("Original Image", image);
    cv::imshow("Blurred Image", blurredImage);
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}
