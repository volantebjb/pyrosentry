import cv2
import os

dataset_dir = "../public/dataset"
raw_dir = os.path.join(dataset_dir, "raw")
rgb_dir = os.path.join(dataset_dir, "rgb")
hsv_dir = os.path.join(dataset_dir, "hsv")

for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    raw_image = cv2.imread(os.path.join(raw_dir, data))
    rgb_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(rgb_dir, data), rgb_image)
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    cv2.imwrite(os.path.join(hsv_dir, data), hsv_image)