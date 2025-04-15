import cv2
import numpy as np

def identifyColor(image_number):
    # Definir rutas absolutas para las imágenes
    if image_number == 1:
        image_path = r"C:\Users\Santiago\Desktop\blue_car.jfif"
    elif image_number == 2:
        image_path = r"C:\Users\Santiago\Desktop\red_car.jfif"
    elif image_number == 3:
        image_path = r"C:\Users\Santiago\Desktop\yellow_car.jfif"
    else:
        print("Error: Número no válido. Debe ser 1, 2 o 3.")
        return

    # Cargar la imagen
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Verificar si la imagen se cargó correctamente
    if img is None:
        print(f"Error: No se pudo cargar la imagen en la ruta: {image_path}")
        return
    
    # Obtener los valores de los tres canales de color
    bluePlane = img[:, :, 0]
    greenPlane = img[:, :, 1]
    redPlane = img[:, :, 2]

    # Calcular el promedio de cada canal
    promedio_r = np.mean(redPlane)
    promedio_g = np.mean(greenPlane)
    promedio_b = np.mean(bluePlane)

    print(f"Blue: {promedio_b}, Green: {promedio_g}, Red: {promedio_r}")

    # Identificación del color
    if promedio_r > 100 and promedio_g > 100 and promedio_b > 100:
        print("El color predominante es amarillo")
    elif promedio_r > 100 and promedio_g < 100 and promedio_b < 100:
        print("El color predominante es rojo")
    elif promedio_b > 100 and promedio_r < 100 and promedio_g < 100:
        print("El color predominante es azul")
    else:
        print("No se pudo identificar un color predominante")

# Mostrar opciones al usuario
print("Seleccione la imagen a analizar:")
print("1 - blue_car.jfif")
print("2 - red_car.jfif")
print("3 - yellow_car.jfif")

# Pedir al usuario que seleccione una opción
try:
    image_number = int(input("Ingrese el número de la imagen (1, 2 o 3): "))
    identifyColor(image_number)
except ValueError:
    print("Error: Debe ingresar un número válido (1, 2 o 3).")
    
#Julian Trujillo
#Nicol Garcia
#Carlos Sanchez
#Vivian Montoya