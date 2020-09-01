import numpy as np
from PIL import Image
import os
import cv2
import random
from math import sqrt

class imageShape():
    def __init__(self):
        #se reciben los parámetros de ancho y alto
        ancho =  int(input("ingrese el ancho deseado de la imagen: "))
        alto = int(input("ingrese el alto deseado de la imagen: "))
        #se almacenan los parámetros ingresados por el usuario
        self.ancho=ancho
        self.alto=alto
    def GenerateShape(self):
        if  self.ancho>self.alto:
            self.min=int(self.alto / 2)
        else: self.min=int(self.ancho / 2)
            #saca el menor de los numeros,
        self.menorT=int(sqrt(self.min * self.min - int((self.min * self.min) / 4)))
        self.imagenshape=cv2.imread("cuadrado.png")
        self.selector = random.randint(0, 3)                   #Genera el numero aleatorio uniformemente distribuido
        self.dimenShape = (self.ancho, self.alto)
        self.redimension_img = cv2.resize(self.imagenshape, self.dimenShape)
        #una vez se halla generado el numero aleatorio entre 0 y 3
        if self.selector== 0:
            #genera un triangulo a partir de lineas
            cv2.line(self.redimension_img, (int(self.ancho / 2), int((self.alto - self.menorT) / 2)), (int(self.ancho / 2) + int(self.menorT / 2), (int((self.alto - self.menorT) / 2) + self.menorT)), (255, 255, 0), 0.5)
            cv2.line(self.redimension_img, (int(self.ancho / 2) + int(self.menorT / 2), int(self.alto / 2) + int(self.menorT / 2)), (int(self.ancho / 2) - int(self.menorT / 2), int(self.alto / 2) + int(self.menorT / 2)), (255, 255, 0), 0.5)
            cv2.line(self.redimension_img, (int(self.ancho / 2) - int(self.menorT / 2), int(self.alto / 2) + int(self.menorT / 2)), (int(self.ancho / 2), int((self.alto - self.menorT) / 2)), (255, 255, 0), 0.5)
            self.imagen_sol=self.redimension_img

        if self.selector== 1:
            # genera un cuadrado
            self.puntoI_x=int((self.ancho - self.min) / 2)
            self.puntoI_y=int((self.alto - self.min) / 2)
            self.redimension_img=cv2.rectangle(self.redimension_img, (self.puntoI_x, self.puntoI_y), (self.puntoI_x + self.min, self.puntoI_y + self.min), (255, 255, 0), -1)
            M=cv2.getRotationMatrix2D((self.ancho // 2, self.alto // 2), 45, 1)        #Rotacion del cuadrado 45 grados
            self.imagen_sol=cv2.warpAffine(self.redimension_img, M, (self.ancho, self.alto))


        if self.selector== 2:
            # genera un rectangulo
            self.anch_rec=int(self.ancho / 4)
            self.alt_rec=int(self.alto / 4)
            self.imagen_sol=cv2.rectangle(self.redimension_img, (self.anch_rec, self.alt_rec), (self.anch_rec + int(self.ancho / 2), self.alt_rec + int(self.alto / 2)), (255, 255, 0), -1)


        if self.selector== 3:
            #genera un circulo
            self.radio=int(self.min / 2)
            self.imagen_sol = cv2.circle(self.redimension_img, ((int(self.ancho / 2)), int(self.alto / 2)), self.radio, (255, 255, 0), 3) #guarda la Imagen

    def showShape(self):
        # muestra la imagen y la mantiene en pantalla durante 5 s
        cv2.imshow("Imagen", self.imagen_sol)
        cv2.waitKey(5000)

    def getShape(self):
        #Se clasifica la imagen generada e imprime el nombre de la figura generada
        if self.selector== 0:
            print("la figura generada es un triangulo")

        if self.selector== 1:
           print("la figura generada es un cuadrado")

        if self.selector== 2:
            print("la figura generada es un rectangulo")

        if  self.selector== 3:
            print("la figura generada es un circulo")

    def WhatShape(self):
        #recibe la dirección y el nombre de una imagen de fondo negro y objeto claro
        #self.path    = input("Ingrese la ubicación de su imagen: ")
        #self.nombre_imagen = input("Ingrese el nombre de su imagen: ")
        #self.imagenes=cv2.imread(path_file)
        #para recibi una imagen se debe descomentariar todo lo anterior
        #para las pruebas se usa la misma imagen generada
        self.imagenes= self.imagen_sol
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Transformacion a Escala de Grises
        self.image_gray = cv2.cvtColor(self.imagenes, cv2.COLOR_BGR2GRAY)
        #Binarización
        ret, self.Ibw_Cb = cv2.threshold(self.image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        #creacion del contorno de la imagen
        self.contorno1, self.contornos, = cv2.findContours(self.Ibw_Cb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for i in self.contorno1:
            self.eps=0.003*cv2.arcLength(i, True)
            self.imagen_persn=cv2.approxPolyDP(i, self.eps, True)
            cv2.drawContours(self.imagenes, [self.imagen_persn], 0, (0, 255, 0), 3)
            x, y, anchofig, altfig=cv2.boundingRect(self.imagen_persn)

        #de acuerdo al número de vertices se clasifica la figura ingresada por el usuario
        if(len(self.imagen_persn))==3:
            print("la figura introducida es un triangulo")
        else:
            if (len(self.imagen_persn))==4:

                if float(anchofig/altfig)==1:
                    print("la figura introducida es un cuadrado")
                else:
                    print("la figura introducida es un rectangulo")
            else:
                print("la figura introducida es un circulo")

        #Se imprime el tipo de figura introducida por la persona



