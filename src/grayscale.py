import cv2 as cv
import numpy as np

img = cv.imread(".\imagens\RGB.png");
img = np.float32(img);

imgGray= np.zeros(img.shape[:2], dtype="uint8");

imgGray[:, :] = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2])/3;

cv.namedWindow("Janela", 1);

cv.imshow("Janela", img);
cv.imshow("CANAL AZUL", imgGray);

cv.waitKey(0);

