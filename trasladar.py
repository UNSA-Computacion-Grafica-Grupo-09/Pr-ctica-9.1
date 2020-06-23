import cv2
import numpy as np

def traslate(image):
    #img = image.copy()

    #img1 = cv2.cvtColor(image.copy(),1)
    img1 = cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)


    ancho = img1.shape[1]  #Columnas
    alto = img1.shape[0] #Filas
 

    #Matriz de traslacion
    # matriz de transformacion 2x3
    
    #     [1,0,t_x]
    # M = [0,1,t_y]
    
    #cv2.warpAffine(ie, M, tam )
    # ie = imagen de entrada
    # M = matriz de transformacion 2x3
    # tam = tamano de la imagen de salida
    
    I = np.eye(ancho,alto)
    #Direcciones=np.array([4,4])
    Direcciones=np.matrix([[1],[1]])
    Multi=np.dot(I,img1)
    
    img1=Multi#+Direcciones
    #img1=I*img1+Direcciones


    #M = np.float32([[1,0,10],[0,1,100]])
    #imageOut = cv2.warpAffine(img, M , (ancho, alto))

    #Ident= np.array([[1, 0, 0],
    #                    [0, 1, 0],
    #                    [0, 0, 1]])

    #M = np.float32([[1,0,10],[0,1,100]])
    #translate_by=[[],[],[]]
    #matrix = np.array([[1, 0, Ident[0]],
    #                    [0, 1, Ident[1]],
    #                    [0, 0, 1]])

    #return np.dot(matrix, data)


        
    return img1

imagen1 = cv2.imread("goose.jpg")
result = traslate(imagen1)
cv2.imwrite("tras_imagen.jpg", result)
cv2.waitKey(0)