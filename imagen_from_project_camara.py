import cv2
from camera_model import *

if __name__ == '__main__':
    # intrinsics parameters
    fx = 1000
    fy = 1000
    width = 1280
    height = 720
    cx = width / 2
    cy = height / 2
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1.0]])

    # extrinsics parameters
    h = 3
    R = set_rotation(0,0, 0)
    t = np.array([0, -10, h])

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
