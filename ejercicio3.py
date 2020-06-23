import cv2
import numpy as np

def crear_img(image):
    filas = image.shape[0]
    columas = image.shape[1]
    array = cv2.resize(image, (((columas * 2) - 1), ((filas * 2) - 1)))
    for i in range(array.shape[0] - 1):
        for j in range(array.shape[1] - 1):
            array[i][j] = 0
    return array


#promedio entre valores
def promedio(valor1, valor2):
    prome = np.copy(valor1)
    for i in range(3):
        prome[i] = (int(valor1[i])+int(valor2[i]))/2
    return prome


def interpolacion(image):
    filas = image.shape[0]
    columas = image.shape[1]
    arr = crear_img(image)

    for k in range(filas-1):
        for h in range(columas - 1):
            nk = k * 2
            nh = h * 2
            arr[nk][nh] = image[k][h]
            arr[nk][nh+2] = image[k][h+1]
            arr[nk+2][nh] = image[k+1][h]
            arr[nk+2][nh+2] = image[k+1][h+1]
            arr[nk][nh+1] = promedio(image[k][h],image[k][h+1])
            arr[nk+1][nh] = promedio(image[k][h],image[k+1][h])
            arr[nk+1][nh+2] = promedio(image[k][h+1],image[k+1][h+1])
            arr[nk+2][nh+1] = promedio(image[k+1][h],image[k+1][h+1])
            arr[nk+1][nh+1] = promedio(arr[nk+1][nh],arr[nk+1][nh+2])
    return arr

imagen1 = cv2.imread("marvel.jpg")
result = interpolacion(imagen1)
cv2.imwrite("res_Interpolacion.png", result)

cv2.waitKey(0)  


