import cv2
import sys
import os

if __name__ == '__main__':
    path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    image_name = 'vtest.avi'
    path_file = os.path.join(path, image_name)

    if True:
        backSub = cv2.createBackgroundSubtractorMOG2()
    else:
        backSub = cv2.createBackgroundSubtractorKNN()

    camera = cv2.VideoCapture(path_file)
    ret = True

    while ret:
        ret, image = camera.read()
        if ret:
            fgMask = backSub.apply(image)
            cv2.imshow("Image", image)
            cv2.imshow('FG Mask', fgMask)
            cv2.waitKey(10)
            image_draw = image.copy()
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for idx, i in enumerate(contours):
                if len(contours[idx]) > 100:
                    hull = cv2.convexHull(contours[idx])
                    cv2.drawContours(image_draw, contours, idx, (0, 255, 255), 2)
                    cv2.drawContours(image_draw, [hull], 0, (255, 0, 0), 2)
                    M = cv2.moments(contours[idx])
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    area = M['m00']
                    x, y, width, height = cv2.boundingRect(contours[idx])
                    (x, y), radius = cv2.minEnclosingCircle(contours[idx])
                    center = (int(x), int(y))
                    radius = int(radius)

                cv2.imshow("Image", image_draw)
                cv2.waitKey(10)

