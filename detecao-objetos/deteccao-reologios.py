import cv2

detector_relogio = cv2.CascadeClassifier("H:/Users/basto/Documents/visao-computacional/Cascades/clocks.xml")

imagem = cv2.imread("H:/Users/basto/Documents/visao-computacional/Images/clock.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = detector_relogio.detectMultiScale(imagem_cinza, scaleFactor=1.03, minNeighbors=1, minSize=(50,50))

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x+w, y + h), (0, 255, 0), 2)

janela = 'image'
cv2.imshow(janela, imagem)
cv2.waitKey(0)