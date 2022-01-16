from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im):
    decodedObjects = pyzbar.decode(im)

    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects

def display(im, decodedObjects):
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        if len(points) > 4:
            hull = list(map(tuple, np.squeeze(hull)))
        else :
            hull = points;

        n = len(hull)

        for j in range(0,n):
            cv2.line(im, hull[j], hull[(j+1)%n], (255,0,0), 2)

    cv2.imshow('Detect', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    im = cv2.imread('C:\\Users\\user\\anaconda3\\envs\\env-01\\image\\bar1.jpeg')
    decodedObjects = decode(im)
    display(im, decodedObjects)



'''# path
path = r'C:\\Users\\user\\anaconda3\\envs\\env-01\\image\\bar1.jpeg'
  
# Using cv2.imread() method
img = cv2.imread(path)

img = cv2.resize(img, (620,480) )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
# Displaying the image
cv2.imshow('image', edged)

cv2.waitKey(0)
cv2.destroyAllWindows()'''