import cv2
import numpy as np
#import imutils
import math

def escalar_imagen(image, tx, ty):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    M = np.float32([[tx,0,0],[0,ty,0]])
    
    #M = np.array([[tx,0,0],[0,ty,0]], dtype = np.float32)


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


    imageOut = Affines(img, M , (ancho, alto))    
    
    return imageOut

imagen1 = cv2.imread("marvel2.jpg")

result = escalar_imagen(imagen1, 0.6, 0.5)
cv2.imwrite("Affine_esc_imagen2.jpg", result)
cv2.waitKey(0)