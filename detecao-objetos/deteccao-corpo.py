import cv2

detector_corpo = cv2.CascadeClassifier('H:/Users/basto/Documents/visao-computacional/Cascades/fullbody.xml')

imagem = cv2.imread('H:/Users/basto/Documents/visao-computacional/Images/people3.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = detector_corpo.detectMultiScale(imagem_cinza, scaleFactor=1.05, minNeighbors=5, minSize=(50, 50))

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

janela = 'image'
cv2.imshow(janela, imagem)
cv2.waitKey(0)