import numpy as np
import cv2

img = cv2.imread('DSC_0058.jpg') #Transformar la imagen a numpy array

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Cambiar la imagen a blanco y negro


row, col = gray.shape
new_img = np.zeros(gray.shape)

for i in range(1, row-1):
    for j in range(1, col-1):
        kernel = [[0,1,0],[1,-4,1],[0,1,0]]#Kernel de la imagen
        count = 0
        for y in range(3):
            for x in range(3):  
                kernel[y][x] *= gray[y+i-1][x+j-1]
                count += kernel[y][x]
        new_img[i][j] = count

print(new_img)
print(new_img[0][0])
cv2.namedWindow("New", cv2.WINDOW_KEEPRATIO)
cv2.imshow("New", new_img)#imagen con el nuevo filtro
cv2.waitKey(0)
cv2.destroyAllWindows