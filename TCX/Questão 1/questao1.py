import cv2 
img = cv2.imread('IMG_8945.jpg')

# redimencionamento da imagem para que se ajuste ao ecrã
scale_percent = 15 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# redimencionamento da imagem
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# conversão da imagem para uma escala de cinza
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# aplicação de um filtro de média com um kernel 3x3
filter_img = cv2.blur(gray_img, ksize=(3,3))

# realização de uma operação de limiarização
ret,thresh_img = cv2.threshold(filter_img, 127,255 ,cv2.THRESH_TRUNC)

cv2.imshow('Imagem Final', thresh_img) 
cv2.waitKey(0)
cv2.destroyAllWindows()