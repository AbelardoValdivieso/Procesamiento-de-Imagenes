import cv2
import numpy as np
import os

if __name__ == '__main__':
    path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    first_column = image_gray[:, 0]
    rect = image_gray[100:200, 100:200]
    rect = np.zeros(rect.shape, np.uint8)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image_hsv)
    s = 255 * np.ones_like(s)
    v = 255 * np.ones_like(v)
    image_hue = cv2.merge((h, s, v))
    image_hue = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)

    #image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    #image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)

    cv2.imshow("Image", image_hue)
    cv2.waitKey(0)



