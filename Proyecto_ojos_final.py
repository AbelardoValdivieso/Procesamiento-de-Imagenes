import dlib
import os
import cv2
from time import time

cap    = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

### Agregar el archivo y el path de "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#declaración de variables a usar
ppr_ant_I = 0
ppr_ant_D = 0

panto2 = 0
panto14 = 0

sueno = 0
parpadeo =0
prom_parpadeo=12
#da inicio al programa una vez ingresado enter
entrada = input("ingrese enter para comenzar \n")

#toma el tiempo inicial del programa
star_time=time()
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    cont=0
    for face in faces:
        cont=cont+1
        a, b = face.left(), face.top()
        c, d = face.right(), face.bottom()
        cv2.rectangle(frame,(a,b), (c,d), (0,255,0),2)
        #print(type(a))
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

        #dibuja una linea horizontal para cada ojo en su punto medio
        distancia_horizontal_ojo_izquierdo = cv2.line(frame, (o1,o2),(o7,o8),(255,0,0),1)
        distancia_horizontal_ojo_derecho   = cv2.line(frame, (o13, o14), (o19, o20), (255, 0, 0), 1)


        parp2 = o2
        parp3 = o14
        # se realiza la diferencia entre los puntos o2 y el punto o2 anterior para guardar la diferencia en ppr1
        ppr1 = o2 - panto2
        # se realiza la diferencia entre los puntos o14 y el punto o14 anterior para guardar la diferencia en ppr1
        ppr2 = o14 - panto14

        panto2 = o2
        panto14 = o14
        #dibuja una linea vertical sobre cada ojo que pasa por el centro de cada uno (izquierdo y derecho)
        distancia_vertical_ojo_izquierdo = cv2.line(frame, (punto_superiorix, punto_superioriy), (punto_inferiorix, punto_inferioriy), (0, 0, 255), 1)
        distancia_vertical_ojo_derecho = cv2.line(frame, (punto_superiordx, punto_superiordy), (punto_inferiordx, punto_inferiordy), (0, 0, 255), 1)

        #se realiza la diferencia entre el punto inferior y superior del ojo izquierdo y derecho
        #ppr_izq diferencia ojo izquierdo
        ppr_izq = punto_inferioriy - punto_superioriy
        # ppr_der diferencia ojo derecho
        ppr_der = punto_inferiordy - punto_superiordy
        font = cv2.FONT_HERSHEY_SIMPLEX
        #este if realiza la cuenta de parpadeos por minuto basandose en las diferencias previamente calculadas ppr_izq ppr_der ppr1 y ppr2
        if (ppr_izq != ppr_ant_I or ppr_izq != (ppr_ant_I+1) or ppr_izq != (ppr_ant_I-1)) and (ppr_der != ppr_ant_D or ppr_der != (ppr_ant_D+1) or ppr_der != (ppr_ant_D-1)):
            if ppr1 < 10 and ppr2 < 10:
                if ppr1 > 2 and ppr2 > 2:
                    parpadeo = parpadeo + 1
            else:
                cv2.putText(frame, 'Se esta moviendo ', (30, 30), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        #ppr_ant_I y ppr_ant_D almacenan la diferencias entre la parte superior e inferior de los ojos izquierdo y derecho
        ppr_ant_I = ppr_izq
        ppr_ant_D = ppr_der
        #imprime el total de parpadeos en pantalla dentro del ciclo establecido, se reinicia cada 60 s
        cv2.putText(frame, "Total de parpadeos: {}".format(parpadeo), (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 255, 255), 2)

        final_time= time()
        #se ve la diferencia de tiempo para medir el total de parpadeos durante un tiempo
        elapsed_time = final_time - star_time
        #aquí se verifica el total de parpadeos en el tiempo establecido en segundos(60)
        if elapsed_time > 60:
            #imprime la cantidad de parpadeos durante el tiempo establecido
            print(parpadeo)
            prom_parpadeo=parpadeo
            #start time toma el valor de final time para empezar un nuevo ciclo
            star_time = final_time
            parpadeo=0
        #si el prom parpadeo es menor a 12 significa que la persona se está durmiendo
        if (prom_parpadeo < 12):
            #imprime el letrero para dar aviso a la persona que se está durmiendo
            cv2.putText(frame, 'NO TE DUERMAS! ', (60, 85), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cont =0
    cv2.imshow("Escala Grises",gray)
    cv2.imshow("Resultado", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
