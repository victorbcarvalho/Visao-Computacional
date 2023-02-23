import cv2

detector_carros = cv2.CascadeClassifier('H:/Users/basto/Documents/visao-computacional/Cascades/cars.xml')

imagem = cv2.imread('H:/Users/basto/Documents/visao-computacional/Images/car.jpg')
imagem = cv2.resize(imagem, (800,600))
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = detector_carros.detectMultiScale(imagem_cinza, scaleFactor=1.02, minNeighbors=3, minSize=(40,40))

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 3)

janela = 'image'
cv2.imshow(janela, imagem)
cv2.waitKey(0)