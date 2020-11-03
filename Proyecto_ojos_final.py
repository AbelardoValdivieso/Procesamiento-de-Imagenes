import dlib
import os
import cv2
from matplotlib import pyplot as plt

cap      = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

### Agregar el archivo y el path de "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        a, b = face.left(), face.top()
        c, d = face.right(), face.bottom()
        cv2.rectangle(frame,(a,b), (c,d), (0,255,0),2)
        print(type(a))
        landmarks = predictor(frame, face)
        #puntos ojo1
        o1 =  landmarks.part(36).x
        o2 =  landmarks.part(36).y
        cv2.circle(frame, (o1,o2), 1, (0,0,255), 1)

        o3 =  landmarks.part(37).x
        o4 =  landmarks.part(37).y
        cv2.circle(frame, (o3,o4), 1, (0,0,255), 1)
        o5 =  landmarks.part(38).x
        o6 =  landmarks.part(38).y
        cv2.circle(frame, (o5,o6), 1, (0,0,255), 1)

        punto_superiorix=int((o3+o5)/2)
        punto_superioriy=int((o4+o6)/2)
        cv2.circle(frame, (punto_superiorix,punto_superioriy), 1, (0,0,255), 1)
        o7 =  landmarks.part(39).x
        o8 =  landmarks.part(39).y
        cv2.circle(frame, (o7,o8), 1, (0,0,255), 1)
        o9 =  landmarks.part(40).x
        o10 = landmarks.part(40).y
        cv2.circle(frame, (o9,o10), 1, (0,0,255), 1)
        o11 =  landmarks.part(41).x
        o12 = landmarks.part(41).y

        punto_inferiorix=int((o9+o11)/2)
        punto_inferioriy=int((o10+o12)/2)
        #print("x", punto_inferiorix,"y",punto_inferioriy)
        cv2.circle(frame, (punto_inferiorix, punto_inferioriy), 1, (0, 0, 255), 1)

        cv2.circle(frame, (o11,o12), 1, (0,0,255), 1)

        # puntos ojo2
        o13 =  landmarks.part(42).x
        o14 =  landmarks.part(42).y
        cv2.circle(frame, (o13,o14), 1, (0,0,255), 1)
        o15 =  landmarks.part(43).x
        o16 =  landmarks.part(43).y
        cv2.circle(frame, (o15,o16), 1, (0,0,255), 1)
        o17 =  landmarks.part(44).x
        o18 =  landmarks.part(44).y

        punto_superiordx=int((o15+o17)/2)
        punto_superiordy=int((o16+o18)/2)
        cv2.circle(frame, (punto_superiordx,punto_superiordy), 1, (0,0,255), 1)

        cv2.circle(frame, (o17,o18), 1, (0,0,255), 1)
        o19 =  landmarks.part(45).x
        o20 =  landmarks.part(45).y
        cv2.circle(frame, (o19,o20), 1, (0,0,255), 1)
        o21 =  landmarks.part(46).x
        o22 = landmarks.part(46).y
        cv2.circle(frame, (o21,o22), 1, (0,0,255), 1)
        o23 = landmarks.part(47).x
        o24 = landmarks.part(47).y
        cv2.circle(frame, (o23,o24), 1, (0,0,255), 1)
        punto_inferiordx=int((o21+o23)/2)
        punto_inferiordy=int((o22+o24)/2)
        cv2.circle(frame, (punto_inferiordx,punto_inferiordy), 1, (0,0,255), 1)


        distancia_horizontal_ojo_izquierdo = cv2.line(frame, (o1,o2),(o7,o8),(255,0,0),1)
        distancia_horizontal_ojo_derecho   = cv2.line(frame, (o13, o14), (o19, o20), (255, 0, 0), 1)

        distancia_horizontal_ojo_derecho = cv2.line(frame, (punto_superiorix, punto_superioriy), (punto_inferiorix, punto_inferioriy), (0, 0, 255), 1)
        distancia_horizontal_ojo_derecho = cv2.line(frame, (punto_superiordx, punto_superiordy), (punto_inferiordx, punto_inferiordy), (0, 0, 255), 1)



    cv2.imshow("Escala Grises",gray)
    cv2.imshow("Resultado", frame)


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()