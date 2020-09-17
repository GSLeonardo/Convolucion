import cv2
import numpy as np
ruta = 'perro1.png'
im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('Normal.png',im)
a = [[-1,0,1],
             [-1,0,1],
                  [-1,0,1]]
kernel = np.asarray(a)
filtro = cv2.filter2D(im, -1, kernel)
cv2.imwrite('Convolucion.png',filtro)
