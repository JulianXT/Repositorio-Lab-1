import cv2
import numpy as np

# Dirección de la cámara del celular
video_path = "http://192.168.1.9:4747/video" #la IP del celular

def detect_parking_space(frame):
    """ Detecta si el espacio de parqueo está ocupado con Canny. """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)  

    # Definir la región del espacio de parqueo
    x, y, w, h = 150, 150, 250, 250  # Ajusta según la ubicación real
    parking_zone = edges[y:y+h, x:x+w]

    # Contar los píxeles con bordes
    edge_count = np.sum(parking_zone > 0)

    # Ajustar umbral de detección
    ocupado = edge_count > 1500  

    return ocupado, edges, (x, y, w, h)

def detect_car_color(frame, x, y, w, h):
    """ Detecta el color del carro en el espacio de parqueo. """
    roi = frame[y:y+h, x:x+w]  # Recortar la zona del parqueo
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Definir rangos de colores en HSV
    color_ranges = {
        "Rojo": [(0, 100, 100), (10, 255, 255)],
        "Verde": [(40, 50, 50), (75, 255, 255)],
        "Azul": [(90, 50, 50), (130, 255, 255)]
    }

    detected_color = "Desconocido"

    for color, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        if np.sum(mask) > 5000:  # Ajusta el umbral de detección de color
            detected_color = color
            break

    return detected_color

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección de espacio de parqueo y bordes
    ocupado, edges, (x, y, w, h) = detect_parking_space(frame)

    if ocupado:
        color = detect_car_color(frame, x, y, w, h)
        print(f"🚗 Espacio ocupado - Color del carro: {color}")
    else:
        print("🟢 Espacio libre")

    # Mostrar la imagen original (a color) sin rectángulos ni marcas
    cv2.imshow("Detección de Color", frame)

    # Mostrar la imagen con bordes Canny
    cv2.imshow("Detección de Bordes - Canny", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

#Julian Trujillo
#Nicol Garcia
#Carlos Sanchez
#Vivian Montoya