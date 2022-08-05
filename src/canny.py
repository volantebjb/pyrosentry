import cv2
import os

directory = "../public/dataset"
raw_dir = os.path.join(directory, "raw")
canny_dir = os.path.join(directory, "canny")


for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    raw_image_path = os.path.join(raw_dir, data)
    raw_image = cv2.imread(raw_image_path)
    
    canny_image = cv2.Canny(raw_image, 100, 200)
    cv2.imwrite(os.path.join(canny_dir, data), canny_image)