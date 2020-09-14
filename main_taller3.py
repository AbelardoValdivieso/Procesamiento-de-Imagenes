import cv2
import numpy as np
from noise import noise
from mse import ecm
import os
from time import time
#el tiempo de ejecucion se encuentra comentariado para cada filtro
if __name__ == '__main__':
    path = 'C:/Users/Gloria Dani Abe/Documents/Abelardo'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # add noise gauss
    lena_gauss_noisy = noise("gauss", image_gray.astype(np.float)/255)
    lena_gauss_noisy = (255 * lena_gauss_noisy).astype(np.uint8)
    cv2.imshow("lena_Gauss", lena_gauss_noisy)
    # add noise s&p
    lena_syp_noisy = noise("s&p", image_gray.astype(np.float) / 255)
    lena_syp_noisy = (255 * lena_syp_noisy).astype(np.uint8)
    cv2.imshow("lena_syp", lena_syp_noisy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #aplicacion de filtros


    #filtro gaussiano para lena_gauss_noisy
    #se tempo el tiempo inicial
    #tiempo_inicio_FG = time()
    N = 7
    image_gaussiano_gauss = cv2.GaussianBlur(lena_gauss_noisy, (N, N), 1.5)
    #tiempo_filtro_GLG = time() - tiempo_inicio_FG
    #tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro gaussiano para lena_gauss_noisy: ", tiempo_filtro_GLG)

    #estimación del ruido con filtro gaussiano
    imagen_noise_gaussiano_lenagauss = abs(lena_gauss_noisy - image_gaussiano_gauss)

    #error cuadrático medio con el filtro gaussiano para lena_gauss_noisy
    ECM_filtrogaussiano_gauss = ecm(image_gaussiano_gauss,lena_gauss_noisy)
    print("error cuadrático medio con el filtro gaussiano para lena_gauss_noisy: ", ECM_filtrogaussiano_gauss)
    cv2.imshow("lena_Gauss", lena_gauss_noisy)
    cv2.imshow("lena_Gauss filtro gaussiano", image_gaussiano_gauss)
    cv2.imshow("estimacion del ruido con filtro gaussiano", imagen_noise_gaussiano_lenagauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # filtro gaussiano para lena_s&p_noisy

    # se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    N = 7
    image_gaussiano_syp = cv2.GaussianBlur(lena_syp_noisy, (N, N), 1.5)
    #tiempo_filtro = time()-tiempo_inicio_FG
    #tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro gaussiano para lena_syp_noisy: ", tiempo_filtro)

    # estimación del ruido con filtro gaussiano
    imagen_noise_gaussiano_lenasyp = abs(lena_syp_noisy - image_gaussiano_syp)

    # error cuadrático medio con el filtro gaussiano para lena_s&p_noisy
    ECM_filtrogaussiano_syp = ecm(image_gaussiano_syp, lena_syp_noisy)
    print("error cuadrático medio con el filtro gaussiano para lena_s&p_noisy: ", ECM_filtrogaussiano_syp)
    cv2.imshow("lena_syp", lena_syp_noisy)
    cv2.imshow("lena_syp filtro gaussiano", image_gaussiano_syp)
    cv2.imshow("estimacion del ruido con filtro gaussiano lena syp", imagen_noise_gaussiano_lenasyp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # filtro median para lena gauss
    # se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    image_median_gauss = cv2.medianBlur(lena_gauss_noisy, 7)
    #tiempo_filtro = time() - tiempo_inicio_FG
    # tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro mediana para lena_gauss_noisy: ", tiempo_filtro)

    #estimacion del ruido filtro median lena gauss
    imagen_noise_median_lenagauss=abs(lena_gauss_noisy-image_median_gauss)

    # error cuadrático medio con el filtro mediana para lena_gauss_noisy
    ECM_filtromediana_gauss = ecm(image_median_gauss, lena_gauss_noisy)
    print("\n","error cuadrático medio con el filtro mediana para lena_gauss_noisy: ", ECM_filtromediana_gauss)
    cv2.imshow("lena_Gauss", lena_gauss_noisy)
    cv2.imshow("lena_Gauss filtro mediana", image_median_gauss)
    cv2.imshow("estimacion del ruido con filtro mediana lena_gauss", imagen_noise_median_lenagauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    #filtro median para s&p
    #se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    image_median_syp = cv2.medianBlur(lena_syp_noisy, 7)
    #tiempo_filtro = time() - tiempo_inicio_FG
    #tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro mediana para lena_syp_noisy: ", tiempo_filtro)

    # estimacion del ruido filtro mediana lena syp
    imagen_noise_median_lenasyp = abs(lena_syp_noisy - image_median_syp)

    # error cuadrático medio con el filtro mediana para lena_s&p_noisy
    ECM_filtromediana_syp = ecm(image_median_syp, lena_syp_noisy)
    print("error cuadrático medio con el filtro mediana para lena_s&p_noisy: ", ECM_filtromediana_syp)
    cv2.imshow("lena_syp", lena_syp_noisy)
    cv2.imshow("lena_syp filtro mediana", image_median_syp)
    cv2.imshow("estimacion del ruido con filtro mediana lena syp", imagen_noise_median_lenasyp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # filtro bilateral con lena_gauss_noisy
    #se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    image_bilateral_gauss = cv2.bilateralFilter(lena_gauss_noisy, 15, 25, 25)
    #tiempo_filtro = time() - tiempo_inicio_FG
    #tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro bilateral para lena_gauss_noisy: ", tiempo_filtro)

    # estimacion del ruido filtro bilateral lena gauss
    imagen_noise_bilateral_lenagauss = abs(lena_gauss_noisy - image_bilateral_gauss)

    # error cuadrático medio con el filtro bilateral para lena_gauss
    ECM_filtrobilateral_gauss = ecm(image_bilateral_gauss, lena_gauss_noisy)
    print("\n","error cuadrático medio con el filtro bilateral para lena_gauss_noisy: ", ECM_filtrobilateral_gauss)
    cv2.imshow("lena_Gauss", lena_gauss_noisy)
    cv2.imshow("lena_Gauss filtro bilateral", image_bilateral_gauss)
    cv2.imshow("estimacion del ruido con filtro bilateral lena_gauss", imagen_noise_bilateral_lenagauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # filtro bilateral con lena_syp_noisy
    # se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    image_bilateral_syp = cv2.bilateralFilter(lena_syp_noisy, 15, 25, 25)
    #tiempo_filtro = time() - tiempo_inicio_FG
    # tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro bilateral para lena_syp_noisy: ", tiempo_filtro)

    #estimacion del ruido filtro bilateral lena syp
    imagen_noise_bilateral_lenasyp = abs(lena_syp_noisy - image_bilateral_syp)

    # error cuadrático medio con el filtro bilateral para lena_s&p_noisy
    ECM_filtrobilateral_syp = ecm(image_bilateral_syp, lena_syp_noisy)
    print("error cuadrático medio con el filtro bilateral para lena_s&p_noisy: ", ECM_filtrobilateral_syp)
    cv2.imshow("lena_syp", lena_syp_noisy)
    cv2.imshow("lena_syp filtro bilateral", image_bilateral_syp)
    cv2.imshow("estimacion del ruido con filtro bilateral lena syp", imagen_noise_bilateral_lenasyp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # filtro nlm con lena_gauss_noisy
    # se toma el tiempo inicial
    #tiempo_inicio_FG = time()
    image_nlm_lena_gauss = cv2.fastNlMeansDenoising(lena_gauss_noisy,5, 15, 25)
    #tiempo_filtro = time() - tiempo_inicio_FG
    # tiempo de ejecución del filtro
    #print("tiempo de ejecución del filtro nlm para lena_gauss_noisy: ", tiempo_filtro)

    #estimacion del ruido filtro nlm lena gauss
    imagen_noise_nlm_lenagauss = abs(lena_gauss_noisy - image_nlm_lena_gauss)

    # error cuadrático medio con el filtro nlm para lena_gauss
    ECM_filtronlm_gauss = ecm(image_nlm_lena_gauss, lena_gauss_noisy)
    print("\n","error cuadrático medio con el filtro nlm para lena_gauss_noisy: ", ECM_filtronlm_gauss)
    cv2.imshow("lena_Gauss", lena_gauss_noisy)
    cv2.imshow("lena_Gauss filtro nlm", image_nlm_lena_gauss)
    cv2.imshow("estimacion del ruido con filtro nlm lena_gauss", imagen_noise_nlm_lenagauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # filtro nlm con lena_syp_noisy
    # se toma el tiempo inicial
    tiempo_inicio_FG = time()
    image_nlm_lena_syp = cv2.fastNlMeansDenoising(lena_syp_noisy, 5, 15, 25)
    tiempo_filtro = time() - tiempo_inicio_FG
    # tiempo de ejecución del filtro
    print("tiempo de ejecución del filtro nlm para lena_syp_noisy: ", tiempo_filtro)

    #estimacion del ruido filtro nlm lena syp
    imagen_noise_nlm_lenasyp = abs(lena_syp_noisy - image_nlm_lena_syp)

    # error cuadrático medio con el filtro nlm para lena_s&p_noisy
    ECM_filtronlm_syp = ecm(image_nlm_lena_syp, lena_syp_noisy)
    print("error cuadrático medio con el filtro nlm para lena_s&p_noisy: ", ECM_filtronlm_syp)
    cv2.imshow("lena_syp", lena_syp_noisy)
    cv2.imshow("lena_syp filtro nlm", image_nlm_lena_syp)
    cv2.imshow("estimacion del ruido con filtro nlm lena syp", imagen_noise_nlm_lenasyp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
