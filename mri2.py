import cv2
import matplotlib.pyplot as plt

img = cv2.imread(‘flower.jpg‘,0)
edges = cv2.Canny(img,100,200)#其他的默认
plt.subplot(121),plt.imshow(img,‘gray‘)
plt.subplot(122),plt.imshow(edges,‘gray‘)