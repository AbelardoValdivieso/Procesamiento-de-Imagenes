import numpy as np
import cv2
import os
class colorImage:
        def __init__(self):
            self.path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
            imagename ='codigo.JPG'
            path_file = os.path.join(self.path, imagename)
            self.image = cv2.imread(path_file)
            cv2.imshow('Imagen',self.image)
            cv2.waitKey(0)
        def displayProperties(self):
            self.path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
            imagenamex = 'codigo.JPG'
            path_file = os.path.join(self.path, imagenamex)
            imagen = cv2.imread(path_file)
            Alto, ancho,channels = imagen.shape
            print("Alto:",Alto, "  Ancho:",ancho)
        def makeGray(self):
            self.path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
            imagenamex = 'codigo.JPG'
            path_file = os.path.join(self.path, imagenamex)
            self.imagen = cv2.imread(path_file,0)
            cv2.imshow('Imagen', self.imagen)
            cv2.waitKey(0)

        def colorizeRGB(self):
            self.path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
            imagename = 'codigo.JPG'
            path_file = os.path.join(self.path, imagename)
            imagen = cv2.imread(path_file)
            alto, ancho, channels = imagen.shape
            self.cadena = input("Introduzca una canal de color que desea imponer: ")
            if self.cadena=="blue":
                imagen[0:alto,0:ancho, 1] = 0
                imagen[0:alto,0:ancho, 2] = 0
            elif self.cadena=="red":
                imagen[0:alto,0:ancho, 0] = 0
                imagen[0:alto,0:ancho, 1] = 0
            elif self.cadena=="green":
                imagen[0:alto,0:ancho, 0] = 0
                imagen[0:alto,0:ancho, 2] = 0
            else: cv2.imshow('Imagen', imagen)
            print("el canal escogido fue :\n", self.cadena)
            cv2.imshow('Imagen', imagen)
            cv2.waitKey(0)
        def makehue(self):
            self.path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
            imagenamex = 'codigo.JPG'
            path_file = os.path.join(self.path, imagenamex)
            self.imagen = cv2.imread(path_file)
            self.hsvImage = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
            S=self.hsvImage[:,:, 1] = 255
            V=self.hsvImage[:,:, 2] = 255
            self.BGR_Image= cv2.cvtColor(self.hsvImage, cv2.COLOR_HSV2BGR)
            cv2.imshow('image', self.BGR_Image)
            cv2.waitKey(0)
result=colorImage()
#result.displayProperties()
result.makeGray()
result.colorizeRGB()
result.makehue()