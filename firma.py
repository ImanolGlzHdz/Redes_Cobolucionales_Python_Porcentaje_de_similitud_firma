import numpy as np
import cv2
#aqui las 2 imagenes se obtienen
imagen = cv2.imread("firma1.png")
imagen2 = cv2.imread("firma1.png")
#aqui se transforman a arreglo
imagenarreglo = np.asarray(imagen)
imagenarreglo2 = np.asarray(imagen2)

#variables para el porcentaje de similitud
porcentaje=0
porcentaje2=0
#variables de el tamaño de la imagen
ancho = len(imagenarreglo[0])
alto = len(imagenarreglo)

#for, para comparar cada pixel
for y in range(alto):
    for x in range(ancho):
        pixel = imagenarreglo[y][x]
        pixel2 = imagenarreglo2[y][x]
        
        promedio = (pixel[0] + pixel[1] + pixel[2])/1
        promedio2 = (pixel2[0] + pixel2[1] + pixel2[2])/1
        
        if promedio>100:
            promedio=255
            
        if promedio<100:
            porcentaje=porcentaje+1
            promedio=0
            
        if promedio2>100:
            promedio2=255
            
        if promedio2<100:
            promedio2=0
            
        if promedio==0:
            if promedio2==0:
                porcentaje2=porcentaje2+1.001
            
        imagenarreglo[y][x][0] = promedio
        imagenarreglo[y][x][1] = promedio
        imagenarreglo[y][x][2] = promedio



cien=100
porcentaje=cien/porcentaje
porcentaje2=porcentaje2*porcentaje

#este es el que debes de retornar a la pagina web
print(porcentaje2)

