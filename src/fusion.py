import cv2
import os

dataset_dir = "../public/dataset"
raw_dir = os.path.join(dataset_dir, "raw")
hsv_dir = os.path.join(dataset_dir, "hsv")
canny_dir = os.path.join(dataset_dir, "canny")
roberts_dir = os.path.join(dataset_dir, "roberts")
fusion_dir = os.path.join(dataset_dir, "fusion")

for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    hsv_image = cv2.imread(os.path.join(hsv_dir, data))
    canny_image = cv2.imread(os.path.join(canny_dir, data))
    roberts_image = cv2.imread(os.path.join(roberts_dir, data))
    concatenated_image = cv2.hconcat([hsv_image, canny_image, roberts_image])
    cv2.imwrite(os.path.join(fusion_dir, data), concatenated_image)