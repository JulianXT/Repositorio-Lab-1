import cv2
import numpy as np

def identifyColor(image_number):
    # Rutas
    if image_number == 1:
        image_path = r"C:\Users\nicol\OneDrive\Documentos\red_car.jfif"
    elif image_number == 2:
        image_path = r"C:\Users\nicol\OneDrive\Documentos\yellow_car.jfif"
    elif image_number == 3:
        image_path = r"C:\Users\nicol\OneDrive\Documentos\blue_car.jfif"
    else:
        print("Error: Número no válido. Debe ser 1, 2 o 3.")
        return

    # Leer imagen
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Error: No se pudo cargar la imagen en la ruta: {image_path}")
        return

    # Promedios
    blue = np.mean(img[:, :, 0])
    green = np.mean(img[:, :, 1])
    red = np.mean(img[:, :, 2])

    print(f"Promedios - Rojo: {red:.2f}, Verde: {green:.2f}, Azul: {blue:.2f}")

    # Detección de color con lógica afinada
    if red > 100 and green > 100 and abs(red - green) < 15 and blue < red and blue < green:
        print("El color predominante es AMARILLO")
    elif red > blue and red > green:
        print("El color predominante es ROJO")
    elif blue > red and blue > green:
        print("El color predominante es AZUL")
    else:
        print("No se pudo identificar el color como rojo, azul o amarillo")

# Menú
print("Seleccione la imagen a analizar:")
print("1 - red_car.jfif")
print("2 - yellow_car.jfif")
print("3 - blue_car.jfif")

# Ejecutar
try:
    image_number = int(input("Ingrese el número de la imagen (1, 2 o 3): "))
    identifyColor(image_number)
except ValueError:
    print("Error: Debe ingresar un número válido (1, 2 o 3).")
        
#Julian Trujillo
#Nicol Garcia
#Carlos Sanchez
#Vivian Montoya