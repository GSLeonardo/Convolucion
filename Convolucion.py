import numpy as np
import cv2

img = cv2.imread('/home/leogalindo01/Documents/GitHub/Convolucion/Goku.jpeg') #Transformar la imagen a numpy array
#cv2.namedWindow("Original", cv2.WINDOW_KEEPRATIO)
#cv2.imshow("Original", img)#Mostrar imagen original
#cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Cambiar la imagen a blanco y negro
#cv2.namedWindow("Before", cv2.WINDOW_KEEPRATIO)
#cv2.imshow("Before", gray)#Mostrar imagen en blanco y negro, antes del filtro 
#cv2.waitKey(0)

row, col = gray.shape
new_img = np.zeros(gray.shape)

#Kernels
#kernel = [[-1,0,1],[-1,0,1],[-1,0,1]]
#kernel = [[1,0,-1],[1,0,-1],[1,0,-1]]
#kernel = [[1,1,1],[0,0,0],[-1,-1,-1]]
#kernel = [[-1,-1,-1],[0,0,0],[1,1,1]]
#kernel = [[-1,0,1],[-2,0,2],[-1,0,1]]
#kernel = [[1,0,-1],[2,0,-2],[1,0,-1]]
#kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
#kernel = [[0.1,0.1,0.1],[0.1,0.1,0.1],[0.1,0.1,0.1]]
padding = 2
for i in range(padding, row-padding):
    for j in range(padding, col-padding):
        kernel = [[2,4,5,4,2],[4,9,12,9,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]]#Kernel de la imagen
        count = 0
        for y in range(5):
            for x in range(5):  
                kernel[y][x] *= gray[y+i-padding][x+j-padding]
                count += kernel[y][x]
                count *= 1.0/159
        new_img[i][j] = count

print(new_img)
cv2.namedWindow("New", cv2.WINDOW_KEEPRATIO)
cv2.imshow("New", new_img)#imagen con el nuevo filtro
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows