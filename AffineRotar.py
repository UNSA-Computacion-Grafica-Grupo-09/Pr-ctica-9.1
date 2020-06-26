

import cv2
import numpy as np
#import imutils
import math

def rotar_imagen(image):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    
    # def matrix_rotate(angulo, tx, ty):
    # angulo = angulo de rotcion en rdianes 
    # tx = el centro de la imagen en x
    # ty = el centro de la imagen en y
    
    #Matriz de rotación
    
    def matrix_rotacion(angulo, tx, ty):
        coseno = math.cos(angulo)
        seno = math.sin(angulo)
        calcular_1 = (1 - coseno) * tx - seno * ty
        calcular_2 = seno*tx+(1 - coseno)*ty
        return np.array([[coseno, seno, calcular_1], [-seno, coseno, calcular_2]], dtype=np.float32)
        #M = np.float32([[tx,0,0],[0,ty,0]])
    #M = matrix_rotacion(0.261799, ancho//2, alto//2)


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




    M = matrix_rotacion(1.56, ancho//2, alto//2)
    imageOut = Affines(img, M , (ancho, alto))
        
    return imageOut

imagen1 = cv2.imread("marvel.jpg")
result = rotar_imagen(imagen1)
cv2.imwrite("Affine_rot_imagen_pru.jpg", result)
cv2.waitKey(0)