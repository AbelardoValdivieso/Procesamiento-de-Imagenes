import cv2
import numpy as np
import cv2
import glob
import os
import json
from camera_model import *

if __name__ == '__main__':

    data = json.load(open('calibrationcamaracel.json'))
    K = data['K']
    # intrinsics parameters
    width =int(K[0][2])*2
    height=int(K[1][2])*2

    # extrinsics parameters
    # Caso 1 d=2, h=1, tilt=0 pan = 5
    # Caso 2 d=3, h=2, tilt=30 pan = 0
    d=3
    h = 2
    tilt=0
    pan=0
    R = set_rotation(tilt,pan,0)
    t = np.array([0, d, h])

    # create camera
    camera = projective_camera(K, width, height, R, t)

    square_3D = np.array([[0.5, 0.5, 0], [0.5, -0.5,0], [-0.5, -0.5, 0], [-0.5, 0.5, 0]])
    square_2D = projective_camera_project(square_3D, camera)

    square_3D_2 = np.array([[0.5, 0.5, 1], [0.5, -0.5, 1], [-0.5, -0.5, 1], [-0.5, 0.5, 1]])
    square_2D_2 = projective_camera_project(square_3D_2, camera)


    image_projective = 255 * np.ones(shape=[camera.height, camera.width, 3], dtype=np.uint8)
    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D[1][0], square_2D[1][1]), (0, 1, 255), 3)
    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D[2][0], square_2D[2][1]), (0, 1, 255), 3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D[3][0], square_2D[3][1]), (0, 1, 255), 3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D[0][0], square_2D[0][1]), (0, 1, 255), 3)

    cv2.line(image_projective, (square_2D_2[1][0], square_2D_2[1][1]), (square_2D_2[2][0], square_2D_2[2][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D_2[2][0], square_2D_2[2][1]), (square_2D_2[3][0], square_2D_2[3][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D_2[0][0], square_2D_2[0][1]), (square_2D_2[1][0], square_2D_2[1][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D_2[3][0], square_2D_2[3][1]), (square_2D_2[0][0], square_2D_2[0][1]), (0, 0, 255), 3)

    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D_2[1][0], square_2D_2[1][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D_2[2][0], square_2D_2[2][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D_2[0][0], square_2D_2[0][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D_2[3][0], square_2D_2[3][1]), (255, 0, 0), 3)


    # cuadrado_3D = np.array([[1, 1, 0], [1, -1, 0], [-1, -1, 0], [-1, 1, 0]])
    # cuadrado2_3D = np.array([[1, 1, 2], [1, -1, 2], [-1, -1, 2], [-1, 1, 2]])

    cv2.imshow("Image", image_projective)
    cv2.waitKey(0)


