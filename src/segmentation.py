import cv2
import os
import numpy as np

dataset_dir = "../public/dataset"
raw_dir = os.path.join(dataset_dir, "raw")
hsv_dir = os.path.join(dataset_dir, "hsv")
segmentation_dir = os.path.join(dataset_dir, "segmentation")

for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    hsv_image = cv2.imread(os.path.join(hsv_dir, data))
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    segmented_image = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
    cv2.imwrite(os.path.join(segmentation_dir, data), segmented_image)