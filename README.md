# 🧪 Laboratorio 1 - Uso de OpenCV con Python  
**Programación – I-2025 – GDSPROC – Universidad del Quindío**  
**Docente:** Alexander López-Parrado, PhD.  
**Estudiantes:** Julian Trujillo, Nicol Garcia, Vivian Montoya, Carlos Sanchez

---

## 🎯 Descripción del laboratorio
Este laboratorio tiene como objetivo aplicar conceptos básicos de procesamiento de imágenes utilizando la biblioteca OpenCV en Python. A través de una serie de retos, se busca poner en práctica habilidades de programación y visión por computador, construyendo un conjunto de programas que serán útiles para el desarrollo del proyecto final.

---

## 📦 Archivos entregados

### Punto_1.py
Genera una imagen de 640x480 píxeles con un cuadrado blanco de 200x200 píxeles en el centro, sobre un fondo negro.

### Punto_2.py
Solicita al usuario el nombre de una imagen (`blue_car.jfif`, `red_car.jfif` o `yellow_car.jfif`) y, mediante la función `identifyColor`, identifica el color del automóvil analizando los valores promedio de los canales BGR.

### punto_3.py
Detecta si un puesto de parqueo está ocupado o disponible utilizando técnicas de detección de bordes (Canny). La función `identifySpot` se encarga de este análisis.

### Imágenes
- `blue_car.jfif`
- `red_car.jfif`
- `yellow_car.jfif`

Estas imágenes se utilizan como entrada para los programas desarrollados.

---

## 💻 Ejecución de los programas
Todos los programas están escritos en Python y hacen uso de la biblioteca OpenCV. Para ejecutar correctamente cada script, es necesario tener instalada la librería ejecutando:

```bash
python -m pip install opencv-contrib-python
```

También se recomienda verificar que `pip` esté actualizado:

```bash
python -m pip install --upgrade pip
```

---

## 🧠 Retos resueltos
- Generación de imágenes monocromáticas
- Cálculo de valores promedio de color# No code was selected, so a new code snippet will be generated.

# Import necessary libraries
import cv2
import numpy as np

# Function to generate an image with a white square on a black background
def generate_image():
    # Create a black image with a size of 640x480 pixels
    image = np.zeros((480, 640, 3), np.uint8)
    
    # Draw a white square in the center of the image
    cv2.rectangle(image, (220, 140), (420, 340), (255, 255, 255), -1)
    
    # Display the generated image
    cv2.imshow('Generated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to identify the color of a car
def identify_color(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Calculate the average BGR values of the image
    average_bgr = np.mean(image, axis=(0, 1))
    
    # Identify the color based on the average BGR values
    if average_bgr[0] > average_bgr[1] and average_bgr[0] > average_bgr[2]:
        return 'Blue'
    elif average_bgr[1] > average_bgr[0] and average_bgr[1] > average_bgr[2]:
        return 'Green'
    else:
        return 'Red'

# Function to detect if a parking spot is occupied or available
def identify_spot(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Count the number of edges
    edge_count = np.count_nonzero(edges)
    
    # Determine if the parking spot is occupied or available
    if edge_count > 10000:
        return 'Occupied'
    else:
        return 'Available'

# Main function
def main():
    # Generate an image with a white square on a black background
    generate_image()
    
    # Identify the color of a car
    image_path = 'blue_car.jfif'
    color = identify_color(image_path)
    print(f'The color of the car is: {color}')
    
    # Detect if a parking spot is occupied or available
    image_path = 'parking_spot.jpg'
    spot_status = identify_spot(image_path)
    print(f'The parking spot is: {spot_status}')

if __name__ == '__main__':
    main()
- Identificación de colores con funciones
- Detección de puestos ocupados/libres mediante procesamiento de bordes

---

## 👤 Autores
**Julian Trujillo**  
**Nicol Garcia**  
**Vivian Montoya**  
**Carlos Sanchez**  

Estudiantes de Ingeniería Electrónica  
Universidad del Quindío