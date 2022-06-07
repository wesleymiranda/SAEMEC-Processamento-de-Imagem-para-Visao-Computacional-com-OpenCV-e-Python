import cv2 as cv
import numpy as np

img = cv.imread(".\imagens\RGB.png");

imgB = np.zeros(img.shape[:], dtype="uint8");
imgG = np.zeros(img.shape[:], dtype="uint8");
imgR = np.zeros(img.shape[:], dtype="uint8");

imgB[:, :, 0] = img[:, :, 0];
imgG[:, :, 1] = img[:, :, 1];
imgR[:, :, 2] = img[:, :, 2];

cv.imshow("IMAGEM ORIGINAL", img);
cv.imshow("CANAL AZUL", imgB);
cv.imshow("CANAL VERDE", imgG);
cv.imshow("CANAL VERMELHO", imgR);

cv.waitKey(0);

