import numpy as np
import cv2

img = cv2.imread("/Users/ana/Documents/Imagenes/ojo.jpg") #Transformar la imagen a numpy array
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
for i in range(1, row-1):
    for j in range(1, col-1):
        kernel = [[1,1,1],[0,0,0],[-1,-1,-1]]#Kernel de la imagen
        count = 0
        for y in range(3):
            for x in range(3):
                kernel[y][x] *= gray[y+i-1][x+j-1]
                count += kernel[y][x]
        new_img[i][j] = count

#kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
#kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#img_prewittx = cv2.filter2D(new_img, -1, kernelx)
#img_prewitty = cv2.filter2D(new_img, -1, kernely)
#cv2.imshow("Prewitt X", new_img)
#cv2.imshow("Prewitt Y", new_img)

#print(new_img)
#print(new_img[0][0])
#cv2.namedWindow("New", cv2.WINDOW_KEEPRATIO)
cv2.imshow("New", new_img)#imagen con el nuevo filtro
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
