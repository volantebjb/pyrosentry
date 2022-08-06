import cv2
import os
from skimage.filters import roberts

directory = "../public/dataset"
raw_dir = os.path.join(directory, "raw")
roberts_dir = os.path.join(directory, "roberts")

for i, filename in enumerate(os.listdir(raw_dir)):
    data = f"fluid_flame_{i+1}.jpg"
    raw_image = cv2.imread(os.path.join(raw_dir, data))
    grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    roberts_image = roberts(grayscale_image)
    filtered_image = cv2.convertScaleAbs(roberts_image, alpha=(255.0))
    cv2.imwrite(os.path.join(roberts_dir, data), filtered_image)