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
            imagen = cv2.imread(path_file)
            cv2.imshow('Imagen', self.image)
            cv2.waitKey(0)
x=colorImage()
x.displayProperties()
x.makeGray()
