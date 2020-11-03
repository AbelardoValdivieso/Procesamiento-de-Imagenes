import cv2
import numpy as np
import sys
import os

import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time


def recreate_image(centers, labels, rows, cols):
    d = centers.shape[1]
    image_clusters = np.zeros((rows, cols, d))
    label_idx = 0
    for i in range(rows):
        for j in range(cols):
            image_clusters[i][j] = centers[labels[label_idx]]
            label_idx += 1
    return image_clusters


if __name__ == '__main__':
    path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    image_name = "bandera.png"
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    metodo=input("seleccione el metodo a usar, (i) kmeans (ii) gmm \n")
    #n_colors = 5
    method = ['kmeans', 'gmm']
    if  metodo=='kmeans':
        select=0
    else:
        if metodo=='gmm':
            select=1

    # Convert to floats instead of the default 8 bits integer coding. Dividing by
    # 255 is important so that plt.imshow behaves works well on float data (need to
    # be in the range [0-1])
    image = np.array(image, dtype=np.float64) / 255
    vecdistancia = []
    vecncolors= []
    graficar= []
    result  = np.ndarray(shape=(11,11), dtype=float)
    for i in range(0,len(result)):
        for j in range(0, len(result)):
            result[i][j]=0
    x = np.arange(1, 10, 1)
    acum=acumtotal=0
    for i in range(10000):
        vecdistancia.append(0)
        vecncolors.append(0)
    for i in range(9):
        graficar.append(0)

    # Load Image and transform to a 2D numpy array.
    rows, cols, ch = image.shape
    assert ch == 3
    image_array = np.reshape(image, (rows * cols, ch))
    for i in range(1,11,1):
        image_array_sample = shuffle(image_array, random_state=0)[:10000]
        print("Para n_clusters :", i)
        if method[select] == 'gmm':
            model = GMM(n_components=i).fit(image_array_sample)
            centro = GMM(n_components=i).fit_predict(image_array_sample)
        else:
            model = KMeans(n_clusters=i, random_state=0).fit(image_array_sample)
            modelo = KMeans(n_clusters=i, random_state=0).fit_transform(image_array_sample)
            centro = KMeans(n_clusters=i, random_state=0).fit_predict(image_array_sample)
            labels = model.predict(image_array)
            centers = model.cluster_centers_
            distance = model.inertia_
            for p in np.arange(0,i):
                for j in np.arange(0,len(centro)):
                    if p==centro[j]:
                        acum=acum+modelo[j][p]
                print("El cluster: ", p+1, "la distancia es: ", acum)
                result[p][i]=acum
                acum = 0
    #acum=0
    #for i in range(1, 10):
        #for j in range(0, len(result)):
            #acum=acum+result[j][i]
        #graficar[i-1]=acum
        #acum=0

    #plt.plot(x, graficar)
    #plt.xlabel('#Cluster')
    #plt.ylabel('Distancia')
    #plt.title('Distancia Intra Cluster vs #Clusters')
    #plt.show()



    plt.figure(2)
    plt.clf()
    plt.axis('off')
    plt.title('Quantized image ({} colors, method={})'.format(i, method[select]))
    plt.imshow(recreate_image(centers, labels, rows, cols))

    plt.show()
