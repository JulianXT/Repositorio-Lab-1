# Import OpenCV module
import cv2

# Read image
img = cv2.imread(r"C:\Users\Santiago\Desktop\blue_car.jfif", cv2.IMREAD_COLOR)

# Get image dimensions
dims = img.shape
print(f'Image has {dims[2]} color planes each having {dims[0]} rows and {dims[1]} columns')

# Get matrix for each color plane
bluePlane = img[:, :, 0]
greenPlane = img[:, :, 1]
redPlane = img[:, :, 2]

# Show image and each color plane
cv2.imshow("Image", img)
cv2.imshow("Blue Plane", bluePlane)
cv2.imshow("Green Plane", greenPlane)
cv2.imshow("Red Plane", redPlane)

# Function to compute the mean of a plane
def compute_mean(plane, name):
    dims = plane.shape
    mean = 0.0
    for row in plane:
        for p in row:
            mean += p
    mean /= (dims[0] * dims[1])
    print(f'Mean of {name} plane is: {mean:.2f}')

# Compute and display mean for each plane
compute_mean(bluePlane, "blue")
compute_mean(greenPlane, "green")
compute_mean(redPlane, "red")

# Wait for key
cv2.waitKey()
cv2.destroyAllWindows()
