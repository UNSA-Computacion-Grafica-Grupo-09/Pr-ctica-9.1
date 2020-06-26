
import cv2
import math as mt
import numpy as np
from matplotlib import pyplot as plt


    




def trasladar_imagen(image):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    
    #Matriz de traslacion
    # matriz de transformacion 2x3
    
    #     [1,0,t_x]
    # M = [0,1,t_y]

    A=[[2,0],[0,2]]

    def Affines(image,M,dim ) :
            fil , col = image.shape [0:2]#tomamos las dimensiones
            #img_res = np.zeros ([ dim[1],dim[0],3] , dtype = np . uint8 )
            image_res=np.zeros((fil,col,3),np.uint8)#Creamos nuestra matriz para la respuesta
            A = M [:2,:2]
            B = M [:,2:]
            for i in range ( fil ):#tomamos las dimensiones
                for j in range ( col ) :
                    res = np.dot(A,np.float32([[i],[j]]))+B #aplicamos la operacion A*M+B
                    res = np.uint32(res)
                    if res[0,0]>=dim[1] or res[1,0]>=dim[0]:
                        continue

                    image_res [res[0,0],res[1,0]] = image[i,j]#colocaos en su pixel correspondiente
            return image_res



    M = np.float32([[1,0,10],[0,1,100]])
    #imageOut = AffineO(img,M , (ancho, alto))
    imageOut = Affines(img,M , (ancho, alto))
            
    return imageOut

imagen1 = cv2.imread("goose.jpg")
result = trasladar_imagen(imagen1)
cv2.imwrite("tras_imagenAffine.jpg", result)
cv2.waitKey(0)