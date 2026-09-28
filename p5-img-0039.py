import cv2
# Leer la imagen con cv2 = computer vision
img = cv2.imread('kaicenat.jpg')
# Determina el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles (795, 735, 3)
print(img.shape)
# Mostrando imagen en ventana barra de titulo Kai Cenat 0039
cv2.imshow('Kai Cenat 0039', img)
## Tiempo de espera
cv2.waitKey(0)
# Destruir todas las ventanas
cv2.destroyAllWindows()