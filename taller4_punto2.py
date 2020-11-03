import cv2
import numpy as np
import sys
import os

def click_event1(event, x, y, flags, param):
    ruta = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    nombre = 'lena.png'
    path_file = os.path.join(ruta, nombre)
    I1= cv2.imread(path_file)
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Puntos de I1 elegidos")
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(I1, str(x) + ',' + str(y), (x, y), font,1, (255, 0, 0), 2)
        cv2.imshow('I1', I1)
        cv2.waitKey(0)

def click_event2(event, x, y, flags, param):
    ruta = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    nombre = 'lena_warped.png'
    path_file = os.path.join(ruta, nombre)
    I2= cv2.imread(path_file)
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Puntos de I2 elegidos")
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(I2, str(x) + ',' + str(y), (x, y), font,1, (255, 0, 0), 2)
        cv2.imshow('I2', I2)
        cv2.waitKey(0)

### PARA I1
ruta = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
nombre = 'lena.png'
path_file = os.path.join(ruta, nombre)
I1 = cv2.imread(path_file)
cv2.imshow('I1', I1)

cv2.setMouseCallback("I1", click_event1)
cv2.waitKey(0)

# Ingreso de datos para I1
print("A continuacion ingrese los numeros de cada punto elegido para I1")

pnt11 = int(input("¿Cuál es el primer numero del primer punto elegido? "))
pnt12 = int(input("¿Cuál es el segundo numero del primer punto elegido? "))
pnt21 = int(input("¿Cuál es el primer numero del segundo punto elegido? "))
pnt22 = int(input("¿Cuál es el segundo numero del segundo punto elegido? "))
pnt31 = int(input("¿Cuál es el primer numero del tercer punto elegido? "))
pnt32 = int(input("¿Cuál es el segundo numero del tercer punto elegido? "))

# Affine para I1
pts1 = np.float32([[pnt11,pnt12], [pnt21,pnt22], [pnt31,pnt32]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M_affine1 = cv2.getAffineTransform(pts1, pts2)
image_affine1 = cv2.warpAffine(I1, M_affine1, I1.shape[:2])

cv2.imshow("I1", image_affine1)
cv2.waitKey(0)

# similarity para I1
tx = 50
ty = 20

sx = 0.75
sy = 1.25

theta = 5
theta_rad = theta * np.pi / 180

M_sim = np.float32([[sx * np.cos(theta_rad), -np.sin(theta_rad), tx],
                    [np.sin(theta_rad), sy * np.cos(theta_rad), ty]])
image_similarityI1 = cv2.warpAffine(I1, M_sim, I1.shape[:2])
cv2.imshow("Similarity I1", image_similarityI1)
cv2.waitKey(0)

# ### PARA I2 se tiene que:
# ruta = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
# nombre = 'lena_warped.png'
# path_file = os.path.join(ruta, nombre)
# I2 = cv2.imread(path_file)
# cv2.imshow('I2', I2)
#
# cv2.setMouseCallback("I2", click_event2)
# cv2.waitKey(0)

# Ingreso de datos para I2
# print("A continuacion ingrese los numeros de cada punto elegido para I2")
#
# I2_pnt11 = int(input("¿Cuál es el primer numero del primer punto elegido? "))
# I2_pnt12 = int(input("¿Cuál es el segundo numero del primer punto elegido? "))
# I2_pnt21 = int(input("¿Cuál es el primer numero del segundo punto elegido? "))
# I2_pnt22 = int(input("¿Cuál es el segundo numero del segundo punto elegido? "))
# I2_pnt31 = int(input("¿Cuál es el primer numero del tercer punto elegido? "))
# I2_pnt32 = int(input("¿Cuál es el segundo numero del tercer punto elegido? "))
#
# # Affine para I2
# pts1 = np.float32([[I2_pnt11,I2_pnt12], [I2_pnt21,I2_pnt22], [I2_pnt31,I2_pnt32]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# M_affine2 = cv2.getAffineTransform(pts1, pts2)
# image_affine2 = cv2.warpAffine(I2, M_affine2, I2.shape[:2])
#
# cv2.imshow("I2", image_affine2)
# cv2.waitKey(0)

# similarity para I2
# M_sim = np.float32([[sx * np.cos(theta_rad), -np.sin(theta_rad), tx],
#                     [np.sin(theta_rad), sy * np.cos(theta_rad), ty]])
# image_similarityI2 = cv2.warpAffine(I2, M_sim, I2.shape[:2])
# cv2.imshow("Similarity I2", image_similarityI2)
# cv2.waitKey(0)