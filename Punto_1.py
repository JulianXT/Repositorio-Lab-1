import cv2
import numpy as np

##Crear una imagen negra de 640(ancho)x480(alto)

imagen_cuadrado = np.zeros((480, 640), dtype=np.uint8)

# Dibuja el cuadrado blanco en el centro
##225 es blanco 
x, y, size = 220, 140, 200  # Coordenadas superiores izquierdas y tamaño
imagen_cuadrado[y:y+size, x:x+size] = 225

# mostrar ka imagen 
cv2.imwrite("cuadrado.png", imagen_cuadrado)
cv2.imshow("Imagen", imagen_cuadrado)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Julian Trujillo
#Nicol Garcia
#Carlos Sanchez
#Vivian Montoya