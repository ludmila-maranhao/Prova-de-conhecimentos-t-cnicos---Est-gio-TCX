import cv2
import numpy as np

#carregar uma imagem escolhida
img = cv2.imread('IMG_9045.jpg', cv2.IMREAD_UNCHANGED)

# conversão da imagem para uma escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# realização de uma operação de limiarização binária
ret, img_thresh = cv2.threshold(img_gray, 145, 255, cv2.THRESH_BINARY)

# detecção dos contornos na imagem limiarizada
contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#desenho de retângulos ao redor dos objetos detectados
for c in contours:
  x, y, w, h = cv2.boundingRect(c)
 
    # conferir se o tamanho dos contornos são grandes o suficiente, para não ocorrer erros devido ao ruído da imagem
  if (cv2.contourArea(c)) > 1500:
    cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0), 5)

# exibição da imagem final com os retângulos
cv2.imshow('Imagem Final com Retângulos', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()