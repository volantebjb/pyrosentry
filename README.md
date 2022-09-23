# PyroSentry

## Description

This project is about detecting liquid flames. It involves several steps including converting images to different color spaces, applying edge detection and segmentation, and finally concatenating the results.

## Documentation

The documentation for this project can be found in the `documentation` directory. The main document is `liquid_flame_detection.pdf`.

## Scripts

- **rgb_hsv_conversion.py**: Converts the raw images to RGB and HSV color spaces.
- **canny_edge_detection.py**: Applies Canny edge detection to the raw images.
- **roberts_edge_detection.py**: Applies Roberts edge detection to the raw images.
- **image_segmentation.py**: Segments the HSV images based on a specific color range.
- **image_fusion.py**: Concatenates the HSV, Canny, and Roberts images.
