import numpy as np
import cv2
import glob
import os
import json

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo/Imagenes Celular'
path_file = os.path.join(path, '*.jpg')
images = glob.glob(path_file)
cont=0
for fname in images:
    img = cv2.imread(fname)
    scale_percent = 19  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (7,7), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        #corners2 = cv2.cornerSubPix(resized, corners, (7, 7), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        imag = cv2.drawChessboardCorners(resized, (7, 7), corners, ret)



cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print(mtx)
print(dist)
print(cont)
# reprojection error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error

print("total error: {}".format(mean_error / len(objpoints)))

#undistortion
path_file = os.path.join(path, 'prob.jpg')
img = cv2.imread(path_file)
scale_percent = 19  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
h, w = resized.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

if True:
    dst = cv2.undistort(resized, mtx, dist, None, newcameramtx)
else:
    mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
    dst = cv2.remap(resized, mapx, mapy, cv2.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]
cv2.imshow('distorted', resized)
cv2.imshow('calibresult', dst)
cv2.waitKey(0)
#
# file_name = 'calibrationcamara.json'
# json_file = os.path.join(path, file_name)
# path_file = os.path.join(path, 'bien.jpg')

path2="C:/Users/Gloria Dani Abe/PycharmProjects/pythonProject1"
file_name = 'calibrationcamaracel.json'
json_file = os.path.join(path2, file_name)


img = cv2.imread(path_file)

data = {
    'K': mtx.tolist(),
    'distortion': dist.tolist(),
}

with open(json_file, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=1, ensure_ascii=False)

with open(json_file) as fp:
    json_data = json.load(fp)
    print(json_data)