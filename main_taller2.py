import clase_taller2
import cv2


if __name__ == '__main__':
#main
    x=clase_taller2.imageShape() #solicita al usuario las dimensiones de la imagen
    x.GenerateShape()            #Se crea la figura
    x.showShape()                #visualiza la figura generada durante 5 segundos
    clas_imagen=x.getShape()
    cv2.destroyAllWindows()
    imagen_usuario=x.WhatShape()  #recibe una imagen de entrada (de fondo negro y objeto claro) que contiene una figura y la clasifica

