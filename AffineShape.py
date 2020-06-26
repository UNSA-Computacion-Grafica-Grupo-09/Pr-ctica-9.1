import cv2
import numpy as np
#import imutils
import math

def shear_imagen(image):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    

    def Affines(image,M,dim ) :
            fil , col = image.shape [0:2]#tomamos las dimensiones
            #img_res = np.zeros ([ dim[1],dim[0],3] , dtype = np . uint8 )
            image_res=np.zeros((fil,col,3),np.uint8)#Creamos nuestra matriz para la respuesta
            A = M [:2,:2]
            B = M [:,2:]
            for i in range ( fil ):#tomamos las dimensiones
                for j in range ( col ) :
                    res = np.dot(A,np.float32([[i],[j]]))+B #aplicamos la operacion A*[x1,y1]+B
                    res = np.uint32(res)
                    if res[0,0]>=dim[1] or res[1,0]>=dim[0]:
                        continue

                    image_res [res[0,0],res[1,0]] = image[i,j]#colocaos en su pixel correspondiente
            return image_res


    #M=[[1, shy, 0], [shx, 1, 0]]
    M = np.float32([[1, 0.3, 0], [0.2, 1, 0]]) #shx
    imageOut = Affines(image, M, (ancho, alto))
        
    return imageOut


  
       
imagen1 = cv2.imread("batman.jpg")
result = shear_imagen(imagen1)
cv2.imwrite("Affine_shear_imagen.jpg", result)
cv2.waitKey(0)