import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

if __name__ == '__main__':
    path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    image_name = 'soccer_game.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hsv = cv2.calcHist([image_hsv], [0],None,[180],[0,180])
    plt.plot(hist_hsv, color='green')
    plt.xlim([0,180])
    plt.show()
    max_val = print(hist_hsv.max())
    max_pos = print(hist_hsv.argmax())
    
    #print(print("el valor maximo es en :\n", max_pos))
    #cv2.imshow("Image", image_hue)
    cv2.waitKey(0)


