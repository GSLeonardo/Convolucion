<<<<<<< HEAD
import numpy as np
import cv2

img = cv2.imread('/home/leogalindo01/Documents/GitHub/Convolucion/horizon.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
#cv2.imshow("Before", gray)
#cv2.waitKey(0)
#print(gray)
#cv2.imshow("Old",img)
#cv2.waitKey(0)
rows = gray[0].tolist
col = gray[1].tolist
new_img = [rows, col]
print(len(new_img))
print(new_img[0])
#loops = gray.shape
filter = [[-1,-1,-1],[0,0,0],[1,1,1]]
count = 0
for i in range(2):
    for j in range(1, 1558):
        for k in range(1, 2500):
            for y in range(3):
                for x in range(3):  
                    filter[y][x] *= new_img[i][y+j-1][x+k-1]
                    count += filter[y][x]
            filter = [[-1,-2,-1],[0,0,0],[1,2,1]]
            new_img[i][j][k] = count
            count = 0

print(new_img)
cv2.imshow("New", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows