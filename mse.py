import numpy as np

def ecm(imageA, imageB):

#esta funcion calcula el error cuadrático medio
 err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)

 err /= float(imageA.shape[0] * imageA.shape[1])
 return err