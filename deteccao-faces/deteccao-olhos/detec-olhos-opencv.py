import cv2

# Preparando imagem
imagem = cv2.imread('../../images/people1.jpg')
#imagem = cv2.resize(imagem, (800,600))
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Modelo facial
detector_facial = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

deteccoes = detector_facial.detectMultiScale(imagem_cinza, scaleFactor = 1.3, minSize=(30,30))

for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 3)

detector_olhos = cv2.CascadeClassifier('../haarcascade_eye.xml')

deteccoes_olhos = detector_olhos.detectMultiScale(imagem_cinza, scaleFactor=1.09, minNeighbors=10, maxSize=(70,70))

for (x, y, w, h) in deteccoes_olhos:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 255), 2)

janela = 'image'
cv2.imshow(janela, imagem)
cv2.waitKey(0)
