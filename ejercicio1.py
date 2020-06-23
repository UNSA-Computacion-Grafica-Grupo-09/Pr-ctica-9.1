# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:00:40 2020

@author: MILAGROS PC
"""

import cv2
import numpy as np
import imutils
import math

def trasladar_imagen(image):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    
    #Matriz de traslacion
    # matriz de transformacion 2x3
    
    #     [1,0,t_x]
    # M = [0,1,t_y]
    
    #cv2.warpAffine(ie, M, tam )
    # ie = imagen de entrada
    # M = matriz de transformacion 2x3
    # tam = tamaño de la imagen de salida
    
    # M = np.float32([[2, 0, 0], [0, 2, 0]])
    # dst=cv2.warpAffine(img1, M, (c, f))
    
    M = np.float32([[1,0,10],[0,1,100]])
    imageOut = cv2.warpAffine(img, M , (ancho, alto))
        
    return imageOut

# imagen1 = cv2.imread("goose.jpg")
# result = trasladar_imagen(imagen1)
# cv2.imwrite("tras_imagen.jpg", result)
# cv2.waitKey(0)

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
   
    M = matrix_rotacion(0.261799, ancho//2, alto//2)
    imageOut = cv2.warpAffine(img, M , (ancho, alto))
        
    return imageOut

imagen1 = cv2.imread("marvel.jpg")
result = rotar_imagen(imagen1)
cv2.imwrite("rot_imagen_pru.jpg", result)
cv2.waitKey(0)

def escalar_imagen(image, tx, ty):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    
    M = np.array([[tx,0,0],[0,ty,0]], dtype = np.float32)
    imageOut = cv2.warpAffine(img, M , (ancho, alto))    
    
    return imageOut

# imagen1 = cv2.imread("marvel2.jpg")
# result = escalar_imagen(imagen1, 0.8, 1.5)
# cv2.imwrite("esc_imagen.jpg", result)
# cv2.waitKey(0)

def shear_imagen(image):
    img = image.copy()
    ancho = img.shape[1]  #Columnas
    alto = img.shape[0] #Filas
    
    M = np.float32([[1, 0.2, 0], [0.2, 1, 0]]) 
    imageOut = cv2.warpAffine(image, M, (ancho, alto))
        
    return imageOut
  
       
# imagen1 = cv2.imread("batman.jpg")
# result = shear_imagen(imagen1)
# cv2.imwrite("recort_imagen.jpg", result)
# cv2.waitKey(0)