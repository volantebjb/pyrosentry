import cv2
import os

dataset_dir = "../public/dataset"
raw_dir = os.path.join(dataset_dir, "raw")
canny_dir = os.path.join(dataset_dir, "canny")

for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    raw_image = cv2.imread(os.path.join(raw_dir, data))
    canny_image = cv2.Canny(raw_image, 100, 200)
    cv2.imwrite(os.path.join(canny_dir, data), canny_image)